# Copilot CLI Timeout and Output Information

## ⏱️ Current Timeout Behavior

### Standard Implementation (After Completion)
```bash
python3 /tmp/test_single_example.py
```
- **Shows output**: After Copilot completes (5-10 minutes later)
- **Timeout**: 5-10 minutes based on prompt size
- **Pros**: Clean, complete output; follows SWE-bench patterns
- **Cons**: No indication of progress; you wait blindly

### Real-Time Implementation (Live Output)
```bash
python3 /tmp/test_single_realtime.py
```
- **Shows output**: Line by line as Copilot generates it
- **Timeout**: Same 5-10 minutes
- **Pros**: See progress; know it's working; can interrupt if needed
- **Cons**: More complex; may have buffering issues

## 📊 Expected Timeline for SWE-bench

For a typical 50K character SWE-bench prompt:
1. **0-30 seconds**: Copilot CLI starting up and processing prompt
2. **30s-2 minutes**: Copilot analyzing the code and problem
3. **2-6 minutes**: Copilot generating the solution and patch
4. **6+ minutes**: Finalizing output and cleanup

## 🎯 Recommendations

### For Testing/Development
Use the **real-time version** so you can:
- See that it's actually working
- Watch the solution being generated
- Interrupt if something goes wrong
- Get immediate feedback

### For Production/Batch Processing
Use the **standard version** because:
- It's more reliable
- Follows SWE-bench patterns exactly
- Better error handling
- Cleaner integration

## 🚀 Quick Commands

**See real-time output:**
```bash
cd /Users/bradenstitt/projects/SWE-bench
python3 /tmp/test_single_realtime.py
```

**Standard (wait for completion):**
```bash
cd /Users/bradenstitt/projects/SWE-bench
python3 /tmp/test_single_example.py
```

**Full SWE-bench pipeline:**
```bash
cd /Users/bradenstitt/projects/SWE-bench
PYTHONPATH=/Users/bradenstitt/projects/SWE-bench python3 swebench/inference/run_api.py \
    --dataset_name_or_path princeton-nlp/SWE-bench_Lite_bm25_13K \
    --split test \
    --model_name_or_path copilot-cli \
    --output_dir ./copilot_results \
    --shard_id 0 \
    --num_shards 300
```