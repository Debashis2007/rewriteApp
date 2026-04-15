# Hugging Face LLM Fetcher

A Python toolkit for querying and analyzing high-value LLM models from Hugging Face Hub.

## Setup

### Prerequisites
- Python 3.9+
- pip

### Installation

1. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:
```bash
pip install huggingface-hub requests
```

## Scripts

### 1. Basic LLM Fetcher (`hf_llm_fetcher.py`)

Fetches the top 50 high-value LLM models from Hugging Face.

**Usage:**
```bash
source venv/bin/activate
python3 hf_llm_fetcher.py
```

**Output:**
- Displays table of top 50 LLMs with download counts, likes, and authors
- Saves results to `high_value_llms.json`

**Features:**
- Filters models with minimum 100 downloads
- Sorted by download count
- Extracts metadata: author, likes, creation date, tags

### 2. Advanced Query Tool (`hf_advanced_query.py`)

Flexible querying tool with multiple search modes and filters.

**Installation:**
No additional setup needed (uses same venv).

**Usage Examples:**

#### Get Top 30 LLMs by downloads
```bash
python3 hf_advanced_query.py --mode top --limit 30
```

#### Get Top 20 LLMs by likes
```bash
python3 hf_advanced_query.py --mode top --metric likes --limit 20
```

#### Search by criteria (minimum downloads and likes)
```bash
python3 hf_advanced_query.py --mode search --min-downloads 1000000 --min-likes 500
```

#### Get all models from a specific author
```bash
python3 hf_advanced_query.py --mode author --author "meta-llama" --limit 20
```

#### Get models from author with specific metrics
```bash
python3 hf_advanced_query.py --mode author --author "Qwen" --limit 15
```

#### Save results to JSON
```bash
python3 hf_advanced_query.py --mode top --limit 50 --save top_50_llms.json
```

**Command-line Arguments:**

- `--mode` (default: `top`): Query mode - `top`, `search`, or `author`
- `--metric` (default: `downloads`): Sort metric - `downloads`, `likes`, `trending`, or `recent`
- `--min-downloads` (default: `0`): Minimum download filter
- `--min-likes` (default: `0`): Minimum likes filter
- `--author`: Filter by author name
- `--limit` (default: `30`): Maximum number of results
- `--save`: Save results to JSON file

## Output Format

### Console Output
Formatted table showing:
- Model ID
- Author
- Download count
- Like count

### JSON Output
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

## Example Queries

### Find all DeepSeek models
```bash
python3 hf_advanced_query.py --mode author --author "deepseek" --save deepseek_models.json
```

### Get most popular LLMs (100M+ downloads)
```bash
python3 hf_advanced_query.py --mode search --min-downloads 100000000 --limit 50
```

### Find highly-liked models
```bash
python3 hf_advanced_query.py --mode top --metric likes --limit 20
```

### Get trending LLMs
```bash
python3 hf_advanced_query.py --mode top --metric trending --limit 30
```

## Key LLM Publishers

Common high-value authors to query:
- `meta-llama` - Meta's Llama models
- `Qwen` - Alibaba's Qwen models
- `deepseek-ai` - DeepSeek models
- `mistralai` - Mistral AI models
- `openai` - OpenAI models
- `microsoft` - Microsoft models
- `EleutherAI` - EleutherAI models

## Results

The scripts successfully retrieve:
- **Top LLMs by downloads**: Qwen3-0.6B (15M+), GPT-2 (13M+), Qwen2.5-7B (12M+)
- **Most liked LLMs**: Meta-Llama-3-8B (6.5K likes), Llama-3.1-8B-Instruct (5.7K likes)
- **High-value models**: Models with millions of downloads and thousands of likes
- **Comprehensive metadata**: Author, creation date, tags, and pipeline information

## API Reference

### HFLLMQuery Class

#### Methods

- `search_by_criteria(min_downloads, min_likes, author, limit)` - Search with multiple filters
- `get_top_by_metric(metric, limit)` - Get top models by metric
- `get_models_by_author(author, limit)` - Get all models from specific author
- `display_table(models, title)` - Display results in formatted table
- `save_results(models, filename)` - Save to JSON file

## Notes

- Results are cached by download count for faster retrieval
- Timestamps are in ISO 8601 format
- Private models are excluded by default
- Tags provide model capabilities and framework information
- Models are filtered for "text-generation" pipeline tag only

## Troubleshooting

### Module not found error
Ensure you've activated the virtual environment:
```bash
source venv/bin/activate
```

### No results returned
- Check your filter criteria (min-downloads, min-likes may be too high)
- Verify author name spelling
- Try reducing the --limit value

### API rate limiting
Hugging Face Hub has rate limits. If you hit them:
- Wait a few moments before retrying
- Reduce the --limit value
- Use official Hugging Face token for higher limits
