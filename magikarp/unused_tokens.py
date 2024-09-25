import numpy as np

GEMMA_UNUSED_TOKENS = np.arange(7, 106)  # <|unused_token
COHERE_UNUSED_TOKENS = np.arange(255029, 256000)  # above tokenizer size

GPT2_UNUSED_TOKENS = np.arange(177, 188)  # unused 245-255 fallback
TIKTOKEN_UNUSED_TOKENS = GPT2_UNUSED_TOKENS
LLAMA2_UNUSED_TOKENS = np.arange(58, 130)  # duplicate single byte
MISTRAL_UNUSED_TOKENS = np.arange(14, 131)  # duplicate single byte ascii 0x0B to 0x7F

OLMO_UNUSED_TOKENS = np.arange(50280, 50304)  # unused above vocab size
NEOX_UNUSED_TOKENS = [173]  # 0xf1

STARCODER2_UNUSED_TOKENS = [23519, 12740, 27012]  # found after using L2 norm
YI_UNUSED_TOKENS = np.arange(145, 305)  #  <|unused_token
JAMBA_UNUSED_TOKENS = np.arange(4, 515)  # <|maskxxx|>

# Use embeddings above vocab size - note: no weight decay in embeddings for these models
DEEPSEEK_CODE_UNUSED_TOKENS = np.arange(32050, 32250)
DEEPSEEK_LANG_UNUSED_TOKENS = np.arange(101000, 102000)

MAP_NEO_UNUSED_TOKENS = np.arange(248, 259)  # unused 245-255 fallback
FUGAKU_UNUSED_TOKENS = np.arange(278, 289)  # unused 245-255 fallback

# Defines reference unused tokens for models
# optional for most models, but also functions as a kind of registry of models to process

