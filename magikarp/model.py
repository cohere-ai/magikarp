import functools
from typing import Optional

import numpy as np
from torch.nn import Embedding
from transformers import AutoConfig, AutoModelForCausalLM, AutoModelForSequenceClassification, AutoTokenizer

from magikarp.utils import oov_distance_metrics

try:
    import hf_olmo
except:
    pass


class ModelAnalyzer:
    def __init__(
        self,
        model_id: str,
        known_unused_tokens: Optional[list[int]] = None,
        trust_remote_code: bool = False,
        vocab_size_lb: int = 0,
    ):
        """Analyze a model for unused tokens.
        * model_id: The model id to analyze
        * known_unused_tokens: A list of token ids that are known to be unused in the model
        * trust_remote_code: Whether to trust the remote model code for huggingface
        * vocab_size_lb: The lower bound for the vocabulary size, in case the model has multiple embedding modules
        """
        xargs = dict(use_mamba_kernels=False) if "Jamba" in model_id else {}  # Jamba crashes by default
        self.model = AutoModelForCausalLM.from_pretrained(model_id, trust_remote_code=trust_remote_code, **xargs)
        #        self.model.config.use_mamba_kernels = False # Jamba
        self.tied_embeddings = self.model.config.tie_word_embeddings
        l = [
            module
            for module in self.model.modules()
            if isinstance(module, Embedding) and module.weight.shape[0] >= vocab_size_lb
        ]
        assert len(l) == 1, f"Expected 1 Embedding module with dimension >= {vocab_size_lb}, but found {len(l)}: {l}"
        self.embeddings = l[0].weight.detach().numpy()
        if hasattr(self.model, "lm_head"):
            unembedding_head = self.model.lm_head
        elif hasattr(self.model, "embed_out"):  # NeoX
            unembedding_head = self.model.embed_out
        elif hasattr(self.model, "model") and hasattr(self.model.model, "transformer"):
            unembedding_head = self.model.model.transformer.ff_out  # OLMo
            self.tied_embeddings = False  # OLMo config uses own convention (weight_tying)
        else:
            raise AttributeError("Could not find the unembedding layer in the model")

        self.unembedding = unembedding_head.weight.detach().numpy()
        self.unembedding_has_bias = (
            unembedding_head.bias is not None and np.linalg.norm(unembedding_head.bias.detach().numpy()) > 1e-3
        )
        if self.unembedding_has_bias:
            print(
                f"Unexpectedly found bias in the final layer, this is may reduce effectiveness of metrics in ways that is out of scope of this code, especially if tied_embeddings is True (it is {self.tied_embeddings}) or unembedding metrics are needed otherwise."
            )
            self.unembedding_bias = unembedding_head.bias.detach().numpy()
        self.known_unused_tokens = [] if known_unused_tokens is None else known_unused_tokens
        self.calculate_unused_token_metric()

    # for plot labels and such
    INDICATOR_UNEMBED_WO1PC_NAME = "Unemb. OOV Cosine Distance w/o 1st PC"
    INDICATOR_UNEMBED_NAME = "Unemb. OOV Cosine Distance"
    INDICATOR_UNEMBED_L2DIST_NAME = "Unemb. OOV L2 Distance"
    INDICATOR_UNEMBED_BIAS_NAME = "Unembedding Bias"
    INDICATOR_EMBED_L2NORM_NAME = "Embeddings L2 Norm"

    def calculate_unused_token_metric(self):
        if self.tied_embeddings:
            assert (
                self.known_unused_tokens is not None and len(self.known_unused_tokens) > 0
            ), "known_unused_tokens must be provided for tied embeddings"
            embedding_distances = oov_distance_metrics(self.embeddings, self.known_unused_tokens)

            self.metric_names = [
                self.INDICATOR_UNEMBED_WO1PC_NAME,
                self.INDICATOR_UNEMBED_NAME,
                self.INDICATOR_UNEMBED_L2DIST_NAME,
            ]
            self.undertrained_token_metrics = np.stack(
                [
                    embedding_distances.cosine_distance_without_first_pc,
                    embedding_distances.cosine_distance,
                    embedding_distances.l2_distance,
                ],
                axis=-1,
            )
        else:
            l2_norm = np.linalg.norm(self.embeddings, axis=1)
            self.metric_names = [self.INDICATOR_EMBED_L2NORM_NAME]
            if len(self.known_unused_tokens) != 0:
                unemb_distances = oov_distance_metrics(self.unembedding, self.known_unused_tokens)
                self.undertrained_token_metrics = np.stack(
                    [
                        l2_norm,
                        unemb_distances.cosine_distance_without_first_pc,
                        #   unemb_distances.cosine_distance,
                        unemb_distances.l2_distance,
                    ],
                    axis=-1,
                )
                self.metric_names += [
                    self.INDICATOR_UNEMBED_WO1PC_NAME,
                    self.INDICATOR_UNEMBED_L2DIST_NAME,
                ]
            else:  # keep 2d like the other case
                self.undertrained_token_metrics = l2_norm[:, np.newaxis]
        if self.unembedding_has_bias:
            self.metric_names += [self.INDICATOR_UNEMBED_BIAS_NAME]
            self.undertrained_token_metrics = np.concatenate(
                [self.undertrained_token_metrics, self.unembedding_bias[:, np.newaxis]], axis=-1
            )
