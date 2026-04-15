# 🤗 Hugging Face LLM Project - Index & Navigation

## 📍 Project Location
```
/Users/deb/Development/GenAI/HuggingFaceProjects/
```

## 📂 Project Contents

### Python Scripts (597 lines of code)

| File | Lines | Purpose | Usage |
|------|-------|---------|-------|
| `hf_llm_fetcher.py` | 132 | Fetch top 50 LLMs | `python3 hf_llm_fetcher.py` |
| `hf_advanced_query.py` | 257 | Advanced filtering & search | `python3 hf_advanced_query.py --help` |
| `hf_analyzer.py` | 208 | Statistical analysis | `python3 hf_analyzer.py` |

### Documentation

| File | Purpose |
|------|---------|
| `README.md` | Comprehensive documentation & API reference |
| `SUMMARY.md` | Project overview & key statistics |
| `QUICK_REFERENCE.sh` | Command reference & usage examples |
| `INDEX.md` | This file |

### Data Files (224 KB total)

| File | Size | Content | Records |
|------|------|---------|---------|
| `high_value_llms.json` | 36 KB | Top 50 LLMs by downloads | 50 models |
| `meta_llama_models.json` | 8 KB | Meta-Llama collection | 10 models |
| `llm_analysis.json` | 180 KB | 200-model analysis | 200 models |

### Configuration
- `venv/` - Python 3.9+ virtual environment
- Dependencies: huggingface-hub 1.10.2, requests 2.33.1

---

## 🚀 Quick Start (3 steps)

### Step 1: Activate Environment
```bash
cd /Users/deb/Development/GenAI/HuggingFaceProjects
source venv/bin/activate
```

### Step 2: Choose Your Tool

**For Basic Fetching:**
```bash
python3 hf_llm_fetcher.py
```

**For Advanced Querying:**
```bash
# Get top 30 models
python3 hf_advanced_query.py --mode top --limit 30

# Find Qwen models
python3 hf_advanced_query.py --mode author --author "Qwen" --limit 20

# Search by criteria
python3 hf_advanced_query.py --mode search --min-downloads 1000000
```

**For Analysis:**
```bash
python3 hf_analyzer.py
```

### Step 3: Export Results
```bash
# Add --save flag to any command
python3 hf_advanced_query.py --mode top --limit 50 --save results.json
```

---

## 🎯 Common Tasks

### Find Something
- **Top 50 LLMs** → `python3 hf_llm_fetcher.py`
- **Popular by author** → `--mode author --author "Qwen"`
- **High quality** → `--mode search --min-downloads 1000000`

### Analyze Data
- **Full analysis** → `python3 hf_analyzer.py`
- **View statistics** → Check generated JSON files
- **Compare models** → `QUICK_REFERENCE.sh` batch commands

### Export & Use
- **Save as JSON** → Add `--save filename.json`
- **View in editor** → Open `.json` files directly
- **Process programmatically** → Use Python scripts

---

## 📊 Key Statistics at a Glance

**From 200 models analyzed:**
- 🏆 **Most Downloads**: Qwen3-0.6B (15M+)
- 👍 **Most Liked**: DeepSeek-R1 (13K+ likes)
- 📊 **Avg Downloads**: 952K per model
- 👥 **Authors**: 86 different organizations
- 🏷️ **Tags**: 764 unique capability tags

**Top Publishers:**
1. Qwen (93.9M downloads, 17 models)
2. Meta-Llama (28.2M downloads, 12 models)
3. DeepSeek (16.5M downloads, 9 models)

---

## 📖 Documentation Map

```
README.md
├── Setup Instructions
├── Script Descriptions
│   ├── hf_llm_fetcher.py
│   ├── hf_advanced_query.py (with modes & args)
│   └── hf_analyzer.py
├── Output Format
├── Example Queries
└── Troubleshooting

SUMMARY.md
├── Project Overview
├── Key Statistics
├── Tools Available
├── Data Collected
├── Usage Examples
└── Next Steps

QUICK_REFERENCE.sh
├── Basic Commands
├── Author Searches
├── Filtered Searches
├── Export & Save
├── Data Processing
└── Workflows

INDEX.md (You Are Here)
└── Navigation & Quick Start
```

