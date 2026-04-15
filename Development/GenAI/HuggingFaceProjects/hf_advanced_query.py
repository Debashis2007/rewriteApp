"""
Advanced Hugging Face LLM Query Tool
Allows custom filtering and analysis of high-value LLMs
"""

from huggingface_hub import list_models, HfApi, model_info
import json
from typing import List, Dict, Optional, Literal
from datetime import datetime
import argparse


class HFLLMQuery:
    """Advanced querying tool for Hugging Face LLMs"""
    
    def __init__(self):
        self.api = HfApi()
    
    def search_by_criteria(
        self,
        min_downloads: int = 0,
        min_likes: int = 0,
        author: Optional[str] = None,
        limit: int = 50
    ) -> List[Dict]:
        """Search for LLMs by specific criteria"""
        
        print(f"\n🔍 Searching for LLMs with criteria:")
        print(f"   Min Downloads: {min_downloads}")
        print(f"   Min Likes: {min_likes}")
        if author:
            print(f"   Author: {author}")
        print(f"   Limit: {limit}\n")
        
        models = list_models(
            filter="text-generation",
            sort="downloads",
            limit=limit * 2,  # Fetch more to filter
            full=True
        )
        
        results = []
        
        for model in models:
            downloads = getattr(model, 'downloads', 0) or 0
            likes = getattr(model, 'likes', 0) or 0
            model_author = getattr(model, 'author', 'Unknown')
            
            # Apply filters
            if downloads < min_downloads:
                continue
            if likes < min_likes:
                continue
            if author and author.lower() not in model_author.lower():
                continue
            
            model_info = {
                "model_id": model.id,
                "author": model_author,
                "downloads": downloads,
                "likes": likes,
                "private": getattr(model, 'private', False),
                "created_at": str(getattr(model, 'created_at', 'N/A')),
                "last_modified": str(getattr(model, 'last_modified', 'N/A')),
                "pipeline_tag": getattr(model, 'pipeline_tag', 'N/A'),
                "tags": getattr(model, 'tags', []),
            }
            results.append(model_info)
            
            if len(results) >= limit:
                break
        
        return results
    
    def get_top_by_metric(
        self,
        metric: str = "downloads",
        limit: int = 30
    ) -> List[Dict]:
        """Get top models sorted by a specific metric"""
        
        print(f"\n⭐ Top {limit} LLMs by {metric}\n")
        
        # Map string to valid sort values
        sort_map: Dict[str, Literal['downloads', 'likes', 'trending_score', 'last_modified']] = {
            "downloads": "downloads",
            "likes": "likes",
            "trending": "trending_score",
            "recent": "last_modified"
        }
        sort_value = sort_map.get(metric, "downloads")  # type: ignore
        
        models = list_models(
            filter="text-generation",
            sort=sort_value,  # type: ignore
            limit=limit,
            full=True
        )
        
        results = []
        for model in models:
            model_info = {
                "model_id": model.id,
                "author": getattr(model, 'author', 'Unknown'),
                "downloads": getattr(model, 'downloads', 0),
                "likes": getattr(model, 'likes', 0),
                "private": getattr(model, 'private', False),
                "created_at": str(getattr(model, 'created_at', 'N/A')),
                "last_modified": str(getattr(model, 'last_modified', 'N/A')),
            }
            results.append(model_info)
        
        return results
    
    def get_models_by_author(
        self,
        author: str,
        limit: int = 20
    ) -> List[Dict]:
        """Get all LLM models from a specific author"""
        
        print(f"\n👤 Fetching models from {author}\n")
        
        models = list_models(
            filter="text-generation",
            author=author,
            limit=limit,
            full=True
        )
        
        results = []
        for model in models:
            model_info = {
                "model_id": model.id,
                "author": getattr(model, 'author', 'Unknown'),
                "downloads": getattr(model, 'downloads', 0),
                "likes": getattr(model, 'likes', 0),
                "tags": getattr(model, 'tags', []),
            }
            results.append(model_info)
        
        return results
    
    def display_table(self, models: List[Dict], title: str = "LLM Models") -> None:
        """Display models in a formatted table"""
        
        if not models:
            print(f"No models found.")
            return
        
        print(f"\n{'='*120}")
        print(f"{title.center(120)}")
        print(f"{'='*120}")
        print(f"{'Model ID':<50} | {'Author':<20} | {'Downloads':<12} | {'Likes':<6}")
        print(f"{'-'*120}")
        
        for model in models:
            model_id = model['model_id'][:48] + ".." if len(model['model_id']) > 50 else model['model_id']
            author = model['author'][:18] + ".." if len(model['author']) > 20 else model['author']
            downloads = model['downloads'] if isinstance(model['downloads'], int) else 'N/A'
            likes = model['likes'] if isinstance(model['likes'], int) else 'N/A'
            
            print(f"{model_id:<50} | {author:<20} | {str(downloads):<12} | {likes:<6}")
        
        print(f"{'='*120}\n")
    
    def save_results(self, models: List[Dict], filename: str) -> None:
        """Save results to JSON file"""
        
        output_data = {
            "timestamp": datetime.now().isoformat(),
            "total_models": len(models),
            "models": models
        }
        
        with open(filename, 'w') as f:
            json.dump(output_data, f, indent=2)
        
        print(f"✅ Saved {len(models)} models to {filename}")


def main():
    parser = argparse.ArgumentParser(description="Query Hugging Face LLMs")
    parser.add_argument(
        "--mode",
        choices=["top", "search", "author"],
        default="top",
        help="Query mode"
    )
    parser.add_argument(
        "--metric",
        choices=["downloads", "likes"],
        default="downloads",
        help="Metric to sort by (for top mode)"
    )
    parser.add_argument(
        "--min-downloads",
        type=int,
        default=0,
        help="Minimum downloads filter"
    )
    parser.add_argument(
        "--min-likes",
        type=int,
        default=0,
        help="Minimum likes filter"
    )
    parser.add_argument(
        "--author",
        type=str,
        default=None,
        help="Filter by author"
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=30,
        help="Limit number of results"
    )
    parser.add_argument(
        "--save",
        type=str,
        default=None,
        help="Save results to JSON file"
    )
    
    args = parser.parse_args()
    
    query = HFLLMQuery()
    models = []
    
    if args.mode == "top":
        models = query.get_top_by_metric(metric=args.metric, limit=args.limit)
        query.display_table(models, f"Top {args.limit} LLMs by {args.metric}")
    
    elif args.mode == "search":
        models = query.search_by_criteria(
            min_downloads=args.min_downloads,
            min_likes=args.min_likes,
            author=args.author,
            limit=args.limit
        )
        query.display_table(models, "Search Results")
    
    elif args.mode == "author":
        if not args.author:
            print("Please provide --author for author search mode")
            return
        models = query.get_models_by_author(author=args.author, limit=args.limit)
        query.display_table(models, f"Models by {args.author}")
    
    if args.save and models:
        query.save_results(models, args.save)


if __name__ == "__main__":
    main()
