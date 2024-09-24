from magikarp.fishing import load_analyzers
from magikarp.unused_tokens import UNUSED_TOKENS
from magikarp.report import hardcoded_indicator_ix, VERIFICATION_THRESHOLD
from magikarp.utils import get_model_and_tokenizer_info, categorize_token_infos, escape_token_for_markdown, output_name
import tabulate, copy, itertools, traceback
import concurrent.futures


def process_model(model_id):
    indicator_ix = hardcoded_indicator_ix(model_id)
    toka, _, token_infos = load_analyzers(
        model_id, indicator_ix=indicator_ix, avoid_loading_model=True, trust_remote_code=True
    )
    try:
        categorized_tokens = categorize_token_infos(toka, token_infos)
        mt_info = get_model_and_tokenizer_info(model_id, toka, token_infos)
    except Exception as e:
        print(f"Error processing model {model_id} - {e.__class__.__name__}: {e}")
        traceback.print_exc()
        return None

    info = {"Model": model_id, "results": categorized_tokens, "indicator_ix": indicator_ix}
    info.update({k: v for _sk, sv in mt_info.items() for k, v in sv.items()})
    return info


def format_info(raw_info, target="notebook", num_tokens=10):
    info = {"Model": raw_info["Model"]}
    output_name_full = output_name(raw_info["Model"], "reports", "md").replace("results/", "")
    output_name_mini = output_name(raw_info["Model"], "reports_mini", "md").replace("results/", "")
    info["reports"] = f"[mini]({output_name_mini}) [full]({output_name_full})"  # Add reports column
    info["Embeddings"] = " × ".join(map(str, raw_info["Embeddings shape"]))
    if raw_info["indicator_ix"] != 0:
        info["Embeddings"] += f"[*]"
    if raw_info["Tied embeddings"]:
        info["Embeddings"] += ", tied"
    if raw_info["LM head uses bias"]:
        info["Embeddings"] += ", with bias"
    info["Tokenizer"] = raw_info.get("Tokenizer Type", "Unknown")
    if "Bytes handling" in raw_info:
        info["Tokenizer"] += ", " + raw_info["Bytes handling"]
    info["Vocab Size"] = raw_info["Vocab Size"]

    vres = raw_info["results"]
    info["# bytes"] = len(vres.bytes)
    info["# unreachable"] = len(vres.unreachables)
    info["# partial utf-8"] = len(vres.partial_utf8)

    cand = vres.candidates
    verified_cand = [c for c in cand if c["max_prob"] < VERIFICATION_THRESHOLD]

    cand_nosb = vres.candidates_nosb
    verified_cand_nosb = [c for c in cand_nosb if c["max_prob"] < VERIFICATION_THRESHOLD]

    info["# partial utf-8"] = len(vres.partial_utf8)
    info["# special"] = len(vres.specials)
    info["# verified"] = f"{len(verified_cand)}/{len(cand)}"
    info["# verified w/o s/b"] = f"{len(verified_cand_nosb)}/{len(cand_nosb)}"

    if target in ["markdown", "notebook"]:
        info["Longest token"] = raw_info["Token for verification prompt building"]
        info["Examples"] = ", ".join(
            escape_token_for_markdown(t["readable_vocab"]) for t in verified_cand_nosb[:num_tokens]
        )
    if target == "markdown":
        info["Examples"] = ", ".join(
            escape_token_for_markdown(t["readable_vocab"]) for t in verified_cand_nosb[:num_tokens]
        )

    return info


def group_key(x):
    return (x.get("Tokenizer Type", "Unknown"), x["Token id for verification prompt building"], x["Tied embeddings"])


models = list(UNUSED_TOKENS.keys())

with concurrent.futures.ThreadPoolExecutor() as executor:
    model_infos_all = list(executor.map(process_model, models))

model_infos = [i for i in model_infos_all if i is not None]
model_infos = sorted(model_infos, key=group_key)
model_infos = [i for g in itertools.groupby(model_infos, key=group_key) for i in sorted(g[1], key=lambda x: x["Model"])]

print(tabulate.tabulate([format_info(i) for i in model_infos], headers="keys", tablefmt="github"))

failed = [model_id for model_id, info in zip(models, model_infos_all) if info is None]

with open("results/summary.md", "w") as f:
    f.write(f"# Summary of under-trained token detection:\n\n")
    f.write("* 'Verified without s/b' refers to without special tokens or single byte tokens\n")
    f.write(
        "\n\n"
        + tabulate.tabulate([format_info(i, target="markdown") for i in model_infos], headers="keys", tablefmt="github")
        + "\n\n"
    )
    f.write(f"Processed {len(model_infos_all)} models, {len(model_infos)} succeeded")
    if failed:
        f.write(f"{len(failed)} failed: {failed}\n")

print(tabulate.tabulate([format_info(i, target="latex") for i in model_infos], headers="keys", tablefmt="github"))

print(f"\nProcessed {len(model_infos_all)} models, {len(model_infos)} succeeded, {len(failed)} failed: {failed}")
