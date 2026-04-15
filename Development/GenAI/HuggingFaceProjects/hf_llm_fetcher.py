"""
Hugging Face LLM Fetcher - Retrieve high-value LLM models
"""

from huggingface_hub import list_models, HfApi
import json
from typing import List, Dict
from datetime import datetime


def get_high_value_llms(
    min_downloads: int = 1000,
    sort_by: str = "downloads",
    limit: int = 50
) -> List[Dict]:
    """
    Fetch high-value LLM models from Hugging Face Hub
    
    Args:
        min_downloads: Minimum number of downloads to filter by
        sort_by: Sort criteria (downloads, trending, recent)
        limit: Maximum number of models to retrieve
    
    Returns:
        List of model dictionaries with metadata
    """
    api = HfApi()
    
    print(f"🤗 Fetching high-value LLMs from Hugging Face Hub...")
    print(f"   Filter: minimum {min_downloads} downloads")
    print(f"   Sort by: {sort_by}")
    print(f"   Limit: {limit} models\n")
    
    try:
        # Get all models with filtering
        models = list_models(
            filter="text-generation",  # LLM models
            sort=sort_by,
            limit=limit,
            full=True  # Get full metadata
        )
        
        high_value_llms = []
        
        for model in models:
            # Filter by downloads if available
            if hasattr(model, 'downloads') and model.downloads is not None:
                if model.downloads < min_downloads:
                    continue
            
            model_info = {
                "model_id": model.id,
                "author": getattr(model, 'author', 'N/A'),
                "downloads": getattr(model, 'downloads', 'N/A'),
                "likes": getattr(model, 'likes', 0),
                "private": getattr(model, 'private', False),
                "created_at": str(getattr(model, 'created_at', 'N/A')),
                "last_modified": str(getattr(model, 'last_modified', 'N/A')),
                "pipeline_tag": getattr(model, 'pipeline_tag', 'N/A'),
                "tags": getattr(model, 'tags', []),
            }
            
            high_value_llms.append(model_info)
        
        return high_value_llms
    
    except Exception as e:
        print(f"❌ Error fetching models: {str(e)}")
        import traceback
        traceback.print_exc()
        return []


def display_llms(llms: List[Dict]) -> None:
    """Display LLM models in a formatted table"""
    
    if not llms:
        print("No models found.")
        return
    
    print(f"\n{'='*100}")
    print(f"{'Model ID':<50} | {'Downloads':<12} | {'Likes':<6} | {'Author':<20}")
    print(f"{'='*100}")
    
    for model in llms:
        model_id = model['model_id'][:48] + ".." if len(model['model_id']) > 50 else model['model_id']
        downloads = model['downloads'] if isinstance(model['downloads'], int) else 'N/A'
        likes = model['likes']
        author = model['author'][:18] + ".." if len(model['author']) > 20 else model['author']
        
        print(f"{model_id:<50} | {str(downloads):<12} | {likes:<6} | {author:<20}")
    
    print(f"{'='*100}\n")


def save_to_json(llms: List[Dict], filename: str = "high_value_llms.json") -> None:
    """Save LLM list to JSON file"""
    
    output_data = {
        "timestamp": datetime.now().isoformat(),
        "total_models": len(llms),
        "models": llms
    }
    
    with open(filename, 'w') as f:
        json.dump(output_data, f, indent=2)
    
    print(f"✅ Saved {len(llms)} models to {filename}")


def main():
    """Main execution"""
    
    # Fetch high-value LLMs
    llms = get_high_value_llms(
        min_downloads=100,  # Models with at least 100 downloads
        sort_by="downloads",
        limit=50
    )
    
    # Display results
    display_llms(llms)
    
    # Save to JSON
    if llms:
        save_to_json(llms)
    
    print(f"\n📊 Retrieved {len(llms)} high-value LLM models")


if __name__ == "__main__":
    main()
