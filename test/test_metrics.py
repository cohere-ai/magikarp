import numpy as np

from magikarp.utils import embedding_distance_metrics


def test_emb_distance_metrics():
    mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    known_unused_tokens = [1, 2]
    metrics = embedding_distance_metrics(mat, known_unused_tokens)
    for k, v in metrics._asdict().items():
        assert v is not None
