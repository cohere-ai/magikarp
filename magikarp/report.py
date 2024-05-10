# functions for creating visualizations and reports
from typing import Iterable, Optional, Union

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import tabulate

from magikarp.fishing import candidates_for_verification, select_placeholder_token
from magikarp.tokenization import TokenizerAnalyzer
from magikarp.utils import output_name


def hardcoded_metrics_ix(model_id):  # yes this is bad
    metric_ix = 1 if "OLMo" in model_id else 0
    return metric_ix


def get_metrics(moda, token_infos):
    if moda is None:
        metric_names = token_infos[0]["metric_names"]
        undertrained_token_metrics = np.array([token_info["metrics"] for token_info in token_infos.values()])
    else:
        metric_names = moda.metric_names
        undertrained_token_metrics = moda.undertrained_token_metrics
    return metric_names, undertrained_token_metrics


# ---- plots ----
def set_plot_style(font_scale=0.8):
    sns.set_context("paper")
    sns.set_theme(style="whitegrid", font_scale=font_scale)
    sns.set_style("whitegrid", {"grid.color": ".95", "grid.linestyle": "--"})
    plt.clf()


def metrics_pairplot(
    token_infos,
    toka,
    moda=None,
    color_by_id=False,
    fig_width=10,
    aspect_ratio=0.8,
    markersize=8,
    save=True,
    save_hires=False,
):
    metric_names, undertrained_token_metrics = get_metrics(moda, token_infos)

    metric_df = pd.DataFrame({k: v for k, v in zip(metric_names, undertrained_token_metrics.T)})

    set_plot_style()
    plot_kws = {"s": markersize}
    diag_kws = {"bins": 100}
    kws = {}
    if color_by_id:
        p = sns.color_palette("crest", as_cmap=True)
        nt = undertrained_token_metrics.shape[0]
        plot_kws["c"] = [p(i / nt) for i in range(nt)]
    g = sns.pairplot(
        metric_df.fillna(0),
        markers=".",
        diag_kind="hist",
        plot_kws=plot_kws,
        diag_kws=diag_kws,
        **kws,
    )
    g.figure.set_size_inches(fig_width, fig_width * aspect_ratio)
    plt.tight_layout()
    filename = output_name(toka.model_id, "metrics_pairplot" + ("_byid" if color_by_id else ""), "png")
    if save:
        plt.savefig(filename, dpi=300)  # , bbox_inches="tight")
        if save_hires:
            plt.savefig(filename.replace(".png", "-hires.png"), dpi=600)
        print(f"Saved pairplot to {filename}")
    return g, filename


def verification_plot(
    model_id,
    verification_candidates,
    metric_name,
    markersize=15,
    aspect_ratio=0.7,
    fig_width=10,
    save=True,
    save_hires=False,
    save_dir="verifications_scatterplot",
):
    set_plot_style(font_scale=1.5)

    metric_values = [c["main_metric"] for c in verification_candidates]
    max_probs = [c["max_prob"] for c in verification_candidates]
    n_below_threshold = sum(p < 0.01 for p in max_probs)
    ylabel = "Max(token probability in verification)"
    g = sns.scatterplot(
        {metric_name: metric_values, ylabel: max_probs},
        x=metric_name,
        y=ylabel,
        s=markersize,
    )
    g.set(yscale="log")
    g.axhline(0.01, linestyle="--", color="lightgrey")
    plt.gcf().set_size_inches(fig_width, fig_width * aspect_ratio)  # Adjust figure size
    plt.tight_layout()
    filename = output_name(model_id, save_dir, "png")
    if save:
        plt.savefig(filename, dpi=300)  # , bbox_inches="tight")  # Save as high quality PNG
        if save_hires:
            plt.savefig(filename.replace(".png", "-hires.png"), dpi=600)
        print(
            f"Saved verification plot to {filename}: {n_below_threshold}/{len(verification_candidates)} below p=0.01 threshold"
        )
    return g, filename


# ---- token filtering ---


def find_byte_tokens(toka: TokenizerAnalyzer, token_infos: dict[int, dict]) -> dict[int, dict]:
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


# ---- tables ----


