import time
from typing import Optional

import fire
import numpy as np
import torch

from magikarp.model import ModelAnalyzer
from magikarp.tokenization import TokenizerAnalyzer, model_needs_fast_tokenizer
from magikarp.unused_tokens import UNUSED_TOKENS
from magikarp.utils import load_verification_results, write_verification_results

DEFAULT_THRESHOLD_PERCENTILE = 2.0
VERIFICATION_PROMPTS = [
    (
        "input_output",
        20,
        "This device repeats its input exactly, as shown in these 100 identical trials.",
        "\nInput: «{token}»\nOutput:",
        " «{token}»",
    ),
    (
        "assistant_explain",
        0,
        "This helpful assistant explains what a phrase means, replying with identical responses to identical questions for reliability.",
        "\nUser: What does 'edslfkj' mean?\nAssistant: 'edslfkj' has no specific meaning I am aware of.\nUser: what does '{token}' mean?\nAssistant:",
        " '{token}'",
    ),
    (
        "repeats",
        50,
        "Below is the output, as you can see it's just giving the same phrase repeated indefinitely:\n",
        "{token}",
        "{token}",
    ),
]


def verify_magikarp(
    toka: TokenizerAnalyzer,
    moda: ModelAnalyzer,
    token_info: dict,
    build_prompt_token: dict,
    n_tokens: int = 3,
) -> tuple[list[dict], list[torch.Tensor]]:
    def raw_logits_to_prob_i(raw_logits: torch.Tensor, token_ix: int):
        raw_logits = raw_logits.detach()
        logits = torch.nn.functional.log_softmax(raw_logits, dim=-1)
        return np.exp(logits[0, token_ix].item())

    token_id = token_info["i"]
    verification_results = []
    raw_logits = []
    for test_name, n, preamble, input_phrase, completion in VERIFICATION_PROMPTS:
        example_id = build_prompt_token["i"]
        nshot = preamble + (input_phrase + completion) * n + input_phrase + completion[: completion.index("{")]
        nshot = nshot.format(token=build_prompt_token["decoded"])
        tokens: torch.Tensor = toka.tokenizer.encode(nshot, return_tensors="pt")  # type: ignore
        assert (tokens == build_prompt_token["i"]).sum().item() == 2 * n + 1, "Prompt building not working as expected"
        sub_id = token_id
        tokens[tokens == example_id] = sub_id

        decoded_subst_prompt = toka.tokenizer.decode(tokens[0])
        encodeable = token_id in toka.tokenizer.encode(decoded_subst_prompt)

        gen_tokens = moda.model.generate(
            tokens.to(moda.model.device),
            max_new_tokens=n_tokens,
            do_sample=True,
            top_k=1,
            return_dict_in_generate=True,
            output_logits=True,
            pad_token_id=toka.tokenizer.pad_token_id,
        )
        generated_tokens = gen_tokens["sequences"][0, tokens.shape[1] :].cpu().numpy()
        try:
            gen_str = toka.tokenizer.decode(generated_tokens)
        except Exception as e:
            gen_str = f"<<Error: {e}>>"
        logits = gen_tokens["logits"]
        token_probs = [raw_logits_to_prob_i(l.cpu(), sub_id) for l in logits]  # tuple of up to n_tokens
        max_prob = max(token_probs, default=np.nan)

        verification_results.append(
            dict(
                test_name=test_name,
                encodeable=encodeable,
                output=gen_str,
                max_prob=max_prob,
            )
        )
        raw_logits.append(logits)
    return verification_results, raw_logits


def classify_verification(token_info: dict) -> float:
    """Classify a token based on its verification results."""
    token_info["max_prob"] = np.max([vr["max_prob"] for vr in token_info["verification"]])
    # encodeable
    if token_info["max_prob"] > 0.9:
        token_info["magikarp"] = "strong_rejected"
    elif token_info["max_prob"] > 0.1:
        token_info["magikarp"] = "weak_rejected"
    elif all(not vr["encodeable"] for vr in token_info["verification"]):
        token_info["magikarp"] = "verification_encoding_failed"
    elif token_info["max_prob"] < 0.001:
        token_info["magikarp"] = "strong_verified"
    else:  # 0.1-0.001
        token_info["magikarp"] = "weak_verified"
    return token_info["max_prob"]


