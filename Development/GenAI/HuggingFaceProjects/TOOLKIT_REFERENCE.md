# 🤗 Hugging Face LLM Toolkit - Complete Reference Guide

## Table of Contents
1. [Python Scripts](#python-scripts)
2. [Data Files](#data-files)
3. [Documentation Files](#documentation-files)
4. [Configuration Files](#configuration-files)
5. [Usage Examples](#usage-examples)

---

## Python Scripts

### 1. **hf_llm_fetcher.py**

**Description:**
Basic LLM fetcher that retrieves the top 50 high-value models from Hugging Face Hub. This is the simplest script to get started with high-value LLM data.

**Purpose:**
- Fetch top-ranked LLM models
- Filter by minimum downloads (100+)
- Extract metadata (downloads, likes, tags, creation date)
- Export results to JSON

**Usage:**
```bash
python3 hf_llm_fetcher.py
```

**Output:**
- Console table with top 50 models
- `high_value_llms.json` file with structured data

**Key Features:**
- Automatic filtering by downloads
- Sorts by download count
- Includes author info, likes, and tags
- Error handling with traceback

**Example Output:**
```
Qwen/Qwen3-0.6B          | 15046236     | 1189   | Qwen
openai-community/gpt2    | 13855848     | 3198   | openai-community
Qwen/Qwen2.5-7B-Instruct | 12731921     | 1205   | Qwen
```

---

### 2. **hf_advanced_query.py**

**Description:**
Advanced query tool with flexible search modes and multiple filtering options. This is the most versatile script with CLI interface for complex queries.

**Purpose:**
- Search LLMs by multiple criteria
- Sort by various metrics (downloads, likes, trending, recent)
- Filter by author/organization
- Combine multiple filters
- Export formatted results

**Usage:**

#### Mode 1: Get Top Models
```bash
# Top 30 by downloads
python3 hf_advanced_query.py --mode top --limit 30

# Top 20 by likes
python3 hf_advanced_query.py --mode top --metric likes --limit 20

# Top 25 trending
python3 hf_advanced_query.py --mode top --metric trending --limit 25
```

#### Mode 2: Search by Criteria
```bash
# Models with 1M+ downloads and 500+ likes
python3 hf_advanced_query.py --mode search \
  --min-downloads 1000000 \
  --min-likes 500 \
  --limit 50

# Popular models
python3 hf_advanced_query.py --mode search \
  --min-downloads 5000000 \
  --limit 30
```

#### Mode 3: Get Author's Models
```bash
# Meta-Llama models
python3 hf_advanced_query.py --mode author --author "meta-llama" --limit 20

# Qwen models
python3 hf_advanced_query.py --mode author --author "Qwen" --limit 25

# DeepSeek models
python3 hf_advanced_query.py --mode author --author "deepseek-ai" --limit 15
```

#### Save Results
```bash
# Save any query to JSON
python3 hf_advanced_query.py --mode top --limit 100 --save my_results.json

# Save filtered results
python3 hf_advanced_query.py --mode search \
  --min-downloads 1000000 \
  --save popular_models.json
```

**Command-line Arguments:**
- `--mode` (default: top) - Query mode: `top`, `search`, or `author`
- `--metric` (default: downloads) - Sort metric: `downloads`, `likes`, `trending`, or `recent`
- `--min-downloads` (default: 0) - Minimum download filter
- `--min-likes` (default: 0) - Minimum likes filter
- `--author` - Filter by author name
- `--limit` (default: 30) - Max number of results
- `--save` - Save results to JSON file

**Output:**
- Formatted table display in console
- Optional JSON file with metadata

---

### 3. **hf_analyzer.py**

**Description:**
Statistical analysis tool that analyzes 200+ LLM models and generates comprehensive statistics, trends, and insights.

**Purpose:**
- Analyze large number of models (200+)
- Generate author statistics
- Analyze tags and frameworks
- Calculate metrics (average, min, max, distributions)
- Identify trends and patterns
- Export comprehensive reports

**Usage:**
```bash
# Run full analysis
python3 hf_analyzer.py
```

**Output:**
- Console display with multiple sections:
  - Overall statistics
  - Top authors by downloads
  - Most common tags
- `llm_analysis.json` file with full data

**Features:**
- Analyzes 200+ models
- Author breakdown with averages
- Tag frequency analysis
- Statistical summaries
- Organized report format

**Example Output:**
```
OVERALL STATISTICS:
Total Models Analyzed:     200
Total Downloads:           190,534,540
Total Likes:               150,669
Avg Downloads:             952,672.70
Avg Likes:                 753.35
Max Downloads:             15,046,236
Unique Authors:            86

TOP AUTHORS BY DOWNLOADS:
Qwen          | 17 models | 93,920,391 total downloads
meta-llama    | 12 models | 28,174,371 total downloads
deepseek-ai   | 9 models  | 16,541,400 total downloads
```

---

### 4. **hf_model_downloader.py**

**Description:**
Model downloader for fetching LLM models and files locally. Use this to download models for local inference or analysis.

**Purpose:**
- Download complete models from Hugging Face
- Download specific files from models
- Get model information and metadata
- Estimate disk space requirements
- List downloaded models
- Manage local model cache

**Usage:**

#### Get Model Information
```bash
# Get model info and estimate size
python3 hf_model_downloader.py
```

#### Programmatic Usage (in Python code)
```python
from hf_model_downloader import ModelDownloader

# Initialize downloader
downloader = ModelDownloader(cache_dir="./my_models")

# Download complete model
local_path = downloader.download_model("meta-llama/Llama-2-7b")

# Download specific file
config = downloader.download_specific_file(
    "meta-llama/Llama-2-7b",
    "config.json"
)

# Get model info
info = downloader.get_model_info("meta-llama/Llama-2-7b")

# Estimate disk space
space = downloader.estimate_disk_space("meta-llama/Llama-2-7b")

# List downloaded models
models = downloader.list_downloaded_models()
```

**Features:**
- Download models with progress tracking
- Download individual files
- Get comprehensive model metadata
- Estimate storage requirements
- Automatic cache management
- Filter by file patterns

---

### 5. **example_workflow.py**

**Description:**
Complete workflow example showing how to use all tools together for comprehensive LLM research and analysis.

**Purpose:**
- Demonstrate complete research workflow
- Show how to combine multiple queries
- Generate comparison reports
- Organize results by organization

**Usage:**
```bash
# Run complete workflow
python3 example_workflow.py
```

**What It Does:**
1. Fetches top 30 LLMs by downloads
2. Fetches top 20 LLMs by likes
3. Searches high-value models (1M+ DL, 500+ likes)
4. Analyzes top organizations
5. Generates summary statistics
6. Creates comparison reports

**Output:**
- Multiple formatted tables
- Organization comparison
- Summary statistics
- Detailed analysis report

**Example Output Sections:**
```
[1/5] Fetching top LLMs by downloads...
[2/5] Fetching top LLMs by likes...
[3/5] Searching high-value models...
[4/5] Analyzing top organizations...
[5/5] Generating summary...

ORGANIZATION COMPARISON:
Qwen: 17 models, 93.9M downloads
meta-llama: 12 models, 28.2M downloads
deepseek-ai: 9 models, 16.5M downloads
```

---

## Data Files

### 1. **high_value_llms.json** (36 KB)

**Description:** Curated list of the top 50 high-value LLM models from Hugging Face

**Content Structure:**
```json
{
  "timestamp": "2026-04-15T11:07:45.100820",
  "total_models": 50,
  "models": [
    {
      "model_id": "Qwen/Qwen3-0.6B",
      "author": "Qwen",
      "downloads": 15046236,
      "likes": 1189,
      "private": false,
      "created_at": "2025-04-27 03:40:08+00:00",
      "last_modified": "2025-07-26 03:46:27+00:00",
      "pipeline_tag": "text-generation",
      "tags": ["transformers", "safetensors", "qwen3", ...]
    }
  ]
}
```

**Usage:**
- Reference for top performing models
- Input for model comparison analysis
- Quick lookup of popular models
- Extract metadata for downstream processing

**Best For:**
- Finding trending models
- Benchmark comparison
- Quick model discovery

---

### 2. **llm_analysis.json** (180 KB)

**Description:** Comprehensive analysis of 200+ LLM models with detailed statistics and trends

**Content Structure:**
```json
{
  "timestamp": "2026-04-15T11:09:45.000000",
  "statistics": {
    "total_models_analyzed": 200,
    "total_downloads": 190534540,
    "unique_authors": 86,
    "total_unique_tags": 764,
    "avg_downloads": 952672.70,
    "max_downloads": 15046236
  },
  "author_analysis": {
    "Qwen": {
      "count": 17,
      "total_downloads": 93920391,
      "avg_downloads": 5524728,
      "models": ["Qwen/Qwen3-0.6B", ...]
    }
  },
  "tag_statistics": {
    "text-generation": 200,
    "transformers": 141,
    "conversational": 164,
    ...
  },
  "models": [...]
}
```

**Usage:**
- Deep analysis and statistics
- Trend identification
- Organization comparison
- Tag-based insights
- Metric analysis

**Best For:**
- Research and analysis
- Report generation
- Data science projects
- Trend tracking

---

### 3. **meta_llama_models.json** (6 KB)

**Description:** Collection of all Meta-Llama LLM models retrieved from Hugging Face

**Usage:**
- Quick reference for Meta-Llama models
- Comparison within Llama family
- Benchmark for Meta's models
- Example query result

**Models Included:**
- Llama-3.1-8B-Instruct (9.4M downloads)
- Llama-3.2-3B (1.1M downloads)
- Meta-Llama-3-8B (3.2M downloads)
- And more...

---

### 4. **Custom Query Results**

Generated dynamically when you use `--save` parameter:
```bash
python3 hf_advanced_query.py --mode author --author "deepseek-ai" --save deepseek.json
```

**Usage:**
- Store query results for later analysis
- Build result collections
- Create comparison datasets
- Archive research

---

## Documentation Files

### 1. **README.md**

**Description:** Complete documentation with full API reference, installation, usage examples, and troubleshooting

**Contains:**
- Setup instructions
- Script descriptions
- Detailed usage examples
- Output format explanation
- API reference
- Tips and tricks
- Troubleshooting guide

**Best For:**
- Comprehensive learning
- API reference
- Detailed examples
- Problem solving

**Usage:**
```bash
# Read full documentation
cat README.md
# or
less README.md
```

---

### 2. **QUICKSTART.md**

**Description:** 5-minute quick start guide for getting up and running immediately

**Contains:**
- Quick setup (5 minutes)
- Common use cases
- Basic commands
- Expected results
- Output samples
- Tips and tricks

**Best For:**
- New users
- Quick reference
- Common tasks
- Getting started

**Usage:**
```bash
# Read quick start
cat QUICKSTART.md
```

---

### 3. **PROJECT_OVERVIEW.md**

**Description:** Comprehensive project overview with complete feature list, structure, and learning path

**Contains:**
- Project structure
- Feature list
- Complete statistics
- Use cases
- Learning path
- Advanced usage
- Integration opportunities

**Best For:**
- Project understanding
- Feature discovery
- Use case mapping
- Advanced usage

---

### 4. **COMPLETION_REPORT.md**

**Description:** Detailed completion report showing deliverables, results, and verification status

**Contains:**
- Deliverables checklist
- Results summary
- Feature implementation status
- Performance metrics
- Quality checklist
- Next steps

**Best For:**
- Project verification
- Deliverables confirmation
- Quality assurance
- Progress tracking

---

### 5. **INDEX.md**

**Description:** File index and organization reference

**Best For:**
- File lookup
- Project structure navigation
- Finding specific files

---

### 6. **SUMMARY.md**

**Description:** Feature summary and capabilities overview

**Best For:**
- Feature discovery
- Quick overview
- Capability reference

---

### 7. **STATUS.sh**

**Description:** Executable bash script that displays formatted status report

**Usage:**
```bash
bash STATUS.sh
```

**Output:**
- Beautiful formatted status report
- Key statistics
- Quick reference commands
- Verification checklist

---

## Configuration Files

### 1. **requirements.txt**

**Description:** Python package dependencies for the project

**Content:**
```
huggingface-hub==1.10.2
requests==2.33.1
pyyaml==6.0.3
tqdm==4.67.3
```

**Usage:**
```bash
# Install all dependencies
pip install -r requirements.txt
```

**Packages:**
- `huggingface-hub` - Hugging Face API client
- `requests` - HTTP library
- `pyyaml` - YAML parsing
- `tqdm` - Progress bars

---

### 2. **venv/** (Virtual Environment)

**Description:** Python virtual environment with all dependencies installed

**Usage:**
```bash
# Activate virtual environment
source venv/bin/activate

# Run any script
python3 script_name.py

# Deactivate when done
deactivate
```

---

## Usage Examples

### Scenario 1: Find Top Models

**Objective:** Discover the most popular LLM models
```bash
source venv/bin/activate
python3 hf_advanced_query.py --mode top --limit 50
```

**Output:** Top 50 models by downloads in formatted table

---

### Scenario 2: Find High-Quality Models

**Objective:** Find models with both popularity and community approval
```bash
python3 hf_advanced_query.py --mode search \
  --min-downloads 5000000 \
  --min-likes 1000 \
  --limit 30 \
  --save high_quality.json
```

**Output:** 
- Table with filtered results
- `high_quality.json` with full data

---

### Scenario 3: Compare Organizations

**Objective:** Compare models from different organizations
```bash
# Get Qwen models
python3 hf_advanced_query.py --mode author --author "Qwen" --save qwen.json

# Get Meta-Llama models
python3 hf_advanced_query.py --mode author --author "meta-llama" --save llama.json

# Get DeepSeek models
python3 hf_advanced_query.py --mode author --author "deepseek-ai" --save deepseek.json
```

**Output:** Three separate JSON files for comparison

---

### Scenario 4: Run Full Analysis

**Objective:** Generate comprehensive statistics and insights
```bash
python3 hf_analyzer.py
```

**Output:**
- Console report with statistics
- `llm_analysis.json` with complete analysis

---

### Scenario 5: Complete Research Workflow

**Objective:** Perform comprehensive research on LLMs
```bash
python3 example_workflow.py
```

**Output:**
- Multiple analysis sections
- Organization comparisons
- Summary statistics
- Multiple formatted tables

---

### Scenario 6: Get Trending Models

**Objective:** Find trending/recently popular models
```bash
python3 hf_advanced_query.py --mode top --metric trending --limit 25
```

**Output:** Top 25 trending models

---

### Scenario 7: Build Custom Dataset

**Objective:** Create a custom dataset of models matching criteria
```bash
python3 hf_advanced_query.py --mode search \
  --min-downloads 2000000 \
  --min-likes 300 \
  --limit 100 \
  --save my_dataset.json
```

**Output:** `my_dataset.json` with 100 matching models

---

## Quick Command Reference

| Task | Command |
|------|---------|
| Get top 50 models | `python3 hf_advanced_query.py --mode top --limit 50` |
| Get top by likes | `python3 hf_advanced_query.py --mode top --metric likes --limit 30` |
| Get trending | `python3 hf_advanced_query.py --mode top --metric trending --limit 25` |
| Search criteria | `python3 hf_advanced_query.py --mode search --min-downloads 1000000` |
| Get author models | `python3 hf_advanced_query.py --mode author --author "meta-llama"` |
| Run analysis | `python3 hf_analyzer.py` |
| Run workflow | `python3 example_workflow.py` |
| Fetch top 50 | `python3 hf_llm_fetcher.py` |
| Save results | `python3 hf_advanced_query.py --mode top --save output.json` |

---

## File Organization

```
/Users/deb/Development/GenAI/HuggingFaceProjects/
│
├── 🐍 Python Scripts (5)
│   ├── hf_llm_fetcher.py              ← Start here for basics
│   ├── hf_advanced_query.py           ← Main tool for queries
│   ├── hf_analyzer.py                 ← Run for statistics
│   ├── hf_model_downloader.py         ← Download models
│   └── example_workflow.py            ← See complete example
│
├── 📊 Data Files (4+)
│   ├── high_value_llms.json           ← Top 50 models
│   ├── llm_analysis.json              ← Full analysis
│   ├── meta_llama_models.json         ← Meta-Llama collection
│   └── [custom results]               ← Your saved queries
│
├── 📚 Documentation (7)
│   ├── README.md                      ← Full docs
│   ├── QUICKSTART.md                  ← Quick start
│   ├── PROJECT_OVERVIEW.md            ← Complete overview
│   ├── COMPLETION_REPORT.md           ← Details
│   ├── INDEX.md                       ← File index
│   ├── SUMMARY.md                     ← Summary
│   └── STATUS.sh                      ← Visual status
│
└── ⚙️ Configuration (2)
    ├── requirements.txt               ← Dependencies
    └── venv/                          ← Virtual environment
```

---

## Getting Started

1. **Read QUICKSTART.md** (5 minutes)
2. **Activate venv**: `source venv/bin/activate`
3. **Run basic query**: `python3 hf_advanced_query.py --mode top --limit 10`
4. **Explore more**: Try different modes and filters
5. **Read full docs**: Check README.md for detailed reference

---

**Version:** 1.0  
**Status:** ✅ Production Ready  
**Created:** April 15, 2026
