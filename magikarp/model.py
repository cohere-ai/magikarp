import functools
from typing import Optional

import numpy as np
from torch.nn import Embedding
from transformers import AutoModelForCausalLM

from magikarp.utils import embedding_distance_metrics


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
        self.tied_embeddings = self.model.config.tie_word_embeddings
        l = [
            module
            for module in self.model.modules()
            if isinstance(module, Embedding) and module.weight.shape[0] >= vocab_size_lb
        ]
        assert len(l) == 1, f"Expected 1 Embedding module with dimension >= {vocab_size_lb}, but found {len(l)}: {l}"
        self.embeddings = l[0].weight.detach().numpy()
        if hasattr(self.model, "lm_head"):
            lm_head = self.model.lm_head
        elif hasattr(self.model, "embed_out"):  # NeoX
            lm_head = self.model.embed_out
        elif hasattr(self.model, "model") and hasattr(self.model.model, "transformer"):
            lm_head = self.model.model.transformer.ff_out  # OLMo
            self.tied_embeddings = False  # OLMo config uses own convention (weight_tying)
        elif hasattr(self.model, "output"):
            lm_head = self.model.output
            self.tied_embeddings = False
        else:
            raise AttributeError("Could not find the language modelling head in the model")

        self.output_embeddings = lm_head.weight.detach().numpy()
        self.output_embeddings_has_bias = (
            lm_head.bias is not None and np.linalg.norm(lm_head.bias.detach().numpy()) > 1e-3
        )
        if self.output_embeddings_has_bias:
            print(
                f"Unexpectedly found bias in the final layer, this is may reduce effectiveness of under-trainedness indicators in ways that is out of scope of this code, especially if tied_embeddings is True (it is {self.tied_embeddings}) or output embedding based indicators are needed otherwise."
            )
            self.output_embeddings_bias = lm_head.bias.detach().numpy()
        self.known_unused_tokens = [] if known_unused_tokens is None else known_unused_tokens
        self.calculate_unused_token_metric()

    # for plot labels and such
    INDICATOR_EOUT_CD_NAME = "E_{out} Cosine Distance"
    INDICATOR_EOUT_WO1PC_CD_NAME = "E_{out} Cosine Distance w/o 1st PC"
    INDICATOR_EOUT_CENTERED_CD_NAME = "E_{out} Cosine Distance Centered"
    INDICATOR_EOUT_L2DIST_NAME = "E_{out} L2 Distance"
    INDICATOR_EOUT_BIAS_NAME = "E_{out} Bias"
    INDICATOR_EIN_L2NORM_NAME = "E_{in} L2 Norm"

    def calculate_unused_token_metric(self):
        if len(self.known_unused_tokens) > 0:
            output_embedding_distances = embedding_distance_metrics(self.output_embeddings, self.known_unused_tokens)
            self.indicator_names = [
                self.INDICATOR_EOUT_CD_NAME,
                self.INDICATOR_EOUT_L2DIST_NAME,
            ]
            self.undertrained_token_indicators = np.stack(
                [
                    output_embedding_distances.cosine_distance,
                    output_embedding_distances.l2_distance,
                ],
                axis=-1,
            )
        elif self.tied_embeddings:
            raise ValueError("known_unused_tokens must be provided for tied embeddings")
        else:
            self.indicator_names = []
            self.undertrained_token_indicators = np.zeros((self.output_embeddings.shape[0], 0))  # make concat happy

        if self.output_embeddings_has_bias:
            self.indicator_names += [self.INDICATOR_EOUT_BIAS_NAME]
            self.undertrained_token_indicators = np.concatenate(
                [self.undertrained_token_indicators, self.output_embeddings_bias[:, np.newaxis]], axis=-1
            )

        if not self.tied_embeddings:  # prepend, so the first metric is the default
            l2_norm = np.linalg.norm(self.embeddings, axis=1)
            self.indicator_names = [self.INDICATOR_EIN_L2NORM_NAME] + self.indicator_names
            self.undertrained_token_indicators = np.concatenate(
                [l2_norm[:, np.newaxis], self.undertrained_token_indicators], axis=-1
            )

    def model_info(self):
        return {
            "model_info": {
                "Tied embeddings": self.tied_embeddings,
                "LM head uses bias": bool(self.output_embeddings_has_bias),  # avoid np.bool_
                "Embeddings shape": list(self.embeddings.shape),
            },
            "indicator_names": self.indicator_names,
        }
