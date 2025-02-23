# Run all verifications and generate most complete results.
# This should just be in results already, but if not, will regenerate all results
# It can also be used to regenerate cached under-trainedness indicators.
# Grouped by model family to allow some disk clearing between runs, but optimized for mirroring UNUSED_TOKENS and not for minimal disk use.

set -e  # Exit immediately if a command exits with a non-zero status

for arg in "$@"; do
    case $arg in
        "gpt2")
            python magikarp/fishing.py --model_id "openai-community/gpt2" 
            python magikarp/fishing.py --model_id "openai-community/gpt2-medium" #--threshold_ratio 100
            python magikarp/fishing.py --model_id "openai-community/gpt2-large" 
            python magikarp/fishing.py --model_id "openai-community/gpt2-xl"
            python magikarp/fishing.py --model_id "EleutherAI/gpt-j-6b"
            python magikarp/fishing.py --model_id "microsoft/phi-2"
            python magikarp/fishing.py --model_id "benjamin/Mistral-7B-v0.1-zett-gpt2"
            ;;
        "neox")
            python magikarp/fishing.py --model_id "EleutherAI/gpt-neox-20b" # --threshold_ratio 100
            python magikarp/fishing.py --model_id "EleutherAI/pythia-6.9b"
            python magikarp/fishing.py --model_id "allenai/OLMo-7B-hf"  --indicator_ix 1
            python magikarp/fishing.py --model_id "allenai/OLMo-1.7-7B-hf" # --threshold_ratio 100
            python magikarp/fishing.py --model_id "allenai/OLMoE-1B-7B-0924"
            ;;
        "llama2")
            python magikarp/fishing.py --model_id "meta-llama/Llama-2-7b-hf"
            python magikarp/fishing.py --model_id "meta-llama/Llama-2-13b-hf"
            python magikarp/fishing.py --model_id "meta-llama/Llama-2-70b-hf"
            python magikarp/fishing.py --model_id "152334H/miqu-1-70b-sf"
            python magikarp/fishing.py --model_id "microsoft/Phi-3-mini-128k-instruct"  --trust-remote-code
            python magikarp/fishing.py --model_id "microsoft/Phi-3.5-mini-instruct"            
            python magikarp/fishing.py --model_id "Skywork/Skywork-13B-base" --trust-remote-code
            ;;        
        "llama3")
            python magikarp/fishing.py --model_id "meta-llama/Meta-Llama-3-8B"
            python magikarp/fishing.py --model_id "meta-llama/Meta-Llama-3-70B"
            python magikarp/fishing.py --model_id "meta-llama/Meta-Llama-3.1-8B"            
            python magikarp/fishing.py --model_id "meta-llama/Meta-Llama-3.1-70B"
            ;;    
        "mistral")
            python magikarp/fishing.py --model_id "mistralai/Mistral-7B-v0.1"
            python magikarp/fishing.py --model_id "mistralai/Mistral-7B-Instruct-v0.2"
            python magikarp/fishing.py --model_id "mistralai/Mistral-7B-v0.3"
            python magikarp/fishing.py --model_id "mistralai/Mixtral-8x7B-v0.1"
            python magikarp/fishing.py --model_id "mistralai/Codestral-22B-v0.1"
            python magikarp/fishing.py --model_id "HuggingFaceH4/zephyr-7b-beta" #--threshold_ratio 100
            python magikarp/fishing.py --model_id "upstage/SOLAR-10.7B-v1.0"
            python magikarp/fishing.py --model_id "upstage/solar-pro-preview-instruct" --trust-remote-code
            python magikarp/fishing.py --model_id "Rakuten/RakutenAI-7B" 
            python magikarp/fishing.py --model_id "h2oai/h2o-danube2-1.8b-base"
            python magikarp/fishing.py --model_id "Nexusflow/Starling-LM-7B-beta"
            ;;                       
        "gemma")
            python magikarp/fishing.py --model_id "google/gemma-2b"
            python magikarp/fishing.py --model_id "google/gemma-7b"
            python magikarp/fishing.py --model_id "google/codegemma-7b"
            ;;        
        "cohere")
            python magikarp/fishing.py --model_id "CohereForAI/c4ai-command-r-v01"
            python magikarp/fishing.py --model_id "CohereForAI/c4ai-command-r-plus"
            python magikarp/fishing.py --model_id "CohereForAI/aya-23-35B"
            ;;        
        "qwen")
            python magikarp/fishing.py --model_id "Qwen/Qwen1.5-MoE-A2.7B"
            python magikarp/fishing.py --model_id "Qwen/Qwen1.5-32B"
            python magikarp/fishing.py --model_id "Qwen/Qwen1.5-72B-Chat"
            python magikarp/fishing.py --model_id "Qwen/Qwen2-57B-A14B"
            python magikarp/fishing.py --model_id "Qwen/Qwen2.5-32B-Instruct"
            python magikarp/fishing.py --model_id "Qwen/Qwen2.5-7B"
            ;;
        "tiktoken")
            python magikarp/fishing.py --model_id "stabilityai/stablelm-2-12b" --trust-remote-code # missing weights if not trust remote
            python magikarp/fishing.py --model_id "mistralai/Mistral-Nemo-Base-2407" --threshold_ratio 5
            ;;
        "allenai")
            python magikarp/fishing.py --model_id "allenai/Llama-3.1-Tulu-3-8B"
            python magikarp/fishing.py --model_id  "allenai/OLMo-2-1124-7B" --indicator_ix 1
            python magikarp/fishing.py --model_id  "allenai/OLMo-2-1124-13B" --indicator_ix 1
            ;;
        "deepseek")
            python magikarp/fishing.py --model_id  "deepseek-ai/deepseek-llm-7b-base"
            python magikarp/fishing.py --model_id  "deepseek-ai/deepseek-math-7b-base"
            python magikarp/fishing.py --model_id  "deepseek-ai/deepseek-coder-33b-base"
            python magikarp/fishing.py --model_id  "deepseek-ai/DeepSeek-V2-Lite" --trust-remote-code
            python magikarp/fishing.py --model_id  "chuxin-llm/Chuxin-1.6B-Base"
            ;;
        "yi")
            python magikarp/fishing.py --model_id "01-ai/Yi-9B"
            python magikarp/fishing.py --model_id "01-ai/Yi-1.5-9B"
            python magikarp/fishing.py --model_id "01-ai/Yi-Coder-9B-Chat"
            ;;
        "ai21")
            python magikarp/fishing.py --model_id "ai21labs/Jamba-v0.1" --trust_remote_code
            python magikarp/fishing.py --model_id "ai21labs/AI21-Jamba-1.5-Mini" --trust-remote-code
            ;;
        "exaone")
            python magikarp/fishing.py --model_id "LGAI-EXAONE/EXAONE-3.0-7.8B-Instruct" --trust-remote-code
            python magikarp/fishing.py --model_id "LGAI-EXAONE/EXAONE-3.5-2.4B-Instruct" --trust-remote-code
            ;;
        "eurollm")
            python magikarp/fishing.py --model_id "utter-project/EuroLLM-1.7B"
            python magikarp/fishing.py --model_id "utter-project/EuroLLM-9B"
            ;;
        "unigram")
            python magikarp/fishing.py --model_id "Fugaku-LLM/Fugaku-LLM-13B"
            python magikarp/fishing.py --model_id "facebook/xglm-7.5B"
            ;;
        "misc")
            python magikarp/fishing.py --model_id "bigcode/starcoder2-15b"
            python magikarp/fishing.py --model_id "ibm-granite/granite-3.0-8b-base"
            python magikarp/fishing.py --model_id "m-a-p/neo_7b" --trust-remote-code
            python magikarp/fishing.py --model_id "internlm/internlm2_5-7b-chat" --trust-remote-code
            python magikarp/fishing.py --model_id "PleIAs/Pleias-1.2b-Preview"
            ;;
        "reports")
            python generate_results.py
            python generate_results.py "OLMo-1.7|neox-20b|zephyr" --poster --all_tokens_plot
            python generate_results.py "Cohere" --poster
            ;;
        *)
            echo "Error: Invalid argument '$arg'. Supported arguments are: 'gemma', 'cohere', 'qwen', 'tiktoken', 'deepseek', 'yi', 'ai21', 'unigram', 'misc', 'reports'"
            exit 1
            ;;
    esac
done





