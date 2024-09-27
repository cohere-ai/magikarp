import gzip
import itertools
import json
import os
import re
from collections import Counter, namedtuple
from typing import List, Union
import numpy as np
from sklearn.decomposition import PCA


# --- results saving/loading utils ---


def output_name(model_id, tag, extension):
    model_id_alphanum = re.sub(r"[^a-zA-Z0-9]", "_", model_id)
    filename = f"results/{tag}/{model_id_alphanum}.{extension}"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    return filename


def write_verification_results(token_infos, model_id, compress=True) -> str:
    output_file = output_name(model_id, "verifications", "jsonl")
    open_fn_with_formats = [(open, "")]
    if compress:  # write both compressed and uncompressed versions, with uncompressed never committed
        open_fn_with_formats.append((gzip.open, ".gz"))
    for open_func, gzext in open_fn_with_formats:
        with open_func(output_file + gzext, "wt") as f:
            for _, token_info in sorted(token_infos.items()):
                print(json.dumps(token_info), file=f)

    return output_file


def load_verification_results(model_id):
    for open_fn, ext in [(open, ""), (gzip.open, ".gz")]:
        try:
            with open_fn(output_name(model_id, "verifications", "jsonl" + ext), "r") as f:
                return {token_info["i"]: token_info for token_info in [json.loads(line) for line in f]}
        except FileNotFoundError:
            pass
    return None


# --- distance metric utils ---


def cosine_distance(mat: np.ndarray, v: np.ndarray) -> float:
    """
    Calculate the cosine distance between a matrix and a vector.

    Args:
        mat: The matrix of shape (n, m).
        v: The vector of shape (m,).

    Returns:
        The cosine distances between the each row in the matrix and the vector.
    """
    # clip here mainly needed if rows of mat are 0, e.g. in Phi-3
    return 1 - np.dot(mat, v) / (np.linalg.norm(mat, axis=1) * np.linalg.norm(v)).clip(min=1e-6)


DistanceMetrics = namedtuple(
    "indicators", ["cosine_distance", "cosine_distance_without_first_pc", "cosine_distance_without_mean", "l2_distance"]
)


def embedding_distance_metrics(mat: np.ndarray, known_unused_tokens: List[int]) -> DistanceMetrics:
    """
    Calculate the distance metrics for out-of-vocabulary (OOV) tokens.

    Args:
        mat: The matrix of shape (n, m) representing the embeddings.
        known_unused_tokens: A list of token indices that are known to be unused.

    Returns:
        A named tuple containing the cosine distance metrics:
        - cosine_distance: The cosine distance between the embeddings and the mean unused vector.
        - cosine_distance_without_first_pc: The cosine distance between the embeddings and the mean unused vector without the first principal component.
        - l2_distance: The L2 distance between the embeddings and the mean unused vector.
    """
    assert mat.shape[0] > mat.shape[1], "Expected more tokens than dimensions"

    mean_unused_vector = mat[known_unused_tokens].mean(axis=0)
    l2_distance = np.linalg.norm(mat - mean_unused_vector, axis=1)

    mean_row = mat.mean(axis=0)
    mat_without_mean = mat - mean_row
    mean_unused_vector_without_matmean = mat_without_mean[known_unused_tokens].mean(axis=0)

    n_comp = 1
    pca = PCA(n_components=n_comp)
    pca.fit(mat)
    mat_without_first_pc = mat
    for i in range(n_comp):
        pca_component = pca.components_[i]
        mat_without_first_pc = mat_without_first_pc - np.outer(mat_without_first_pc.dot(pca_component), pca_component)
    mean_unused_vector_without_first_pc = mat_without_first_pc[known_unused_tokens].mean(axis=0)

    return DistanceMetrics(
        cosine_distance=cosine_distance(mat, mean_unused_vector),
        cosine_distance_without_first_pc=cosine_distance(mat_without_first_pc, mean_unused_vector_without_first_pc),
        cosine_distance_without_mean=cosine_distance(mat_without_mean, mean_unused_vector_without_matmean),
        l2_distance=l2_distance,
    )


# --- misc


def format_ranges(ixs: list[int]) -> str:
    sixs = sorted(set(ixs))
    ranges = []
    for k, g in itertools.groupby(enumerate(sixs), lambda x: x[0] - x[1]):
        g = list(g)
        if len(g) == 1:
            ranges.append(f"{g[0][1]}")
        else:
            ranges.append(f"{g[0][1]}-{g[-1][1]}")
    s = ", ".join(ranges)
    c = Counter(ixs)
    for d in range(2, 5):
        ddups = {k: v for k, v in c.items() if v == d}
        if ddups:
            ds = ",".join(str(s) for s in sorted(ddups.keys()))
            s += f" - 2x {len(ddups)} items: {ds}"
    return s


