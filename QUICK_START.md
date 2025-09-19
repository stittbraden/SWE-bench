# Quick Start: Running SWE-bench with GitHub Copilot CLI

## ✅ Integration Complete!

I've successfully added GitHub Copilot CLI support to SWE-bench. The integration is ready to use!

## 🚀 How to Run

### Step 1: Verify Setup
```bash
# Test that Copilot CLI works
python3 /tmp/minimal_test.py
```
You should see: `✓ Copilot CLI integration test PASSED`

### Step 2: Run SWE-bench with Copilot CLI

```bash
cd /Users/bradenstitt/projects/SWE-bench

# Use the processed dataset that has the 'text' column
PYTHONPATH=/Users/bradenstitt/projects/SWE-bench python3 swebench/inference/run_api.py \
    --dataset_name_or_path princeton-nlp/SWE-bench_Lite_bm25_13K \
    --split test \
    --model_name_or_path copilot-cli \
    --output_dir ./copilot_results
```

### Step 3: Check Available Models
```bash
PYTHONPATH=/Users/bradenstitt/projects/SWE-bench python3 swebench/inference/run_api.py --help
```

You should see `copilot-cli` in the list of available models:
```
--model_name_or_path {claude-2,claude-3-haiku-20240307,claude-3-opus-20240229,claude-3-sonnet-20240229,claude-instant-1,copilot-cli,gpt-3.5-turbo-0613,...}
```

## 📁 What Was Added

### Files Modified:
- `swebench/inference/run_api.py` - Added copilot-cli support

### Files Created:
- `COPILOT_CLI_INTEGRATION.md` - Detailed documentation
- `RUN_COPILOT_INTEGRATION.md` - Setup instructions  
- `QUICK_START.md` - This file
- `/tmp/minimal_test.py` - Simple test script

## 🔧 Integration Details

The integration adds:

1. **Model Support**: `copilot-cli` as a valid model choice
2. **CLI Wrapper**: Function that calls `copilot -p "prompt"` 
3. **Inference Pipeline**: Full SWE-bench compatible inference function
4. **Cost Tracking**: $0 cost (covered by Copilot subscription)
5. **Error Handling**: Retry logic and timeout handling

## 📊 Example Usage

### Run on Small Dataset
```bash
PYTHONPATH=/Users/bradenstitt/projects/SWE-bench python3 swebench/inference/run_api.py \
    --dataset_name_or_path princeton-nlp/SWE-bench_Lite_bm25_13K \
    --split test \
    --model_name_or_path copilot-cli \
    --output_dir ./copilot_results \
    --max_cost 100  # No actual cost, but good for testing
```

### Run with Sharding (for large datasets)
```bash
# Run shard 0 of 4 shards
PYTHONPATH=/Users/bradenstitt/projects/SWE-bench python3 swebench/inference/run_api.py \
    --dataset_name_or_path princeton-nlp/SWE-bench_Lite_bm25_13K \
    --split test \
    --model_name_or_path copilot-cli \
    --output_dir ./copilot_results \
    --shard_id 0 \
    --num_shards 4
```

## 📄 Output Format

Results are saved in JSONL format:
```json
{
  "instance_id": "example_id",
  "model_name_or_path": "copilot-cli", 
  "text_inputs": "... original SWE-bench prompt ...",
  "full_output": "... Copilot CLI response ...",
  "model_patch": "... extracted code diff ..."
}
```

## 🎯 Next Steps

1. **Run Evaluation**: Use SWE-bench's evaluation tools on your results
2. **Compare Performance**: Run the same dataset with other models
3. **Scale Up**: Use larger SWE-bench datasets for comprehensive benchmarking

## 🔍 Troubleshooting

- **Module errors**: Always use `PYTHONPATH=/Users/bradenstitt/projects/SWE-bench` prefix
- **CLI errors**: Run `copilot` interactively first to ensure authentication
- **Dependencies**: Run the pip install commands from `RUN_COPILOT_INTEGRATION.md`

## ✨ Success!

You now have a fully functional GitHub Copilot CLI integration for SWE-bench! 

The agent will use Copilot's advanced coding capabilities to solve SWE-bench tasks, giving you insights into how well Copilot performs on real-world software engineering problems.