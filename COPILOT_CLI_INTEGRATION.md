# GitHub Copilot CLI Integration for SWE-bench

This integration adds support for using GitHub Copilot CLI as an agent in SWE-bench benchmarking.

## Overview

The integration allows SWE-bench to use GitHub Copilot CLI to solve coding tasks and benchmarks. It wraps the `copilot` CLI tool and integrates it into the SWE-bench inference pipeline.

## Prerequisites

1. **GitHub Copilot CLI**: Ensure you have the GitHub Copilot CLI installed and configured
   ```bash
   # Install GitHub Copilot CLI (if not already installed)
   npm install -g @githubnext/github-copilot-cli
   
   # Or using the newer official version
   gh extension install github/gh-copilot
   
   # Login to GitHub Copilot
   copilot
   ```

2. **SWE-bench**: Clone and set up SWE-bench as usual

3. **Python Dependencies**: Install SWE-bench dependencies
   ```bash
   pip install -r requirements.txt
   ```

## Integration Details

The integration adds:

- **Model Support**: `copilot-cli` model name
- **CLI Wrapper**: `call_copilot_cli()` function that wraps subprocess calls
- **Inference Function**: `copilot_cli_inference()` following SWE-bench patterns
- **Routing Logic**: Automatic routing for models starting with "copilot"

### Files Modified

- `swebench/inference/run_api.py`: Main integration file with CLI wrapper and inference logic

## Usage Examples

### Basic Usage

Run SWE-bench evaluation with Copilot CLI:

```bash
cd /path/to/SWE-bench

# Run inference on a dataset using Copilot CLI
python swebench/inference/run_api.py \
    --dataset_name_or_path princeton-nlp/SWE-bench_Lite \
    --split test \
    --model_name_or_path copilot-cli \
    --output_dir ./results
```

### With Dataset Sharding

For large datasets, you can use sharding:

```bash
# Run on shard 0 of 4 shards
python swebench/inference/run_api.py \
    --dataset_name_or_path princeton-nlp/SWE-bench_Lite \
    --split test \
    --model_name_or_path copilot-cli \
    --output_dir ./results \
    --shard_id 0 \
    --num_shards 4
```

### With Custom Model Arguments

Although most arguments are ignored by the CLI, you can still specify them for consistency:

```bash
python swebench/inference/run_api.py \
    --dataset_name_or_path princeton-nlp/SWE-bench_Lite \
    --split test \
    --model_name_or_path copilot-cli \
    --output_dir ./results \
    --model_args "temperature=0.7,top_p=0.9"
```

### Full Evaluation Pipeline

1. **Run Inference**:
   ```bash
   python swebench/inference/run_api.py \
       --dataset_name_or_path princeton-nlp/SWE-bench_Lite \
       --split test \
       --model_name_or_path copilot-cli \
       --output_dir ./copilot_results
   ```

2. **Evaluate Results**:
   ```bash
   # Use SWE-bench's evaluation tools
   python swebench/harness/run_evaluation.py \
       --dataset_name_or_path princeton-nlp/SWE-bench_Lite \
       --split test \
       --predictions_path ./copilot_results/copilot-cli__SWE-bench_Lite__test.jsonl \
       --max_workers 4 \
       --run_id copilot_cli_evaluation
   ```

## Configuration

### Environment Variables

The integration doesn't require additional environment variables beyond those needed for GitHub Copilot CLI authentication.

### Model Parameters

The following parameters are supported but ignored by the CLI:
- `temperature`: CLI uses its own temperature settings
- `top_p`: CLI uses its own sampling settings
- `max_cost`: Set to `None` or high value since CLI usage is covered by subscription

### Token Limits

The integration uses approximate token counting (1 token per 4 characters) with a default limit of 200,000 tokens.

## Output Format

The integration produces standard SWE-bench output format:

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

### Common Issues

1. **CLI Not Found**:
   ```
   Error: GitHub Copilot CLI (copilot) not found
   ```
   - Ensure Copilot CLI is installed and in your PATH
   - Try `which copilot` to verify installation

2. **Authentication Issues**:
   - Run `copilot` interactively first to ensure authentication
   - Check your GitHub Copilot subscription status

3. **Timeout Issues**:
   - The integration has a 5-minute timeout per request
   - For very large prompts, consider breaking them down

4. **Permission Issues**:
   - Ensure the Copilot CLI has permission to read the working directory
   - Use `--add-dir` flag if needed: `copilot --add-dir /path/to/swe-bench`

### Debugging

Enable debug logging:

```bash
export COPILOT_LOG_LEVEL=debug
python swebench/inference/run_api.py --model_name_or_path copilot-cli ...
```

## Performance Considerations

- **Speed**: CLI calls are slower than API calls due to subprocess overhead
- **Rate Limits**: Respect GitHub Copilot usage limits
- **Concurrency**: The integration runs sequentially; avoid high concurrency
- **Cost**: Usage is covered by GitHub Copilot subscription (no per-token charges)

## Comparison with Other Agents

| Feature | OpenAI API | Anthropic API | Copilot CLI |
|---------|------------|---------------|-------------|
| Cost | Per-token | Per-token | Subscription |
| Speed | Fast | Fast | Moderate |
| Context | API limits | API limits | Large context |
| Tools | Limited | Limited | Full tooling |
| Local files | No | No | Yes |

## Contributing

To extend or modify the integration:

1. **Add new CLI options**: Modify `call_copilot_cli()` function
2. **Change routing logic**: Update the model name detection in `main()`
3. **Customize output parsing**: Modify response object creation
4. **Add new model variants**: Update `MODEL_LIMITS` dictionary

## License

This integration follows the same license as SWE-bench.