def make_tokens_table(
    toka: TokenizerAnalyzer,
    token_infos: Union[dict[int, dict], list[dict]],
    find_superstrings_in: Optional[Iterable] = None,
    threshold=1e9,
    truncate=20,
    xcols=None,
    tablefmt="github",
) -> tuple[str, int]:
    if isinstance(token_infos, dict):
        token_infos = list(token_infos.values())
    superstring_token_to_maxprob = {ti["i"]: ti.get("max_prob") for ti in find_superstrings_in or []}

    def color_format_proba(p, text=None):
        if p < 0.001:
            color = "rgb(169, 68, 66)"  # dark red
        elif p < 0.01:
            color = "rgb(255, 145, 0)"  # orange
        elif p < 0.1:
            color = "rgb(251, 189, 8)"  # yellow
        else:  # > 0.9
            color = "rgb(40, 167, 69)"  # green
        text = text or f"{p:.2g}"
        return f"<span style='border: 1px solid {color};'>{text}</span>"

    def token_as_markdown(i, color=False):
        token = toka.vocab_to_readable_string(i)
        token = repr(token)[1:-1]  # escape \n, unicode, etc
        token = token.replace(" ", "▁")  # make spaces show clearly
        token = token.replace("\\\\", "\\")  # un-escape \
        token = token.replace("|", r"\|")  # breaks tables
        token = f"````` {token} `````"  # more ` such that even ```` in tokens doesn't break markdown
        if color and (sp := superstring_token_to_maxprob.get(i)) is not None:
            token = color_format_proba(sp, token)
        return token

    def token_info_cols(ti):
        info_dict = dict(
            token_id=ti["i"],
            token=token_as_markdown(ti["i"]),
            metric=ti["main_metric"],
            **{k: ti[k] for k in (xcols or []) if ti.get(k)},
        )
        if "reencoded" in info_dict:  # unreachable tokens
            info_dict["reencoded"] = ", ".join(f"{i}: {token_as_markdown(i)}" for i in ti["reencoded_ids"])
        if "max_prob" in info_dict:
            info_dict["max_prob"] = color_format_proba(info_dict["max_prob"])
        if find_superstrings_in:
            superstrings = [
                st for st in find_superstrings_in if ti["raw_vocab"] in st["raw_vocab"] and st["i"] > ti["i"]
            ]
            if superstrings:
                info_dict["in_other_tokens"] = ", ".join(
                    token_as_markdown(st["i"], color=True) for st in superstrings[:5]
                )
                if len(superstrings) > 5:
                    info_dict["in_other_tokens"] += f", ..."
        return info_dict

    token_infos = sorted(token_infos, key=lambda x: x["main_metric"])
    headers = "keys"

    below_thr = [token_info_cols(ti) for ti in token_infos if ti["main_metric"] < threshold]
    above_thr = [token_info_cols(ti) for ti in token_infos if ti["main_metric"] >= threshold]
    below_thr_table_main = tabulate.tabulate(below_thr[:truncate], headers=headers, tablefmt=tablefmt)
    below_thr_table_more = tabulate.tabulate(below_thr[truncate:], headers=headers, tablefmt=tablefmt)

    markdown = f"{len(below_thr)} entries below threshold of {threshold:.3f}\n\n{below_thr_table_main}\n"
    if len(below_thr) > truncate:
        markdown += f"<details><summary>{len(below_thr)-truncate} additional entries below threshold</summary>\n\n{below_thr_table_more}\n</details>\n"

    if above_thr:
        above_thr_table = tabulate.tabulate(above_thr, headers=headers, tablefmt=tablefmt)
        markdown += f"<details><summary>{len(above_thr)} additional entries above threshold</summary>\n\n{above_thr_table}\n</details>"

    return markdown, len(below_thr)


# --- main report


def get_verified_candidates(token_infos):
    verification_candidates, verification_cand_threshold = candidates_for_verification(token_infos)
    if not all("max_prob" in c for c in verification_candidates):
        n_total = len(verification_candidates)
        verification_candidates = [c for c in verification_candidates if "max_prob" in c]
        print(
            f"❗ WARNING: verification step not completed, loaded {len(verification_candidates)} out of {n_total} candidates"
        )
    return verification_candidates, verification_cand_threshold


