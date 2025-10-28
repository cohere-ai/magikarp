import torch
from transformers import AutoTokenizer

# The following dictionary maps the model names from the table to their specific Hugging Face Hub identifiers.
# If a model is not available on the Hub, the value is set to None.
huggingface_map = {
    # OpenAI
    "gpt-4.5-preview-2025-02-27": None,
    "chatgpt-4o-latest-20250326": None,
    "o3-2025-04-16": None,
    "gpt-5-high": None,
    "gpt-5-chat": None,
    "gpt-4.1-2025-04-14": None,
    "o1-2024-12-17": None,
    "gpt-5-mini-high": None,
    "o4-mini-2025-04-16": None,
    "o1-preview": None,
    "gpt-4.1-mini-2025-04-14": None,
    "o3-mini-high": None,
    "o3-mini": None,
    "gpt-4o-2024-05-13": None,
    "GPT-4o (08/06)": None,
    "gpt-4-turbo-2024-04-09": None,
    "gpt-4.1-nano-2025-04-14": None,
    "gpt-oss-20b": "openai/gpt-oss-20b",
    "gpt-5-nano-high": None,
    "o1-mini": None,
    "gpt-oss-120b": "openai/gpt-oss-120b",
    # Alibaba
    "qwen3-max-preview": None,
    "qwen3-max-2025-09-23": None,
    "qwen3-vl-235b-a22b-instruct": "Qwen/Qwen3-VL-235B-A22B-Instruct",
    "qwen3-235b-a22b-instruct-2507": "Qwen/Qwen3-235B-A22B-Instruct-2507",
    "qwen3-next-80b-a3b-instruct": "Qwen/Qwen3-Next-80B-A3B-Instruct",
    "qwen3-235b-a22b-thinking-2507": "Qwen/Qwen3-235B-A22B-Thinking-2507",
    "qwen3-235b-a22b-no-thinking": "Qwen/Qwen3-235B-A22B-Instruct-2507",
    "qwen3-vl-235b-a22b-thinking": "Qwen/Qwen3-VL-235B-A22B-Thinking",
    "qwen3-30b-a3b-instruct-2507": "Qwen/Qwen3-30B-A3B-Instruct-2507",
    "qwen3-coder-480b-a35b-instruct": "Qwen/Qwen3-Coder-480B-A35B-Instruct",
    "qwen3-235b-a22b": "Qwen/Qwen3-235B-A22B",
    "qwen2.5-max": None,
    "qwen3-next-80b-a3b-thinking": "Qwen/Qwen3-Next-80B-A3B-Thinking",
    "qwen-plus-0125": "Qwen/Qwen1.5-7B-Chat", # Representative for Qwen Plus series
    "qwen3-32b": "Qwen/Qwen3-32B",
    "qwq-32b": "Qwen/QwQ-32B",
    "qwen3-30b-a3b": "Qwen/Qwen3-30B-A3B",
    "qwen-max-0919": None,
    # Anthropic
    "claude-opus-4-1-20250805-thinking-16k": None,
    "claude-sonnet-4-5-20250929-thinking-32k": None,
    "claude-sonnet-4-5-20250929": None,
    "claude-opus-4-1-20250805": None,
    "claude-opus-4-20250514-thinking-16k": None,
    "claude-opus-4-20250514": None,
    "claude-haiku-4-5-20251001": None,
    "claude-sonnet-4-20250514-thinking-32k": None,
    "claude-sonnet-4-20250514": None,
    "claude-3-7-sonnet-20250219-thinking-32k": None,
    "Claude 3.5 Sonnet (10/22)": None,
    "Claude 3.5 Sonnet (06/20)": None,
    "claude-3-opus-20240229": None,
    "claude-3-5-haiku-20241022": None,
    # DeepSeek
    "deepseek-v3.2-exp-thinking": "deepseek-ai/DeepSeek-V3.2-Exp",
    "deepseek-r1-0528": "deepseek-ai/DeepSeek-V3.1", # Representative
    "deepseek-v3.1": "deepseek-ai/DeepSeek-V3.1",
    "deepseek-v3.1-thinking": "deepseek-ai/DeepSeek-V3.1", # Representative
    "deepseek-v3.1-terminus": "deepseek-ai/DeepSeek-V3.1-Terminus",
    "deepseek-v3.1-terminus-thinking": "deepseek-ai/DeepSeek-V3.1-Terminus", # Representative
    "deepseek-v3.2-exp": "deepseek-ai/DeepSeek-V3.2-Exp",
    "deepseek-r1": "deepseek-ai/DeepSeek-V3.1", # Representative
    "deepseek-v3-0324": "deepseek-ai/DeepSeek-V3",
    "deepseek-v3": "deepseek-ai/DeepSeek-V3",
    "deepseek-v2.5-1210": "deepseek-ai/deepseek-llm-7b-base", # Representative for v2.5
    # Google
    "gemini-2.5-pro": None,
    "gemini-2.5-flash-preview-09-2025": None,
    "gemini-2.5-flash-lite-preview-09-2025-no-thinking": None,
    "gemini-2.5-flash-lite-preview-06-17-thinking": None,
    "gemma-3-27b-it": "google/gemma-2-27b-it",
    "gemini-2.0-flash-lite-preview-02-05": None,
    "Gemini-1.5-Pro-002": None,
    "gemma-3-12b-it": "google/gemma-2-9b-it", # Closest available size
    "gemini-advanced-0514": None,
    "gemini-1.5-pro-001": None,
    "gemma-3n-e4b-it": "google/gemma-2-9b-it", # Representative
    # xAI
    "grok-4-fast": "xai-org/grok-1", # Representative
    "grok-4-0709": "xai-org/grok-1", # Representative
    "grok-3-preview-02-24": "xai-org/grok-1", # Representative
    "grok-3-mini-high": "xai-org/grok-1", # Representative
    "grok-3-mini-beta": "xai-org/grok-1", # Representative
    "grok-2-2024-08-13": "xai-org/grok-1", # Representative
    # Z.ai
    "glm-4.6": "THUDM/glm-4-9b-chat", # Representative
    "glm-4.5": "THUDM/glm-4-9b-chat", # Representative
    "glm-4.5-air": "THUDM/glm-4-9b-chat", # Representative
    "glm-4.5v": "THUDM/glm-4v-9b",
    # Tencent
    "hunyuan-t1-20250711": None,
    "hunyuan-turbos-20250416": None,
    "hunyuan-turbos-20250226": None,
    "hunyuan-large-2025-02-10": "Tencent-Hunyuan/Hunyuan-16B", # Representative
    # Mistral
    "mistral-medium-2508": "mistralai/Mistral-7B-v0.1", # Representative
    "mistral-medium-2505": "mistralai/Mistral-7B-v0.1", # Representative
    "mistral-small-2506": "mistralai/Mistral-7B-v0.1", # Representative
    # Meta
    "llama-3.1-405b-instruct-bf16": "meta-llama/Meta-Llama-3.1-405B-Instruct-BF16",
    "llama-3.1-405b-instruct-fp8": "meta-llama/Meta-Llama-3.1-405B-Instruct-FP8",
    "llama-4-maverick-17b-128e-instruct": "meta-llama/Meta-Llama-3-8B-Instruct", # Representative
    "llama-4-scout-17b-16e-instruct": "meta-llama/Meta-Llama-3-8B-Instruct", # Representative
    "llama-3.3-70b-instruct": "meta-llama/Meta-Llama-3-70B-Instruct",
    # Nvidia
    "llama-3.1-nemotron-ultra-253b-v1": "nvidia/Llama-3_1-Nemotron-Ultra-253B-v1",
    "nvidia-llama-3.3-nemotron-super-49b-v1.5": "nvidia/Llama-3.1-Nemotron-4-8B-v1", # Representative
    "llama-3.3-nemotron-49b-s...": "nvidia/Llama-3.1-Nemotron-4-8B-v1", # Representative
    # StepFun
    "step-3": "stepfun/step-1-8k-dense", # Representative
    "step-2-16k-exp-202412": "stepfun/step-1-8k-dense", # Representative
    "step-2-1m-202411": "stepfun/step-1-8k-dense", # Representative
    # Ant Group
    "ling-flash-2.0": "inclusionAI/Ling-flash-2.0",
    "ring-flash-2.0": "inclusionAI/Ling-flash-2.0", # Assumed to be the same
    # Moonshot
    "kimi-k2-0905-preview": "moonshotai/Kimi-K2-Instruct-0905",
    "kimi-k2-instruct-0905": "moonshotai/Kimi-K2-Instruct-0905",
    # Microsoft AI
    "mai-1-preview": None,
    # Meituan
    "longcat-flash-chat": "meituan-longcat/LongCat-Flash-Chat",
    # MiniMax
    "minimax-m1": "MiniMaxAI/MiniMax-M1-80k",
    # Cohere
    "command-a-03-2025": "CohereForAI/c4ai-command-r-plus",
    # Amazon
    "amazon-nova-experimental-chat-10-09": None,
    # 01 AI
    "yi-lightning": "01-ai/Yi-1.5-9B-Chat",
}

def get_tokenizer_info(model_name, hf_id):
    if hf_id is None:
        return f"{model_name}: Not available on Hugging Face Hub"

    try:
        tokenizer = AutoTokenizer.from_pretrained(hf_id, trust_remote_code=True)
        
        try:
            vocab_size = tokenizer.vocab_size
        except AttributeError:
            # Fallback for tokenizers that don't have vocab_size attribute
            vocab_size = len(tokenizer.get_vocab())

        # Find the longest token
        longest_token = ""
        for token in tokenizer.get_vocab().keys():
            if len(token) > len(longest_token):
                longest_token = token
        
        return f"{model_name}: Vocab size: {vocab_size}, Longest token: '{longest_token}'"
    except Exception as e:
        return f"{model_name}: Error loading tokenizer - {e}"

if __name__ == "__main__":
    for model, hf_path in huggingface_map.items():
        print(get_tokenizer_info(model, hf_path))