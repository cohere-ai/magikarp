"""
Run magikarp verification by hitting a local vLLM /v1/completions endpoint.

Use this when transformers can't load the model via AutoModelForCausalLM but
vLLM can (e.g. quantized MoE checkpoints, models whose packaging predates a
transformers refactor). Indicators must already be cached in
results/verifications/<model>.jsonl(.gz) — run fishing.py (or, if model load
fails too, scripts/extract_embeddings_indicators.py) first.

Start the vLLM server separately, e.g.:
    vllm serve <model_id> -tp 2 --port 8765 --host 127.0.0.1 --max-model-len 4096
"""

import argparse
import json
import math
import os
import sys
import time
from typing import Any

import numpy as np
import requests

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from magikarp.fishing import VERIFICATION_PROMPTS, classify_verification
from magikarp.tokenization import TokenizerAnalyzer
from magikarp.unused_tokens import UNUSED_TOKENS
from magikarp.utils import (
    DEFAULT_THRESHOLD_PERCENTILE,
    candidates_for_verification,
    load_verification_results,
    select_placeholder_token,
    write_verification_results,
)

VLLM_TOPK = 20  # vLLM caps logprobs at 20 by default


def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


def vllm_complete(base_url: str, model: str, prompt_token_ids, max_tokens: int, logprobs: int):
    r = requests.post(
        f"{base_url.rstrip('/')}/v1/completions",
        json={
            "model": model,
            "prompt": prompt_token_ids,
            "max_tokens": max_tokens,
            "temperature": 0.0,
            "top_p": 1.0,
            "logprobs": logprobs,
            "n": 1,
            "stream": False,
        },
        timeout=120,
    )
    r.raise_for_status()
    return r.json()


def prob_of_token_id(resp: dict, token_id: int, tokenizer) -> tuple[list[float], list[str]]:
    """Given a /v1/completions response, return per-position prob of token_id and the generated string."""
    ch = resp["choices"][0]
    out_text = ch["text"]
    lp = ch.get("logprobs", {})
    top_logprobs = lp.get("top_logprobs") or []
    # top_logprobs is a list (one per generated position) of dicts: {token_string: logprob}
    # vLLM's openai-compat returns strings, not ids. We must map id -> string the same way vLLM does.
    target_str = tokenizer.decode([token_id])
    target_repr_variants = {target_str, target_str.lstrip(), target_str.strip()}
    probs = []
    for pos_logprobs in top_logprobs:
        best = 0.0
        for tok_str, logp in pos_logprobs.items():
            if tok_str in target_repr_variants or tok_str == target_str:
                p = math.exp(logp)
                if p > best:
                    best = p
        probs.append(best)
    return probs, out_text


def verify_one_token(
    toka: TokenizerAnalyzer,
    token_info: dict,
    build_prompt_token: dict,
    base_url: str,
    model: str,
    n_tokens: int = 3,
) -> list[dict]:
    token_id = token_info["i"]
    results: list[dict] = []
    for test_name, n, preamble, input_phrase, completion in VERIFICATION_PROMPTS:
        example_id = build_prompt_token["i"]
        nshot = preamble + (input_phrase + completion) * n + input_phrase + completion[: completion.index("{")]
        nshot = nshot.format(token=build_prompt_token["decoded"])
        ids = toka.tokenizer.encode(nshot)
        n_subs = sum(1 for t in ids if t == example_id)
        assert n_subs == 2 * n + 1, f"Prompt building broken: expected {2*n+1} substitutions, got {n_subs}"
        ids = [token_id if t == example_id else t for t in ids]
        decoded_subst_prompt = toka.tokenizer.decode(ids)
        encodeable = token_id in toka.tokenizer.encode(decoded_subst_prompt)

        try:
            resp = vllm_complete(base_url, model, ids, max_tokens=n_tokens, logprobs=VLLM_TOPK)
            probs, out_text = prob_of_token_id(resp, token_id, toka.tokenizer)
            max_prob = max(probs, default=0.0)
        except Exception as e:
            out_text = f"<<vLLM error: {e}>>"
            max_prob = float("nan")
        results.append(
            dict(test_name=test_name, encodeable=encodeable, output=out_text, max_prob=max_prob)
        )
    return results


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model_id", required=True)
    ap.add_argument("--base_url", default="http://127.0.0.1:8765")
    ap.add_argument("--threshold_ratio", type=float, default=DEFAULT_THRESHOLD_PERCENTILE)
    ap.add_argument("--limit", type=int, default=None, help="cap number of candidates to verify")
    ap.add_argument("--overwrite", action="store_true", help="re-verify already-done tokens")
    args = ap.parse_args()

    log(f"Loading tokenizer + cached indicators for {args.model_id}")
    toka = TokenizerAnalyzer(args.model_id)
    token_infos = toka.categorize_tokens()
    cached = load_verification_results(args.model_id) or {}
    for tid, ti in cached.items():
        if tid in token_infos:
            keys = {"indicators", "indicator_names", "verification", "model_info",
                    "main_indicator", "max_prob", "magikarp"} & set(ti.keys())
            for k in keys:
                token_infos[tid][k] = ti[k]
    if not any("main_indicator" in ti for ti in token_infos.values()):
        log("ERROR: no indicators in cache — run indicator extraction first.")
        sys.exit(1)

    candidates, threshold = candidates_for_verification(token_infos, threshold_ratio=args.threshold_ratio)
    log(f"{len(candidates)} candidates below threshold {threshold:.4f}")
    remaining = [
        c for c in candidates
        if args.overwrite or "verification" not in c
    ]
    if args.limit is not None:
        remaining = remaining[: args.limit]
    log(f"{len(remaining)} to verify (overwrite={args.overwrite}, limit={args.limit})")

    # Probe server
    log(f"Probing {args.base_url}")
    r = requests.get(f"{args.base_url.rstrip('/')}/v1/models", timeout=10)
    r.raise_for_status()
    served = [m["id"] for m in r.json().get("data", [])]
    log(f"  served models: {served}")
    if args.model_id not in served:
        log(f"WARN: {args.model_id} not in served list, using first ({served[0]})")
    served_model = served[0] if served else args.model_id

    build_prompt_token = select_placeholder_token(toka, token_infos)
    log(f"Placeholder token: id={build_prompt_token['i']} {build_prompt_token['decoded']!r}")

    t0 = time.perf_counter()
    for ii, ti in enumerate(remaining):
        ti["verification"] = verify_one_token(
            toka, ti, build_prompt_token, args.base_url, served_model
        )
        mp = classify_verification(ti)
        log(
            f"[{time.perf_counter()-t0:.0f}s {ii+1}/{len(remaining)}] {ti['magikarp']:<28} "
            f"max_prob={mp:.2e} id={ti['i']} raw={ti.get('raw_vocab','')!r}"
        )
        if (ii + 1) % 25 == 0:
            write_verification_results(token_infos, args.model_id)

    out = write_verification_results(token_infos, args.model_id)
    log(f"Wrote results to {out}(.gz)")


if __name__ == "__main__":
    main()
