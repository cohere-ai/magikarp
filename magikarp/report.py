# functions for creating visualizations and reports
from typing import Iterable, Optional, Union

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import tabulate

from magikarp.tokenization import TokenizerAnalyzer
from magikarp.utils import output_name, select_placeholder_token, categorize_token_infos,escape_token_for_markdown


plt.rcParams["text.usetex"] = True

def plot_xylabel(s):
    if "E_{" in s:
        s= s.replace('E_{', '$E_{\\rm ').replace('}','}$')
    return s


def hardcoded_indicator_ix(model_id):  # yes this is bad
    indicator_ix = 1 if model_id in ["allenai/OLMo-7B-hf"] else 0
    return indicator_ix


def get_indicators(moda, token_infos):
    if moda is None:
        indicator_names = token_infos[0]["indicator_names"]
        undertrained_token_indicators = np.array([token_info["indicators"] for token_info in token_infos.values()])
    else:
        indicator_names = moda.indicator_names
        undertrained_token_indicators = moda.undertrained_token_indicators
    return indicator_names, undertrained_token_indicators


# ---- plots ----
def set_plot_style(font_scale=0.8):
    sns.set_context("paper")
    sns.set_theme(style="whitegrid", font_scale=font_scale)
    sns.set_style("whitegrid", {"grid.color": ".95", "grid.linestyle": "--"})
    plt.clf()


