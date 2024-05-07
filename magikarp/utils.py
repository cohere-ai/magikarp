import gzip
import itertools
import json
import os
import re
from collections import Counter, namedtuple
from typing import List

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


DistanceMetrics = namedtuple("Metrics", ["cosine_distance", "cosine_distance_without_first_pc", "l2_distance"])


def oov_distance_metrics(mat: np.ndarray, known_unused_tokens: List[int]) -> DistanceMetrics:
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

    pca = PCA(n_components=1)
    pca.fit(mat)
    first_pc = pca.components_[0]

    mat_without_first_pc = mat - np.outer(mat.dot(first_pc), first_pc)

    mean_unused_vector = mat[known_unused_tokens].mean(axis=0)
    mean_unused_vector_without_first_pc = mat_without_first_pc[known_unused_tokens].mean(axis=0)
    l2_distance = np.linalg.norm(mat - mean_unused_vector, axis=1)

    return DistanceMetrics(
        cosine_distance(mat, mean_unused_vector),
        cosine_distance(mat_without_first_pc, mean_unused_vector_without_first_pc),
        l2_distance,
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