def load_analyzers(
    model_id: str,
    avoid_loading_model: bool = True,
    known_unused_tokens: Optional[list[int]] = None,
    load_verifications: bool = True,
    use_fast: Optional[bool] = None,
    trust_remote_code: bool = False,
    metric_ix: int = 0,
) -> tuple[TokenizerAnalyzer, Optional[ModelAnalyzer], dict]:
    toka = TokenizerAnalyzer(model_id, use_fast=use_fast, trust_remote_code=trust_remote_code)

    if known_unused_tokens is None:
        known_unused_tokens = UNUSED_TOKENS.get(model_id, [])
    token_infos = toka.categorize_tokens()

    loaded_results = load_verification_results(model_id)
    if avoid_loading_model and not loaded_results:
        print(
            f"Warning: Avoid_loading_model is set, but no stored results found for {model_id!r} so we will load the model anyway."
        )
        avoid_loading_model = False

    if load_verifications and loaded_results:
        for token_id, res in loaded_results.items():
            # ONLY load verification and maybe metrics, the rest was saved just for debugging
            for k in {"metrics", "metric_names", "verification"} & set(res.keys()):
                token_infos[token_id][k] = res[k]  # overwritten if not avoid_loading_model
            if "verification" in token_infos[token_id]:
                classify_verification(token_infos[token_id])

    if not avoid_loading_model:  # by default we don't trust saved results for easy experimentation
        moda = ModelAnalyzer(
            model_id,
            known_unused_tokens=known_unused_tokens,
            vocab_size_lb=len(toka.vocab_i2s),
            trust_remote_code=trust_remote_code,
        )
        for token_id, metrics in enumerate(moda.undertrained_token_metrics):
            if token_id in token_infos:
                token_infos[token_id]["metrics"] = [float(x) for x in metrics]  # json friendly
            if token_id == 0:  # a bit of a hack but eh
                token_infos[token_id]["metric_names"] = moda.metric_names
    else:
        moda = None

    for i, ti in token_infos.items():
        ti["main_metric"] = ti["metrics"][metric_ix]

    return toka, moda, token_infos


def candidates_for_verification(token_infos, threshold_ratio=DEFAULT_THRESHOLD_PERCENTILE, threshold=None):
    if threshold is None:
        threshold = np.percentile(
            [tc["main_metric"] for tc in token_infos.values() if tc["category"] == "OK"],
            threshold_ratio,
        )
        print(
            f"Using threshold {threshold:.3f} as {threshold_ratio:.1f}% of tokens to verify with vocab size {len(token_infos)}."
        )
    candidates = sorted(
        [tc for tc in token_infos.values() if tc["main_metric"] <= threshold and tc["category"].startswith("OK")],
        key=lambda tc: tc["main_metric"],
    )
    return candidates, threshold


def select_placeholder_token(toka, token_infos: dict) -> dict:
    # we use a long non-repetitive alphabetical token as a placeholder in building prompts for the verification
    build_prompt_tokens = sorted(
        token_infos.values(),
        key=lambda tc: (
            tc["category"] == "OK",
            tc["decoded"].isalpha(),
            len(set(tc["decoded"])),
            len(tc["decoded"]),
        ),
        reverse=True,
    )
    for build_prompt_token in build_prompt_tokens:
        two_repeats = [build_prompt_token["i"], build_prompt_token["i"]]
        s = toka.clean_decode(two_repeats)
        if toka.clean_encode(s) != two_repeats:
            print(
                f"Skipping token #{build_prompt_token['i']} {build_prompt_token['decoded']!r} as placeholder in building verification prompts due to encoding issues."
            )
        else:
            break
    print(
        f"Using token #{build_prompt_token['i']} {build_prompt_token['decoded']!r} as placeholder in building verification prompts."
    )
    return build_prompt_token


def main(
    model_id: str,
    trust_remote_code=False,
    threshold: Optional[float] = None,
    threshold_ratio: float = DEFAULT_THRESHOLD_PERCENTILE,  # % of tokens to verify
    known_unused_tokens: Optional[list[int]] = None,
    overwrite: bool = False,
    metric_ix: int = 0,  # index of metric to use, default is nearly always ok, use visualize_metrics.ipynb to check
    device: str = "cpu",
):
    known_unused_tokens = known_unused_tokens or UNUSED_TOKENS.get(model_id, [])
    toka, moda, token_infos = load_analyzers(
        model_id,
        avoid_loading_model=False,
        known_unused_tokens=known_unused_tokens,
        load_verifications=not overwrite,
        trust_remote_code=trust_remote_code,
        metric_ix=metric_ix,
    )
    assert moda is not None  # for type checker

    candidates, threshold = candidates_for_verification(
        token_infos, threshold_ratio=threshold_ratio, threshold=threshold
    )
    remaining_candidates = [tc for tc in candidates if "verification" not in tc]
    write_verification_results(token_infos, model_id)
    print(
        f"Verifying {len(remaining_candidates)} of total {len(candidates)} candidates below threshold {threshold:.3f} of {moda.metric_names[metric_ix]!r} for model {model_id} with vocab size {len(token_infos)} on device {device}."
    )

    build_prompt_token = select_placeholder_token(toka, token_infos)

    moda.model.to(device)
    t0 = time.perf_counter()
    for ii, token_info in enumerate(remaining_candidates):
        token_info["verification"], _ = verify_magikarp(toka, moda, token_info, build_prompt_token)
        max_prob = classify_verification(token_info)
        print(
            f"[{time.perf_counter()-t0:.0f}s, {ii+1}/{len(remaining_candidates)}] {token_info['magikarp']} with max_prob = {max_prob:.2e} token {token_info['i']}: {toka.vocab_to_readable_string(token_info['i'])!r} verification info: {token_info['verification']}"
        )
        if ii % 10 == 0:
            write_verification_results(token_infos, model_id)
    print(
        "Finished verification, wrote results to",
        write_verification_results(token_infos, model_id),
    )


if __name__ == "__main__":
    fire.Fire(main)
