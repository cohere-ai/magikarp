# Code for the paper "Fishing for Magikarp"

This repository contains the code and extended results for the paper [Fishing for Magikarp: Automatically Detecting Under-trained Tokens in Large Language Models](https://arxiv.org/abs/2405.05417)

## Exploring Results

The most interesting thing in this repository is probably the detailed reports, found in [results/reports](results/reports).

* `▁` (but not `_`) is a space, and `¿entry?` represents tokens with a vocabulary `entry` which was not encoded as expected.


## Running on other models

### Setup

<details><summary>This is a standard <a href="https://python-poetry.org/">poetry</a> project.</summary>

```bash
poetry shell   # make/activate your virtual environment
poetry install # only the first time or on updates
```

</details>

### Running

See `run_verification.sh` for some example commands for running new models. The script itself is mainly a reference for reproducibility and it is not recommended to run.

For models with tied embeddings, or for nicer visualizations and results, you will need to hard-code some unused token ids in `magikarp/unused_tokens.py`.

* If a related model already exists, copying the token ids is likely to work just fine.
* For non-tied embeddings you can typically just let verification finish, and update unused tokens after you get the results.
* For the rare case of new model families with tied embeddings:
    * Take a guess, like `[0]`, or use the tokenizer vocabulary to pick some.
    * Run the `magikarp/fishing.py` script and kill it when it starts verifying.
    * You now have `results/verifications/yourmodel.jsonl` which allows you to look at the vocabulary and update suitable tokens.
    * Update your unused tokens, and run verification.

### Generating results

* `generate_results.py`: Generates plots and markdown reports. This happens automatically after verification, but to regenerate you can `python generate_results.py [your_model_id]` and then look in `results`.


## Contributing

If you want to contribute results for additional models, please include:
  * The `UNUSED_TOKENS` entry
    * ensure tokenization tests (via `pytest`) pass for the new model, which uses this array as a model registry.
  * A line in `run_verification.sh`
  * All files in `results` that are not `.gitignore`'d

## Model requests

If you know of a model that may be interesting to analyze, but do not have the resources to run it yourself, feel free to open an issue. Please add the Hugging Face id, some information on how it is interesting in terms of tokenization, and keep in mind that the larger the model is, the less likely it is to be prioritized.


