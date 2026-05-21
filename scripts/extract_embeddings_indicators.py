"""
Compute magikarp under-trainedness indicators by reading the token embedding
matrix directly from HuggingFace safetensors shards — no model load.

Useful when transformers/compressed-tensors can't load the model end-to-end
(see e.g. the W4A4 cohere2_vision packaging vs transformers main as of
2026-05-20). Pair this with `scripts/verify_via_vllm.py` to add the
generation-based verification step.

Only handles TIED-EMBEDDINGS models (lm_head shares weights with embed_tokens).
For non-tied models we'd also need the lm_head shard, which isn't always cleanly
extractable.
"""

import argparse
import json
import os
import sys
import time
from glob import glob

import numpy as np
import torch
from safetensors import safe_open

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from magikarp.fishing import classify_verification  # noqa: F401
from magikarp.model import ModelAnalyzer
from magikarp.report import make_tokens_report
from magikarp.tokenization import TokenizerAnalyzer
from magikarp.unused_tokens import UNUSED_TOKENS
from magikarp.utils import write_verification_results

sys.stdout.reconfigure(line_buffering=True)


def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


EMBED_KEY_CANDIDATES = (
    "model.embed_tokens.weight",
    "model.language_model.embed_tokens.weight",
    "transformer.wte.weight",
    "embed_tokens.weight",
    "gpt_neox.embed_in.weight",
)


def find_embedding_in_cache(model_id: str) -> tuple[str, str]:
    """Locate the shard and key for the token embedding in the HF cache."""
    repo_dir_name = "models--" + model_id.replace("/", "--")
    snap_root = os.path.expanduser(f"~/.cache/huggingface/hub/{repo_dir_name}/snapshots")
    snap_dirs = sorted(glob(f"{snap_root}/*"))
    if not snap_dirs:
        raise FileNotFoundError(f"No HF cache snapshots for {model_id}. Download first.")
    snap = snap_dirs[-1]

    index_path = os.path.join(snap, "model.safetensors.index.json")
    if os.path.exists(index_path):
        with open(index_path) as f:
            weight_map = json.load(f)["weight_map"]
        for key in EMBED_KEY_CANDIDATES:
            if key in weight_map:
                return os.path.join(snap, weight_map[key]), key
        for k, v in weight_map.items():
            if k.endswith("embed_tokens.weight"):
                return os.path.join(snap, v), k
        raise KeyError(f"Couldn't find an embed_tokens key in {index_path}")

    single = os.path.join(snap, "model.safetensors")
    if os.path.exists(single):
        with safe_open(single, framework="pt", device="cpu") as f:
            keys = set(f.keys())
        for key in EMBED_KEY_CANDIDATES:
            if key in keys:
                return single, key
        for k in keys:
            if k.endswith("embed_tokens.weight"):
                return single, k
    raise FileNotFoundError(f"No safetensors found in {snap}")


def load_embedding_tensor(shard: str, key: str) -> np.ndarray:
    log(f"Reading {key} from {os.path.basename(shard)}")
    with safe_open(shard, framework="pt", device="cpu") as f:
        emb = f.get_tensor(key)
    log(f"  shape={tuple(emb.shape)} dtype={emb.dtype}")
    return emb.float().numpy()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model_id", required=True)
    ap.add_argument("--shard", help="Path to safetensors shard containing embed_tokens (auto-detected by default)")
    ap.add_argument("--key", help="State-dict key for the embedding tensor (auto-detected by default)")
    ap.add_argument("--threshold_ratio", type=float, default=2.0)
    ap.add_argument("--skip_report", action="store_true")
    args = ap.parse_args()

    shard, key = args.shard, args.key
    if not (shard and key):
        shard, key = find_embedding_in_cache(args.model_id)

    embeddings_np = load_embedding_tensor(shard, key)

    log("Loading tokenizer / categorizing vocab")
    toka = TokenizerAnalyzer(args.model_id)
    token_infos = toka.categorize_tokens()

    if args.model_id not in UNUSED_TOKENS:
        raise SystemExit(
            f"{args.model_id} not in UNUSED_TOKENS — add a registry entry to magikarp/unused_tokens.py first"
        )
    known_unused_tokens = list(UNUSED_TOKENS[args.model_id])

    log("Building ModelAnalyzer in embeddings-only mode (tied)")
    moda = ModelAnalyzer.__new__(ModelAnalyzer)
    moda.model = None
    moda.embeddings = embeddings_np
    moda.output_embeddings = embeddings_np
    moda.tied_embeddings = True
    moda.output_embeddings_has_bias = False
    moda.known_unused_tokens = known_unused_tokens
    moda.calculate_unused_token_metric()
    log(f"  indicators: {moda.indicator_names}")

    indicator_ix = 0
    for token_id, indicators in enumerate(moda.undertrained_token_indicators):
        if token_id in token_infos:
            token_infos[token_id]["indicators"] = [float(x) for x in indicators]
        if token_id == 0:
            token_infos[token_id].update(moda.model_info())
    for ti in token_infos.values():
        if "indicators" in ti:
            ti["main_indicator"] = ti["indicators"][indicator_ix]

    out = write_verification_results(token_infos, args.model_id)
    log(f"Wrote indicator-only results to {out}(.gz)")

    if not args.skip_report:
        log("Generating report (verification field absent → no generation tests)")
        make_tokens_report(args.model_id, toka, moda, token_infos, indicator_ix, threshold_ratio=args.threshold_ratio)


if __name__ == "__main__":
    main()