# -- fishing utils, shared between report and fishing so moved here
DEFAULT_THRESHOLD_PERCENTILE = 2.0


def candidates_for_verification(
    token_infos, threshold_ratio: Union[float, None] = DEFAULT_THRESHOLD_PERCENTILE, threshold=None
):
    if threshold is None:
        threshold = np.percentile(
            [tc["main_indicator"] for tc in token_infos.values() if tc["category"] == "OK"],
            threshold_ratio,
        )
        print(
            f"Using threshold {threshold:.3f} as {threshold_ratio:.1f}% of tokens to verify with vocab size {len(token_infos)}."
        )
    candidates = sorted(
        [tc for tc in token_infos.values() if tc["main_indicator"] <= threshold and tc["category"].startswith("OK")],
        key=lambda tc: tc["main_indicator"],
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


# -- report
from transformers.utils import cached_file
from transformers.tokenization_utils_base import TOKENIZER_CONFIG_FILE, FULL_TOKENIZER_FILE
from transformers.models.auto.tokenization_auto import get_tokenizer_config


def escape_token_for_markdown(token, code_tags=True):
    token = repr(token)[1:-1]  # escape \n, unicode, etc
    token = token.replace(" ", "▁")  # make spaces show clearly
    token = token.replace("\\\\", "\\")  # un-escape \
    token = token.replace("|", r"\|")  # breaks tables
    if code_tags:
        token = f"````` {token} `````"  # more ` such that even ```` in tokens doesn't break markdown
    return token


def find_byte_tokens(toka: "TokenizerAnalyzer", token_infos: dict[int, dict]) -> dict[int, dict]:
    """Find tokens that are single byte characters, ascii 0-127 plus byte fallback"""
    single_byte_vocab = {i: ti for i, ti in token_infos.items() if toka.token_byte_value(i) is not None}
    for i, ti in single_byte_vocab.items():
        ti["ord"] = toka.token_byte_value(i)
        ti["hex"] = "0x%02X" % ti["ord"]
        if ti["ord"] < 128:
            ti["byte_type"] = "ascii"
        elif ti["ord"] >= 245 or ti["ord"] in [0xC0, 0xC1]:
            ti["byte_type"] = "unused_utf8"
        else:
            ti["byte_type"] = "utf8"
    return single_byte_vocab


def find_special_tokens(token_infos: dict[int, dict]) -> dict[int, dict]:
    """Find tokens that are special tokens."""
    special_tokens = {
        i: ti
        for i, ti in token_infos.items()
        if len(ti["raw_vocab"]) >= 3
        and ti["raw_vocab"][0] in "[<"
        and ti["raw_vocab"][-1] in "]>"
        and any(c.isalpha() and ord(c) < 128 for c in ti["raw_vocab"])
        and not ti["raw_vocab"].startswith("<0x")
    }
    return special_tokens


VerificationResult = namedtuple(
    "VerificationResult",
    ["bytes", "specials", "candidates", "threshold", "candidates_nosb", "unreachables", "partial_utf8"],
)


def get_verified_candidates(toka, token_infos):
    verification_candidates, verification_cand_threshold = candidates_for_verification(token_infos)
    if not all("max_prob" in c for c in verification_candidates):
        n_total = len(verification_candidates)
        verification_candidates = [c for c in verification_candidates if "max_prob" in c]
        print(
            f"❗ WARNING: verification step not completed for {toka.model_id}, loaded {len(verification_candidates)} out of {n_total} candidates"
        )
    return verification_candidates, verification_cand_threshold


def categorize_token_infos(toka, token_infos):
    verification_candidates, verification_cand_threshold = get_verified_candidates(toka, token_infos)
    for t in verification_candidates:
        t["readable_vocab"] = toka.vocab_to_readable_string(t["i"])
    single_byte_vocab = find_byte_tokens(toka, token_infos)
    special_token_vocab = find_special_tokens(token_infos)
    exclude = set(single_byte_vocab.keys()) | set(special_token_vocab.keys())
    candidates_without_excl = [ti for ti in verification_candidates if ti["i"] not in exclude]
    unreachable_without_excl = [
        ti for ti in token_infos.values() if "UNREACHABLE" in ti["category"] and ti["i"] not in exclude
    ]
    partial_utf8_without_excl = [
        ti for ti in token_infos.values() if "UNDECODEABLE" in ti["category"] and ti["i"] not in exclude
    ]
    return VerificationResult(
        bytes=single_byte_vocab,
        specials=special_token_vocab,
        candidates=verification_candidates,
        threshold=verification_cand_threshold,
        candidates_nosb=candidates_without_excl,
        unreachables=unreachable_without_excl,
        partial_utf8=partial_utf8_without_excl,
    )


# -- huggingface token info


def get_tokenizer_definition(model_id):
    try:
        with open(cached_file(model_id, FULL_TOKENIZER_FILE), encoding="utf-8") as reader:
            return json.load(reader)
    except Exception:  # does not exist
        return None


def get_huggingface_tokenizer_info(model_id, toka, token_infos):
    tokenizer_info: dict[str, str | int] = {"Vocab Size": len(token_infos)}
    tokenizer_json = get_tokenizer_definition(model_id)

    tokenizer_config = get_tokenizer_config(model_id)

    if tokenizer_class := tokenizer_config.get("tokenizer_class"):
        tokenizer_info["Tokenizer Class"] = tokenizer_class
    else:
        tokenizer_info["Tokenizer Class"] = toka.tokenizer.__class__.__name__

    if tokenizer_json:
        if tokenizer_type := tokenizer_json["model"].get("type"):
            tokenizer_info["Tokenizer Type"] = tokenizer_type

        # get pretokenizer info for byte level
        pretokenizer = tokenizer_json["pre_tokenizer"]
        if pretokenizer:
            pretokenizers = pretokenizer["pretokenizers"] if pretokenizer["type"] == "Sequence" else [pretokenizer]
            byte_level = any(pretokenizer["type"] == "ByteLevel" for pretokenizer in pretokenizers)
        else:
            byte_level = None

        # byte_fallback: check model, then decoder as alternative
        byte_fallback = tokenizer_json["model"].get("byte_fallback")
        decoder = tokenizer_json.get("decoder")
        if decoder and byte_fallback is None:
            decoders = decoder["decoders"] if decoder["type"] == "Sequence" else [decoder]
            byte_fallback = any(decoder["type"] == "ByteFallback" for decoder in decoders)

        if byte_level:
            tokenizer_info["Bytes handling"] = "Byte Input"
            assert not byte_fallback, "Both byte_level and byte_fallback are set"
        elif byte_fallback:
            tokenizer_info["Bytes handling"] = "Byte Fallback"

        dropout = tokenizer_json["model"].get("dropout")
        if dropout is not None:
            tokenizer_info["Dropout"] = dropout

    # patch up some blanks which fail the above detection
    if (
        any(s in model_id for s in ["/gpt2", "/miqu", "/neo_7b", "/Skywork", "/Yi-Coder", "/internlm"])
        and "Tokenizer Type" not in tokenizer_info
    ):
        tokenizer_info["Tokenizer Type"] = "BPE"
    if any(s in model_id for s in ["/miqu"]) and "Bytes handling" not in tokenizer_info:
        tokenizer_info["Bytes handling"] = "Byte Fallback"  # just llama2
    if any(s in model_id for s in ["/neo_7b"]) and "Bytes handling" not in tokenizer_info:
        tokenizer_info["Bytes handling"] = "Byte Input"  # according to comments in source

    return tokenizer_info


# --- combined


def get_model_and_tokenizer_info(model_id, toka, token_infos):
    """Collects a bunch of info about the model and tokenizer"""

    model_info = token_infos[0].get("model_info") or {}
    tokenizer_info = get_huggingface_tokenizer_info(model_id, toka, token_infos)

    # include id for distinguishing coincidental identical ones
    placeholder = select_placeholder_token(toka, token_infos)
    tokenizer_info["Token for verification prompt building"] = toka.vocab_to_readable_string(placeholder["i"])
    tokenizer_info["Token id for verification prompt building"] = placeholder["i"]

    return {"Model Info": model_info, "Tokenizer Info": tokenizer_info}


def dict_to_markdown_list(d, indent=0, bold=False):
    """Converts a dictionary to a nested Markdown list."""
    markdown = ""
    for key, value in d.items():
        fmt = "**" if bold else ""
        markdown += "  " * indent + f"* {fmt}{key}{fmt}: "
        if isinstance(value, dict):
            markdown += "\n" + dict_to_markdown_list(value, indent + 1, bold)
        else:
            markdown += f"{value}\n"
    return markdown
