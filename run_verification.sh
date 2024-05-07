# Run all verifications and generate most complete results.
# This should just be in results already, but if not, will regenerate all results
# It can also be used to regenerate cached metrics.
# Grouped by model family to allow some disk clearing between runs, but optimized for mirroring UNUSED_TOKENS and not for minimal disk use.

# Loop through each argument and take action based on the argument value
for arg in "$@"; do
    case $arg in
        "gpt2")
            python magikarp/fishing.py --model_id "openai-community/gpt2" 
            python magikarp/fishing.py --model_id "openai-community/gpt2-medium"
            python magikarp/fishing.py --model_id "openai-community/gpt2-large" 
            python magikarp/fishing.py --model_id "openai-community/gpt2-xl"
            python magikarp/fishing.py --model_id "EleutherAI/gpt-j-6b"
            python magikarp/fishing.py --model_id "microsoft/phi-2"
            python generate_results.py "gpt2|gpt-j|phi-2" --load
            ;;
        "neox")
            python magikarp/fishing.py --model_id "EleutherAI/gpt-neox-20b" # --threshold_ratio 100
            python magikarp/fishing.py --model_id "EleutherAI/pythia-6.9b" 
            python magikarp/fishing.py --model_id "allenai/OLMo-7B-hf"  --metric_ix 1
            python magikarp/fishing.py --model_id "allenai/OLMo-1.7-7B-hf" --metric_ix 1 # --threshold_ratio 100
            python generate_results.py "EleutherAI|allenai" --load
            python generate_results.py "OLMo-1.7|neox-20b" --poster --all_tokens_plot --load
            ;;
        "llama2")
            python magikarp/fishing.py --model_id "meta-llama/Llama-2-7b-hf"
            python magikarp/fishing.py --model_id "meta-llama/Llama-2-13b-hf"
            python magikarp/fishing.py --model_id "meta-llama/Llama-2-70b-hf"
            python magikarp/fishing.py --model_id "152334H/miqu-1-70b-sf"
            python magikarp/fishing.py --model_id "microsoft/Phi-3-mini-128k-instruct"
            python generate_results.py "Llama-2|miqu|Phi-3" --load
            ;;        
        "mistral")
            python magikarp/fishing.py --model_id "mistralai/Mistral-7B-v0.1"
            python magikarp/fishing.py --model_id "mistralai/Mistral-7B-Instruct-v0.2"
            python magikarp/fishing.py --model_id "mistralai/Mixtral-8x7B-v0.1"
            python magikarp/fishing.py --model_id "HuggingFaceH4/zephyr-7b-beta" #--threshold_ratio 100
            python magikarp/fishing.py --model_id "upstage/SOLAR-10.7B-v1.0"
            python magikarp/fishing.py --model_id "Rakuten/RakutenAI-7B" 
            python magikarp/fishing.py --model_id "h2oai/h2o-danube2-1.8b-base"
            python magikarp/fishing.py --model_id "Nexusflow/Starling-LM-7B-beta"
#           python magikarp/fishing.py --model_id "microsoft/WizardLM-2-7B" # wizard did a disappearing act, but we have results
            python generate_results.py "mistralai|zephyr|upstage|Rakuten|h2oai|Starling|WizardLM" --load
            python generate_results.py "zephyr" --poster --all_tokens_plot --load
            ;;                       
        "gemma")
            python magikarp/fishing.py --model_id "google/gemma-2b"
            python magikarp/fishing.py --model_id "google/gemma-7b"
            python magikarp/fishing.py --model_id "google/codegemma-7b"
            python generate_results.py "gemma" --load
            ;;        
        "cohere")
            python magikarp/fishing.py --model_id "CohereForAI/c4ai-command-r-v01"
            python magikarp/fishing.py --model_id "CohereForAI/c4ai-command-r-plus"
            python generate_results.py "Cohere" --load --poster
            ;;        
        "tiktoken")
            python magikarp/fishing.py --model_id "Qwen/Qwen1.5-MoE-A2.7B"
            python magikarp/fishing.py --model_id "Qwen/Qwen1.5-32B"
            python magikarp/fishing.py --model_id "Qwen/Qwen1.5-72B-Chat"
            python magikarp/fishing.py --model_id "stabilityai/stablelm-2-12b" --trust-remote-code # missing weights if not trust remote
            python magikarp/fishing.py --model_id "meta-llama/Meta-Llama-3-8B"
            ;;
        "misc")
            python magikarp/fishing.py --model_id "01-ai/Yi-9B"
            python magikarp/fishing.py --model_id "bigcode/starcoder2-15b"
            python magikarp/fishing.py --model_id "ai21labs/Jamba-v0.1" --trust_remote_code
            python generate_results.py "Yi-9B|starcoder2|Jamba" --load
            ;;
        *)
            echo "Error: Invalid argument '$arg'. Supported arguments are: 'gpt2', 'neox', 'llama2', 'mistral', 'gemma', 'cohere', 'tiktoken', 'misc'"
            exit 1
            ;;
    esac
done