def make_tokens_report(model_id, toka, moda, token_infos, metric_ix, save_hires=False):
    metric_names, undertrained_token_metrics = get_metrics(moda, token_infos)

    build_prompt_token = select_placeholder_token(toka, token_infos)
    verification_candidates, verification_cand_threshold = get_verified_candidates(token_infos)
    single_byte_vocab = find_byte_tokens(toka, token_infos)
    special_token_vocab = find_special_tokens(token_infos)
    exclude = set(single_byte_vocab.keys()) | set(special_token_vocab.keys())
    candidates_without_excl = [ti for ti in verification_candidates if ti["i"] not in exclude]
    unreachable_without_excl = [
        ti for ti in token_infos.values() if "UNREACHABLE" in ti["category"] and ti["i"] not in exclude
    ]
    undecodable_without_excl = [
        ti for ti in token_infos.values() if "UNDECODEABLE" in ti["category"] and ti["i"] not in exclude
    ]

    # plot verifications first, so we can look at them even if we don't have a threshold
    _, verification_filename = verification_plot(
        model_id, verification_candidates, metric_names[metric_ix], save_hires=save_hires
    )
    _, metrics_filename = metrics_pairplot(token_infos, toka, moda, color_by_id=True, save_hires=save_hires)

    # find threshold for table collapse
    p_verify_threshold = 0.01
    window = 12
    frac_verified_thr = 2.0 / 3
    verifications_below_threshold = np.array([c["max_prob"] < p_verify_threshold for c in candidates_without_excl])

    first_below_thr = window
    # find threshold where verification rate drops below 2/3
    while first_below_thr + window < len(candidates_without_excl):
        if (
            verifications_below_threshold[first_below_thr - window : first_below_thr + window + 1].mean()
            < frac_verified_thr
        ):
            break
        first_below_thr += 1
    else:
        raise ValueError("No threshold detected")
    candidates_threshold = candidates_without_excl[first_below_thr - 1]["main_metric"]
    verified_median_threshold = np.percentile(
        [c["main_metric"] for c in candidates_without_excl if c["max_prob"] < p_verify_threshold],
        50,
    )

    #  token reports tables for various specific categories
    bytes_report, n_bytes_below_thr = make_tokens_table(
        toka,
        single_byte_vocab,
        threshold=verified_median_threshold,
        xcols=["ord", "hex", "byte_type", "reencoded"],
    )
    special_report, n_special_below_thr = make_tokens_table(
        toka,
        special_token_vocab,
        threshold=verified_median_threshold,
        xcols=["reencoded", "max_prob"],  # may be unreachable or tested
    )
    unreachable_report, n_unreachable_below_thr = make_tokens_table(
        toka,
        unreachable_without_excl,
        threshold=verified_median_threshold,
        xcols=["reencoded"],
    )

    # magikarps report - a little slow with find_superstrings_in
    magikarps_report, n_magikarps_below_thr = make_tokens_table(
        toka,
        candidates_without_excl,
        threshold=candidates_threshold,
        xcols=["max_prob"],
        find_superstrings_in=token_infos.values(),
    )
    undecodable_report, n_undecodable_below_thr = make_tokens_table(
        toka,
        undecodable_without_excl,
        threshold=candidates_threshold,
        find_superstrings_in=token_infos.values(),
    )

    # make a giant markdown file and write it

    # summary
    markdown_report = f"# Report for `{model_id}`\n"
    markdown_report += "\n## Model info\n\n"
    if moda is not None:
        markdown_report += "* Tied embeddings: " + ("yes" if moda.tied_embeddings else "no") + "\n"
        markdown_report += f"* Unembeddings use bias: " + ("yes" if moda.unembedding_has_bias else "no") + "\n"
    markdown_report += f"* Metric for under-trained tokens: {metric_names[metric_ix]}\n"
    metric_values_mean = np.mean(undertrained_token_metrics[:, metric_ix])
    metric_values_std = np.std(undertrained_token_metrics[:, metric_ix])
    markdown_report += f"  * Overall distribution {metric_values_mean:.3f} +/- {metric_values_std:.3f}\n"
    markdown_report += (
        f"  * Token used for verification prompt building: `{toka.vocab_to_readable_string(build_prompt_token['i'])}`\n"
    )
    markdown_report += f"  * Verification threshold: {verification_cand_threshold:.3f}\n"
    markdown_report += f"  * Threshold for showing candidate under-trained tokens: {candidates_threshold:.3f}\n"
    markdown_report += (
        f"  * Median verified threshold (for bytes, unreachable and special tokens): {verified_median_threshold:.3f}\n"
    )

    if moda is not None:
        markdown_report += f"* Embeddings shape: {moda.embeddings.shape}\n"
    markdown_report += f"* Vocabulary size: {len(token_infos)}\n"
    markdown_report += f"  * Number of single byte tokens: {len(single_byte_vocab)}, of which {n_bytes_below_thr} below metric threshold\n"
    markdown_report += f"  * Number of special tokens: {len(special_token_vocab)}, of which {n_special_below_thr} below metric threshold\n"
    if len(unreachable_without_excl):
        markdown_report += f"  * Number of unreachable non-single-byte tokens: {len(unreachable_without_excl)}, of which {n_unreachable_below_thr} below metric threshold\n"
    if len(undecodable_without_excl):
        markdown_report += f"  * Number of non-single-byte UTF-fragment tokens: {len(undecodable_without_excl)}, {n_undecodable_below_thr} below soft metric threshold\n"
    markdown_report += f"  * Number of tested under-trained tokens: {len(candidates_without_excl)}, {sum(verifications_below_threshold)} below p = {p_verify_threshold} threshold, {n_magikarps_below_thr} below soft metric threshold\n"
    # plots

    markdown_report += f"\n## Metrics plot\n![Metrics pairplot]({metrics_filename.replace('results/','../')})\n"
    markdown_report += (
        f"\n## Verification plot\n![Verification plot]({verification_filename.replace('results/','../')})\n"
    )

    # tables
    markdown_report += f"\n## Under-trained token verification results\n{magikarps_report}\n"
    if undecodable_without_excl:
        markdown_report += f"\n## Undecodable tokens\n{undecodable_report}\n"

    markdown_report += f"\n## Byte tokens\n{bytes_report}\n"
    markdown_report += f"\n## Special tokens\n{special_report}\n"
    if unreachable_without_excl:
        markdown_report += f"\n## Unreachable tokens\n{unreachable_report}\n"

    with open(output_name(model_id, "reports", "md"), "w") as f:
        f.write(markdown_report)

    return locals()