UNUSED_TOKENS = {
    ## required: cohere
    "CohereForAI/c4ai-command-r-v01": COHERE_UNUSED_TOKENS,
    "CohereForAI/c4ai-command-r-plus": COHERE_UNUSED_TOKENS,
    "CohereForAI/aya-23-35B": COHERE_UNUSED_TOKENS,
    # required: gemma
    "google/gemma-7b": GEMMA_UNUSED_TOKENS,
    "google/gemma-2b": GEMMA_UNUSED_TOKENS,
    "google/codegemma-7b": GEMMA_UNUSED_TOKENS,
    # gpt2 variants
    "openai-community/gpt2": GPT2_UNUSED_TOKENS,
    "openai-community/gpt2-medium": GPT2_UNUSED_TOKENS,
    "openai-community/gpt2-large": GPT2_UNUSED_TOKENS,
    "openai-community/gpt2-xl": GPT2_UNUSED_TOKENS,
    "EleutherAI/gpt-j-6b": GPT2_UNUSED_TOKENS,
    "microsoft/phi-2": GPT2_UNUSED_TOKENS,
    "benjamin/Mistral-7B-v0.1-zett-gpt2": [x + 3 for x in GPT2_UNUSED_TOKENS],
    # llama2 and variants
    "meta-llama/Llama-2-13b-hf": LLAMA2_UNUSED_TOKENS,
    "meta-llama/Llama-2-7b-hf": LLAMA2_UNUSED_TOKENS,
    "meta-llama/Llama-2-70b-hf": LLAMA2_UNUSED_TOKENS,
    "152334H/miqu-1-70b-sf": LLAMA2_UNUSED_TOKENS,
    "microsoft/Phi-3-mini-128k-instruct": LLAMA2_UNUSED_TOKENS,
    "microsoft/Phi-3.5-mini-instruct": LLAMA2_UNUSED_TOKENS,
    "Skywork/Skywork-13B-base": LLAMA2_UNUSED_TOKENS,
    # neox and variants
    "EleutherAI/pythia-6.9b": NEOX_UNUSED_TOKENS,
    "EleutherAI/gpt-neox-20b": NEOX_UNUSED_TOKENS,
    "allenai/OLMo-7B-hf": OLMO_UNUSED_TOKENS,  # required since we use secondary metric
    "allenai/OLMo-1.7-7B-hf": OLMO_UNUSED_TOKENS,  # required since we use secondary metric
    "allenai/OLMoE-1B-7B-0924": OLMO_UNUSED_TOKENS,
    # mistral variants
    "mistralai/Mistral-7B-v0.1": MISTRAL_UNUSED_TOKENS,
    "mistralai/Mistral-7B-Instruct-v0.2": MISTRAL_UNUSED_TOKENS,
    "mistralai/Mistral-7B-v0.3": MISTRAL_UNUSED_TOKENS,
    "mistralai/Mixtral-8x7B-v0.1": MISTRAL_UNUSED_TOKENS,
    "mistralai/Codestral-22B-v0.1": MISTRAL_UNUSED_TOKENS,
    "HuggingFaceH4/zephyr-7b-beta": MISTRAL_UNUSED_TOKENS,
    "Rakuten/RakutenAI-7B": MISTRAL_UNUSED_TOKENS,  # extended tokenizer, same unused
    "upstage/SOLAR-10.7B-v1.0": MISTRAL_UNUSED_TOKENS,
    "upstage/solar-pro-preview-instruct": np.arange(248, 259),
    "h2oai/h2o-danube2-1.8b-base": MISTRAL_UNUSED_TOKENS,
    "Nexusflow/Starling-LM-7B-beta": MISTRAL_UNUSED_TOKENS,
    # tiktoken
    "Qwen/Qwen1.5-MoE-A2.7B": TIKTOKEN_UNUSED_TOKENS,
    "Qwen/Qwen1.5-72B-Chat": TIKTOKEN_UNUSED_TOKENS,
    "Qwen/Qwen1.5-32B": TIKTOKEN_UNUSED_TOKENS,
    "Qwen/Qwen2-57B-A14B": TIKTOKEN_UNUSED_TOKENS,
    "Qwen/Qwen2.5-32B-Instruct": TIKTOKEN_UNUSED_TOKENS,
    "stabilityai/stablelm-2-12b": TIKTOKEN_UNUSED_TOKENS,
    "meta-llama/Meta-Llama-3-8B": TIKTOKEN_UNUSED_TOKENS,
    "meta-llama/Meta-Llama-3.1-8B": TIKTOKEN_UNUSED_TOKENS,
    "meta-llama/Meta-Llama-3-70B": TIKTOKEN_UNUSED_TOKENS,
    "meta-llama/Meta-Llama-3.1-70B": TIKTOKEN_UNUSED_TOKENS,
    "internlm/internlm2_5-7b-chat": TIKTOKEN_UNUSED_TOKENS,
    "mistralai/Mistral-Nemo-Base-2407": np.arange(1245, 1256),  # f5-ff
    # deepseek
    "deepseek-ai/deepseek-llm-7b-base": DEEPSEEK_LANG_UNUSED_TOKENS,
    "deepseek-ai/deepseek-coder-33b-base": DEEPSEEK_CODE_UNUSED_TOKENS,
    "deepseek-ai/deepseek-math-7b-base": DEEPSEEK_LANG_UNUSED_TOKENS,
    "deepseek-ai/DeepSeek-V2-Lite": DEEPSEEK_LANG_UNUSED_TOKENS,
    "chuxin-llm/Chuxin-1.6B-Base": DEEPSEEK_LANG_UNUSED_TOKENS,
    # yi
    "01-ai/Yi-9B": YI_UNUSED_TOKENS,
    "01-ai/Yi-1.5-9B": YI_UNUSED_TOKENS,
    "01-ai/Yi-Coder-9B-Chat": YI_UNUSED_TOKENS,
    # unigram
    "Fugaku-LLM/Fugaku-LLM-13B": FUGAKU_UNUSED_TOKENS,
    "facebook/xglm-7.5B": np.arange(256001, 256008),  # <madeupword>
    # others
    "bigcode/starcoder2-15b": STARCODER2_UNUSED_TOKENS,
    "ai21labs/Jamba-v0.1": JAMBA_UNUSED_TOKENS,
    "ai21labs/AI21-Jamba-1.5-Mini": JAMBA_UNUSED_TOKENS,
    "m-a-p/neo_7b": MAP_NEO_UNUSED_TOKENS,
    "LGAI-EXAONE/EXAONE-3.0-7.8B-Instruct": np.arange(100, 150),  # unused ...
}