def indicators_pairplot(
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
    indicator_names, undertrained_token_indicators = get_indicators(moda, token_infos)

    indicators_df = pd.DataFrame({plot_xylabel(k): v for k, v in zip(indicator_names, undertrained_token_indicators.T)})
    fig_width = fig_width / 3 * len(indicator_names)

    set_plot_style()
    plot_kws = {"s": markersize}
    diag_kws = {"bins": 100}
    kws = {}
    if color_by_id:
        p = sns.color_palette("crest", as_cmap=True)
        nt = undertrained_token_indicators.shape[0]
        plot_kws["c"] = [p(i / (nt-1)) for i in range(nt)]

    g = sns.pairplot(
        indicators_df.fillna(0),
        markers=".",
        diag_kind="hist",
        plot_kws=plot_kws,
        diag_kws=diag_kws,
        **kws,
    )
    g.figure.set_size_inches(fig_width, fig_width * aspect_ratio)
    plt.tight_layout()
    filename = output_name(toka.model_id, "indicators_pairplot" + ("_byid" if color_by_id else ""), "png")
    if save:
        plt.savefig(filename, dpi=300)  # , bbox_inches="tight")
        if save_hires:
            plt.savefig(filename.replace(".png", "-hires.png"), dpi=600)
        print(f"Saved pairplot to {filename}")
    return g, filename


def verification_plot(
    model_id,
    verification_candidates,
    indicator_name,
    vertical_line_at=None, # for indicating the 2% threshold in the all tokens plot
    markersize=10, #15,
    aspect_ratio=0.7,
    fig_width=10,
    save=True,
    save_hires=False,
    save_dir="verifications_scatterplot",
):
    set_plot_style(font_scale=1.5)

    indicator_values = [c["main_indicator"] for c in verification_candidates]
    max_probs = [c["max_prob"] for c in verification_candidates]
    n_below_threshold = sum(p < 0.01 for p in max_probs)
    ylabel = "Max(token probability in verification)"
    indicator_name = plot_xylabel(indicator_name)
    g = sns.scatterplot(
        {indicator_name: indicator_values, ylabel: max_probs},
        x=indicator_name,
        y=ylabel,
        s=markersize,
        edgecolor="lightblue",
    )
    g.set(yscale="log")
    g.axhline(0.01, linestyle="--", color="lightgrey")
    if vertical_line_at is not None:
        g.axvline(vertical_line_at, linestyle=":", color="darkgrey")
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


# ---- tables ----


def make_tokens_table(
    toka: TokenizerAnalyzer,
    token_infos: Union[dict[int, dict], list[dict]],
    full: bool,
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
        token = escape_token_for_markdown(token, code_tags=True)
        if color and (sp := superstring_token_to_maxprob.get(i)) is not None:
            token = color_format_proba(sp, token)
        return token

    def token_info_cols(ti):
        info_dict = dict(
            token_id=ti["i"],
            token=token_as_markdown(ti["i"]),
            indicator=ti["main_indicator"],
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

    token_infos = sorted(token_infos, key=lambda x: x["main_indicator"])
    headers = "keys"

    below_thr = [token_info_cols(ti) for ti in token_infos if ti["main_indicator"] < threshold]
    below_thr_table_main = tabulate.tabulate(below_thr[:truncate], headers=headers, tablefmt=tablefmt)
    below_thr_table_more = tabulate.tabulate(below_thr[truncate:], headers=headers, tablefmt=tablefmt)

    markdown = f"{len(below_thr)} entries below threshold of {threshold:.3f}\n\n{below_thr_table_main}\n"
    if len(below_thr) > truncate:
        markdown += f"<details><summary>{len(below_thr)-truncate} additional entries below threshold</summary>\n\n{below_thr_table_more}\n</details>\n"

    if full and any(ti["main_indicator"] >= threshold for ti in token_infos):
        above_thr = [token_info_cols(ti) for ti in token_infos if ti["main_indicator"] >= threshold]       
        above_thr_table = tabulate.tabulate(above_thr, headers=headers, tablefmt=tablefmt)
        markdown += f"<details><summary>{len(above_thr)} additional entries above threshold</summary>\n\n{above_thr_table}\n</details>"

    return markdown, len(below_thr)


# --- main report




def make_tokens_report(model_id, toka, moda, token_infos, indicator_ix, save_hires=False):
    indicator_names, undertrained_token_indicators = get_indicators(moda, token_infos)

    build_prompt_token = select_placeholder_token(toka, token_infos)
    categorized_tokens = categorize_token_infos(toka, token_infos)

    # plot verifications first, so we can look at them even if we don't have a threshold
    _, verification_filename = verification_plot(
        model_id, categorized_tokens.candidates, indicator_names[indicator_ix], save_hires=save_hires
    )
    _, indicators_filename = indicators_pairplot(token_infos, toka, moda, color_by_id=True, save_hires=save_hires)

    # find threshold for table collapse
    p_verify_threshold = 0.01
    window = 12
    frac_verified_thr = 2.0 / 3
    verifications_below_threshold = np.array(
        [c["max_prob"] < p_verify_threshold for c in categorized_tokens.candidates_nosb]
    )

    first_below_thr = window
    # find threshold where verification rate drops below 2/3
    while first_below_thr + window < len(categorized_tokens.candidates_nosb):
        if (
            verifications_below_threshold[first_below_thr - window : first_below_thr + window + 1].mean()
            < frac_verified_thr
        ):
            break
        first_below_thr += 1
    else:
        print("No threshold detected - using last token as threshold.")
        first_below_thr = len(categorized_tokens.candidates_nosb) - 1
    candidates_threshold = categorized_tokens.candidates_nosb[first_below_thr - 1]["main_indicator"]
    cand_below_threshold = [
        c["main_indicator"] for c in categorized_tokens.candidates_nosb if c["max_prob"] < p_verify_threshold
    ]
    if cand_below_threshold:
        verified_median_threshold = float(np.percentile(cand_below_threshold, 50))
    else:
        print("No candidates below threshold, using 0.0")
        verified_median_threshold = 0.0

    # make a giant markdown file and write it
    for full in [False, True]: # short and long versions
        #  token reports tables for various specific categories
        bytes_report, n_bytes_below_thr = make_tokens_table(
            toka,
            categorized_tokens.bytes,
            full=full,
            threshold=verified_median_threshold,
            xcols=["ord", "hex", "byte_type", "reencoded"],
        )
        special_report, n_special_below_thr = make_tokens_table(
            toka,
            categorized_tokens.specials,
            full=full,
            threshold=verified_median_threshold,
            xcols=["reencoded", "max_prob"],  # may be unreachable or tested
        )
        unreachable_report, n_unreachable_below_thr = make_tokens_table(
            toka,
            categorized_tokens.unreachables,
            full=full,
            threshold=verified_median_threshold,
            xcols=["reencoded"],
        )
        # magikarps report - a little slow with find_superstrings_in
        magikarps_report, n_magikarps_below_thr = make_tokens_table(
            toka,
            categorized_tokens.candidates_nosb,
            full=full,
            threshold=candidates_threshold,
            xcols=["max_prob"],
            find_superstrings_in=token_infos.values(),
        )
        undecodable_report, n_undecodable_below_thr = make_tokens_table(
            toka,
            categorized_tokens.partial_utf8,
            full=full,
            threshold=candidates_threshold,
            find_superstrings_in=token_infos.values(),
        )
        
        markdown_report = f"# Report for `{model_id}`\n"
        markdown_report += "\n## Model info\n\n"
        if moda is not None:
            markdown_report += "* Tied embeddings: " + ("yes" if moda.tied_embeddings else "no") + "\n"
            markdown_report += f"* LM head uses bias: " + ("yes" if moda.output_embeddings_has_bias else "no") + "\n"


        markdown_report += f"* Indicator for under-trained tokens: {indicator_names[indicator_ix]}\n"
        indicator_values_mean = np.mean(undertrained_token_indicators[:, indicator_ix])
        indicator_values_std = np.std(undertrained_token_indicators[:, indicator_ix])
        markdown_report += f"  * Overall distribution {indicator_values_mean:.3f} +/- {indicator_values_std:.3f}\n"
        markdown_report += (
            f"  * Token used for verification prompt building: `{toka.vocab_to_readable_string(build_prompt_token['i'])}`\n"
        )
        markdown_report += f"  * Verification threshold: {categorized_tokens.threshold:.3f}\n"
        markdown_report += f"  * Threshold for showing candidate under-trained tokens: {candidates_threshold:.3f}\n"
        markdown_report += (
            f"  * Median verified threshold (for bytes, unreachable and special tokens): {verified_median_threshold:.3f}\n"
        )

        if moda is not None:
            markdown_report += f"* Embeddings shape: {moda.embeddings.shape}\n"
        markdown_report += f"* Vocabulary size: {len(token_infos)}\n"
        markdown_report += f"  * Number of single byte tokens: {len(categorized_tokens.bytes)}, of which {n_bytes_below_thr} below indicator threshold\n"
        markdown_report += f"  * Number of special tokens: {len(categorized_tokens.specials)}, of which {n_special_below_thr} below indicator threshold\n"
        if len(categorized_tokens.unreachables):
            markdown_report += f"  * Number of non-single-byte unreachable tokens: {len(categorized_tokens.unreachables)}, of which {n_unreachable_below_thr} below indicator threshold\n"
        if len(categorized_tokens.partial_utf8):
            markdown_report += f"  * Number of non-single-byte UTF-fragment tokens: {len(categorized_tokens.partial_utf8)}, {n_undecodable_below_thr} below soft indicator threshold\n"
        markdown_report += f"  * Number of tested under-trained tokens: {len(categorized_tokens.candidates)}, {len(categorized_tokens.candidates_nosb)} non-special, {sum(verifications_below_threshold)} below p = {p_verify_threshold} threshold, {n_magikarps_below_thr} below soft indicator threshold\n"
        # plots

        markdown_report += f"\n## Under-trained token indicators plot\n![Indicators scatter plots]({indicators_filename.replace('results/','../')})\n"
        markdown_report += (
            f"\n## Verification plot\n![Verification plot]({verification_filename.replace('results/','../')})\n"
        )

        # tables
        markdown_report += f"\n## Under-trained token verification results\n{magikarps_report}\n"
        if categorized_tokens.partial_utf8:
            markdown_report += f"\n## Tokens with partial UTF-8 sequences\n{undecodable_report}\n"

        markdown_report += f"\n## Byte tokens\n{bytes_report}\n"
        markdown_report += f"\n## Special tokens\n{special_report}\n"
        if categorized_tokens.unreachables:
            markdown_report += f"\n## Unreachable tokens\n{unreachable_report}\n"

        with open(output_name(model_id, "reports" if full else "reports_mini" , "md"), "w") as f:
            f.write(markdown_report)

    return locals()
