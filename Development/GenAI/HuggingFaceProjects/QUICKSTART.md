# Hugging Face LLM Toolkit - Quick Start Guide

## 🚀 Quick Setup (5 minutes)

### 1. Clone and Setup
```bash
cd /Users/deb/Development/GenAI/HuggingFaceProjects
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Run Your First Query
```bash
# Get top 20 LLMs by downloads
python3 hf_advanced_query.py --mode top --limit 20

# Get all Meta-Llama models
python3 hf_advanced_query.py --mode author --author "meta-llama"

# Get high-value models (1M+ downloads)
python3 hf_advanced_query.py --mode search --min-downloads 1000000
```

## 📊 Available Scripts

| Script | Purpose | Command |
|--------|---------|---------|
| `hf_llm_fetcher.py` | Get top 50 LLMs | `python3 hf_llm_fetcher.py` |
| `hf_advanced_query.py` | Flexible LLM search | `python3 hf_advanced_query.py --help` |
| `hf_analyzer.py` | Analyze LLM statistics | `python3 hf_analyzer.py` |
| `hf_model_downloader.py` | Download models | `python3 hf_model_downloader.py` |

## 💡 Common Use Cases

### Find Popular Models
```bash
python3 hf_advanced_query.py --mode top --metric downloads --limit 50
```

### Find Most Liked Models
```bash
python3 hf_advanced_query.py --mode top --metric likes --limit 30
```

### Find Models by Organization
```bash
python3 hf_advanced_query.py --mode author --author "Qwen" --limit 25
python3 hf_advanced_query.py --mode author --author "deepseek-ai" --limit 25
python3 hf_advanced_query.py --mode author --author "mistralai" --limit 25
```

### Save Results to JSON
```bash
python3 hf_advanced_query.py --mode top --limit 100 --save top_100_llms.json
python3 hf_advanced_query.py --mode author --author "meta-llama" --save llama_models.json
```

### Get Detailed Analysis
```bash
python3 hf_analyzer.py
# Generates llm_analysis.json with comprehensive statistics
```

## 📈 Expected Results

### Top Models (as of April 2026)
- **Qwen3-0.6B**: 15M+ downloads
- **GPT-2**: 13M+ downloads
- **Qwen2.5-7B-Instruct**: 12M+ downloads
- **Llama-3.1-8B-Instruct**: 9M+ downloads
- **DeepSeek-R1**: 3M+ downloads, 13K+ likes

### Key Statistics
- 200 analyzed models
- 190M+ total downloads
- 150K+ total likes
- 86 unique authors
- 764 unique tags

## 🔍 Tips & Tricks

### Filter by Multiple Criteria
```bash
# Models with 5M+ downloads AND 1000+ likes
python3 hf_advanced_query.py --mode search \
  --min-downloads 5000000 \
  --min-likes 1000 \
  --limit 50 \
  --save high_quality_models.json
```

### Compare Organizations
```bash
# Run queries for each org and save separately
python3 hf_advanced_query.py --mode author --author "Qwen" --save qwen_models.json
python3 hf_advanced_query.py --mode author --author "meta-llama" --save llama_models.json
python3 hf_advanced_query.py --mode author --author "deepseek-ai" --save deepseek_models.json
```

### Get Trending Models
```bash
python3 hf_advanced_query.py --mode top --metric trending --limit 30
```

### Analyze Model Tags
```bash
python3 hf_analyzer.py
# Check "llm_analysis.json" for tag statistics
```

## 📁 Output Files

After running scripts, you'll get:
- `high_value_llms.json` - Top 50 LLMs
- `llm_analysis.json` - Detailed analysis with statistics
- `meta_llama_models.json` - Meta-Llama models
- Custom JSON files from `--save` parameter

## 🐛 Troubleshooting

### Virtual Environment Issues
```bash
# Reactivate venv
source venv/bin/activate

# Verify packages
pip list | grep huggingface
```

### Rate Limiting
If you hit Hugging Face API rate limits:
- Wait 1-2 minutes
- Reduce `--limit` parameter
- Run fewer queries in parallel

### No Results
- Check author name spelling
- Reduce `--min-downloads` / `--min-likes` thresholds
- Use broader search criteria

## 🔗 Useful Links

- [Hugging Face Hub](https://huggingface.co)
- [huggingface_hub Docs](https://huggingface.co/docs/hub/security-tokens)
- [Model Hub](https://huggingface.co/models)
- [Text Generation Models](https://huggingface.co/models?pipeline_tag=text-generation)

## 📝 Next Steps

1. **Integrate with your app**: Use the scripts as libraries
2. **Add authentication**: Set `HF_TOKEN` for private models
3. **Schedule updates**: Automate daily/weekly queries
4. **Build dashboard**: Visualize trends over time
5. **Compare models**: Download and evaluate locally

## 💻 Advanced: Using as Library

```python
from hf_advanced_query import HFLLMQuery

query = HFLLMQuery()

# Search programmatically
models = query.search_by_criteria(
    min_downloads=1000000,
    min_likes=500,
    author="Qwen",
    limit=20
)

# Display and save
query.display_table(models, "Qwen High-Value Models")
query.save_results(models, "results.json")
```

## 🎯 Success Metrics

✅ Successfully connected to Hugging Face Hub
✅ Retrieved 50+ high-value LLM models
✅ Analyzed 200+ text-generation models
✅ Identified top authors and tags
✅ Created flexible query tools
✅ Generated comprehensive statistics
✅ Ready for production use

---

**Created**: April 15, 2026
**Status**: Ready for use
**Last Updated**: April 15, 2026
