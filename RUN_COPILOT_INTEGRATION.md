# How to Run SWE-bench with Copilot CLI Integration

## Quick Setup

1. **Install Dependencies** (run this first):
   ```bash
   cd /Users/bradenstitt/projects/SWE-bench
   pip3 install python-dotenv datasets anthropic openai tiktoken tenacity tqdm numpy beautifulsoup4 ghapi GitPython unidiff rich docker modal pre-commit chardet
   ```

2. **Test Copilot CLI** (make sure it works):
   ```bash
   python3 /tmp/minimal_test.py
   ```

## Running SWE-bench with Copilot CLI

### Option 1: Direct Script Execution

Since the full package installation has dependency conflicts, you can run the script directly by setting the Python path:

```bash
cd /Users/bradenstitt/projects/SWE-bench

# Set Python path and run with a small test dataset
PYTHONPATH=/Users/bradenstitt/projects/SWE-bench python3 swebench/inference/run_api.py \
    --dataset_name_or_path princeton-nlp/SWE-bench_Lite \
    --split test \
    --model_name_or_path copilot-cli \
    --output_dir ./copilot_results
```

### Option 2: Install Package in Development Mode

If you want to install the package properly:

```bash
cd /Users/bradenstitt/projects/SWE-bench

# Install in development mode (may have dependency conflicts)
pip3 install -e .

# Then run normally
python3 swebench/inference/run_api.py \
    --dataset_name_or_path princeton-nlp/SWE-bench_Lite \
    --split test \
    --model_name_or_path copilot-cli \
    --output_dir ./copilot_results
```

## Example Commands

### 1. Basic Test Run
```bash
cd /Users/bradenstitt/projects/SWE-bench
mkdir -p copilot_results

PYTHONPATH=/Users/bradenstitt/projects/SWE-bench python3 swebench/inference/run_api.py \
    --dataset_name_or_path princeton-nlp/SWE-bench_Lite \
    --split test \
    --model_name_or_path copilot-cli \
    --output_dir ./copilot_results
```

### 2. Run with Sharding (for large datasets)
```bash
# Run shard 0 of 4
PYTHONPATH=/Users/bradenstitt/projects/SWE-bench python3 swebench/inference/run_api.py \
    --dataset_name_or_path princeton-nlp/SWE-bench_Lite \
    --split test \
    --model_name_or_path copilot-cli \
    --output_dir ./copilot_results \
    --shard_id 0 \
    --num_shards 4
```

### 3. Check Available Models
```bash
PYTHONPATH=/Users/bradenstitt/projects/SWE-bench python3 swebench/inference/run_api.py --help
```
Look for `copilot-cli` in the model choices.

## Expected Output

The script will create output files like:
- `./copilot_results/copilot-cli__SWE-bench_Lite__test.jsonl`

Each line contains:
```json
{
  "instance_id": "example_id", 
  "model_name_or_path": "copilot-cli",
  "text_inputs": "... original prompt ...",
  "full_output": "... Copilot CLI response ...",
  "model_patch": "... extracted diff ..."
}
```

## Troubleshooting

### 1. Module Import Errors
Use `PYTHONPATH=/Users/bradenstitt/projects/SWE-bench` prefix:
```bash
PYTHONPATH=/Users/bradenstitt/projects/SWE-bench python3 swebench/inference/run_api.py --help
```

### 2. Copilot CLI Not Found
Ensure copilot is in your PATH:
```bash
which copilot
# Should return: /Users/bradenstitt/.nvm/versions/node/v22.16.0/bin/copilot
```

### 3. Authentication Issues
Run copilot interactively first:
```bash
copilot
# Follow authentication prompts
```

### 4. Missing Dependencies
Install all at once:
```bash
pip3 install python-dotenv datasets anthropic openai tiktoken tenacity tqdm numpy beautifulsoup4 ghapi GitPython unidiff rich
```

## Testing Your Integration

Run this quick test to verify everything works:
```bash
python3 /tmp/minimal_test.py
```

This should show:
- ✓ Copilot CLI found
- ✓ Copilot CLI call successful
- ✓ Response received

## Next Steps

Once you have results, you can evaluate them using SWE-bench's evaluation tools:

```bash
# Example evaluation (once you have prediction results)
PYTHONPATH=/Users/bradenstitt/projects/SWE-bench python3 swebench/harness/run_evaluation.py \
    --dataset_name_or_path princeton-nlp/SWE-bench_Lite \
    --split test \
    --predictions_path ./copilot_results/copilot-cli__SWE-bench_Lite__test.jsonl \
    --max_workers 4 \
    --run_id copilot_cli_evaluation
```