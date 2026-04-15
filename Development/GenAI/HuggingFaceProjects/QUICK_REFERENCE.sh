#!/bin/bash
# Quick Reference Commands for Hugging Face LLM Project

# Activate virtual environment
source venv/bin/activate

# ============================================
# BASIC COMMANDS
# ============================================

# Fetch top 50 LLMs (basic)
python3 hf_llm_fetcher.py

# Get top 30 models by downloads
python3 hf_advanced_query.py --mode top --limit 30

# Get top 20 models by likes
python3 hf_advanced_query.py --mode top --metric likes --limit 20

# Analyze 200 models with statistics
python3 hf_analyzer.py

# ============================================
# AUTHOR SEARCHES
# ============================================

# Get all Qwen models (Alibaba)
python3 hf_advanced_query.py --mode author --author "Qwen" --limit 25

# Get all Meta-Llama models
python3 hf_advanced_query.py --mode author --author "meta-llama" --limit 20

# Get all DeepSeek models
python3 hf_advanced_query.py --mode author --author "deepseek" --limit 15

# Get all Mistral models
python3 hf_advanced_query.py --mode author --author "mistralai" --limit 15

# Get all Microsoft models
python3 hf_advanced_query.py --mode author --author "microsoft" --limit 10

# ============================================
# FILTERED SEARCHES
# ============================================

# Models with 1M+ downloads
python3 hf_advanced_query.py --mode search --min-downloads 1000000 --limit 30

# Highly popular models (5K+ likes)
python3 hf_advanced_query.py --mode search --min-likes 5000 --limit 20

# Very popular models (1M+ downloads AND 1K+ likes)
python3 hf_advanced_query.py --mode search --min-downloads 1000000 --min-likes 1000 --limit 25

# Find models from Qwen with specific criteria
python3 hf_advanced_query.py --mode search --author "Qwen" --min-downloads 5000000 --limit 10

# ============================================
# EXPORT & SAVE
# ============================================

# Save top 50 models to JSON
python3 hf_advanced_query.py --mode top --limit 50 --save top_50_models.json

# Save Llama models to JSON
python3 hf_advanced_query.py --mode author --author "meta-llama" --limit 25 --save llama_models.json

# Save high-quality models (1M+ downloads, 1K+ likes)
python3 hf_advanced_query.py --mode search \
  --min-downloads 1000000 \
  --min-likes 1000 \
  --limit 30 \
  --save premium_llms.json

# Save models from multiple authors
python3 hf_advanced_query.py --mode author --author "deepseek" --limit 20 --save deepseek_models.json

# ============================================
# DATA FILES
# ============================================

# View high-value LLMs (top 50)
head -50 high_value_llms.json

# Get count of models in analysis
grep -o '"model_id"' llm_analysis.json | wc -l

# Extract model names from JSON
python3 -c "import json; data = json.load(open('high_value_llms.json')); print('\\n'.join([m['model_id'] for m in data['models']]))"

# Get models by author from analysis
python3 -c "import json; data = json.load(open('llm_analysis.json')); qwen = [a for a,s in data['author_analysis'].items() if 'Qwen' in a]; print(qwen)"

# ============================================
# STATISTICS
# ============================================

# Get stats on all generated models
python3 -c "
import json
files = ['high_value_llms.json', 'meta_llama_models.json']
for f in files:
    try:
        data = json.load(open(f))
        print(f'{f}: {data[\"total_models\"]} models, {sum(m[\"downloads\"] for m in data[\"models\"])} total downloads')
    except: pass
"

# List all JSON files with model count
ls -lh *.json | awk '{print $9, $5}'

# ============================================
# CLEANUP
# ============================================

# Remove a single JSON file
rm high_value_llms.json

# Clean all generated JSON files (keep backups!)
# rm *.json

# Clean Python cache
find . -type d -name __pycache__ -exec rm -r {} +
find . -type f -name "*.pyc" -delete

# ============================================
# HELP & INFO
# ============================================

# Get help for advanced query tool
python3 hf_advanced_query.py --help

# Check Python version
python3 --version

# Check installed packages
pip list | grep -E 'huggingface|requests'

# Verify virtual environment
which python3

# ============================================
# ADVANCED USAGE PATTERNS
# ============================================

# Batch process multiple queries
echo "Processing multiple authors..."
for author in "Qwen" "meta-llama" "deepseek-ai" "mistralai"; do
  python3 hf_advanced_query.py --mode author --author "$author" --save "${author}_models.json"
done

# Create comparison report
echo "Creating comparison report..."
python3 -c "
import json, glob
report = {}
for f in glob.glob('*_models.json'):
    data = json.load(open(f))
    report[f] = {'count': data['total_models'], 'timestamp': data['timestamp']}
print(json.dumps(report, indent=2))
" > comparison_report.json

# ============================================
# COMMON WORKFLOWS
# ============================================

# Workflow 1: Find best performing models
echo "Finding best performing models..."
python3 hf_advanced_query.py --mode search \
  --min-downloads 5000000 \
  --min-likes 2000 \
  --limit 20 \
  --save best_models.json

# Workflow 2: Analyze new models
echo "Analyzing all text-generation models..."
python3 hf_analyzer.py

# Workflow 3: Create dataset of top publishers
echo "Creating top publisher dataset..."
for author in "Qwen" "meta-llama" "deepseek-ai" "mistralai" "microsoft"; do
  echo "Fetching $author..."
  python3 hf_advanced_query.py --mode author --author "$author" --limit 20 --save "${author}_collection.json"
done

# ============================================
# TIPS & TRICKS
# ============================================

# View JSON in pretty format
cat high_value_llms.json | python3 -m json.tool | head -50

# Count total models across all files
python3 -c "
import json, glob, os
total = 0
for f in glob.glob('*.json'):
    try:
        data = json.load(open(f))
        count = data.get('total_models', 0)
        total += count
        print(f'{f}: {count} models')
    except: pass
print(f'Total: {total}')
"

# Find models with specific tags
python3 -c "
import json
data = json.load(open('high_value_llms.json'))
chat_models = [m for m in data['models'] if 'chat' in m.get('tags', [])]
print(f'Chat-capable models: {len(chat_models)}')
"

# Deactivate virtual environment
# deactivate
