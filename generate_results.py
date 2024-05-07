# This script generates reports and visualizations
# Use: python generate_results.py [optional_filter] [--load]
# Where
# * --load gives you a few extra bits of information but loads the model
# * optional_filter is a string that is used to filter the models to process, without it all models are processed
import sys
import traceback

import matplotlib.pyplot as plt

from magikarp.fishing import UNUSED_TOKENS, candidates_for_verification, load_analyzers
from magikarp.report import hardcoded_metrics_ix, make_tokens_report, verification_plot
from magikarp.unused_tokens import UNUSED_TOKENS

avoid_loading_model = not any("--load" in v for v in sys.argv)
save_hires = any("--poster" in v for v in sys.argv)
all_tokens_plot = any("--all_tokens_plot" in v for v in sys.argv)
trust_remote = any("--trust" in v for v in sys.argv)
filter = sys.argv[1].split("|") if len(sys.argv) > 1 else ""

for model_id in UNUSED_TOKENS.keys():
    if filter and not any(s in model_id for s in filter):
        continue
    trust_remote_code = "Phi-3" in model_id or trust_remote
    metric_ix = hardcoded_metrics_ix(model_id)

    print(
        f"🛠️  Processing {model_id} (metric ix={metric_ix}) "
        + ("from cache" if avoid_loading_model else "by loading")
        + (" with hi res figures" if save_hires else "")
    )
    try:
        plt.close()
        toka, moda, token_infos = load_analyzers(
            model_id, avoid_loading_model=avoid_loading_model, trust_remote_code=trust_remote_code, metric_ix=metric_ix
        )
        make_tokens_report(model_id, toka, moda, token_infos, metric_ix, save_hires=save_hires)
        if (
            all_tokens_plot
        ):  # additional plot for all verified tokens (usually, all tokens allowed in inputs) for a particular model
            verification_candidates, _ = candidates_for_verification(token_infos, threshold_ratio=100)
            if not all("max_prob" in c for c in verification_candidates):
                n_total = len(verification_candidates)
                verification_candidates = [c for c in verification_candidates if "max_prob" in c]
                print(
                    f"❗ WARNING: verification step not completed, loaded {len(verification_candidates)} out of {n_total} candidates"
                )
            _, verification_filename = verification_plot(
                model_id,
                verification_candidates,
                token_infos[0]["metric_names"][metric_ix],
                save_dir="paper_plots",
                save_hires=save_hires,
            )
    except Exception as e:
        print(f"❌  Error processing {model_id}: {e}")
        traceback.print_exc()
        continue