---

## 💻 Command Reference

### Basic Queries
```bash
# Top 30 models by downloads
python3 hf_advanced_query.py --mode top --limit 30

# Top 20 by likes
python3 hf_advanced_query.py --mode top --metric likes --limit 20
```

### Author Searches
```bash
# Qwen models
python3 hf_advanced_query.py --mode author --author "Qwen"

# Meta-Llama models
python3 hf_advanced_query.py --mode author --author "meta-llama"

# DeepSeek models
python3 hf_advanced_query.py --mode author --author "deepseek-ai"
```

### Filtered Searches
```bash
# Models with 1M+ downloads
python3 hf_advanced_query.py --mode search --min-downloads 1000000

# High-quality (1M+ downloads AND 1K+ likes)
python3 hf_advanced_query.py --mode search \
  --min-downloads 1000000 \
  --min-likes 1000
```

### Save Results
```bash
python3 hf_advanced_query.py --mode top --limit 50 --save my_results.json
```

### Full Analysis
```bash
python3 hf_analyzer.py
```

---

## 🔧 Advanced Features

### Python Integration
```python
from huggingface_hub import list_models

# Get all text-generation models
models = list_models(filter="text-generation", limit=50, full=True)
for model in models:
    print(model.id, model.downloads, model.likes)
```

### JSON Processing
```bash
# View models as list
python3 -c "import json; data = json.load(open('high_value_llms.json')); print([m['model_id'] for m in data['models']])"

# Count models by author
python3 -c "import json; data = json.load(open('llm_analysis.json')); print(len(data['author_analysis']))"
```

### Batch Operations
```bash
# Fetch multiple authors
for author in "Qwen" "meta-llama" "deepseek-ai"; do
  python3 hf_advanced_query.py --mode author --author "$author" --save ${author}_models.json
done
```

---

## 📋 Checklist

Before starting, ensure:
- [ ] Virtual environment activated (`source venv/bin/activate`)
- [ ] All scripts are present (3 .py files)
- [ ] Documentation is readable (3 .md files)
- [ ] Sample data exists (3 .json files)
- [ ] Internet connection available (for API calls)

---

## 🆘 Troubleshooting Quick Fixes

| Issue | Solution |
|-------|----------|
| Module not found | Run: `source venv/bin/activate` |
| No results | Lower `--min-downloads` or `--min-likes` |
| Command not found | Check you're in correct directory |
| API rate limit | Wait a moment and retry |
| Permission denied | Run: `chmod +x hf_*.py` |

---

## 🎓 Learning Path

**Beginner** (Start Here)
1. Read: README.md - Overview section
2. Run: `python3 hf_llm_fetcher.py`
3. View: `high_value_llms.json`

**Intermediate**
1. Read: README.md - Command-line arguments
2. Try: Different `--mode` options
3. Run: Author searches (`--mode author`)

**Advanced**
1. Read: SUMMARY.md - Full statistics
2. Run: `python3 hf_analyzer.py`
3. Create: Custom batch scripts
4. Process: JSON with Python

---

## 🔗 Related Resources

**Hugging Face**
- Models Hub: https://huggingface.co/models
- API Docs: https://huggingface.co/docs/hub/api
- Leaderboard: https://huggingface.co/spaces/open-llm-leaderboard

**Top Publishers**
- Qwen: https://huggingface.co/Qwen
- Meta-Llama: https://huggingface.co/meta-llama
- DeepSeek: https://huggingface.co/deepseek-ai
- Mistral: https://huggingface.co/mistralai
- Microsoft: https://huggingface.co/microsoft

---

## ✨ Project Statistics

- **Total Code**: 597 lines of Python
- **Total Docs**: 3 markdown files
- **Total Data**: 224 KB across 3 JSON files
- **Models Analyzed**: 200+
- **Authors Catalogued**: 86
- **Tags Documented**: 764
- **Scripts Created**: 3 (fetcher, query, analyzer)

---

## 📝 Version & Info

- **Created**: April 15, 2026
- **Python Version**: 3.9+
- **Status**: ✅ Production Ready
- **Last Updated**: April 15, 2026
- **Environment**: macOS with zsh

---

**Next Step**: Pick a command from above or read README.md for detailed documentation!
