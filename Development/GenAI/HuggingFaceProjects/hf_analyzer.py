"""
Hugging Face LLM Model Analyzer
Detailed analysis and comparison of LLM models
"""

from huggingface_hub import list_models
import json
from typing import List, Dict
from datetime import datetime
from collections import defaultdict


class LLMAnalyzer:
    """Analyze and compare LLM models"""
    
    def __init__(self):
        self.models = []
    
    def fetch_all_text_generation_models(self, limit: int = 100) -> List[Dict]:
        """Fetch all text-generation models"""
        
        print(f"📊 Analyzing {limit} text-generation models...\n")
        
        models = list_models(
            filter="text-generation",
            limit=limit,
            full=True
        )
        
        self.models = []
        for model in models:
            model_data = {
                "model_id": model.id,
                "author": getattr(model, 'author', 'Unknown'),
                "downloads": getattr(model, 'downloads', 0) or 0,
                "likes": getattr(model, 'likes', 0) or 0,
                "tags": getattr(model, 'tags', []),
                "private": getattr(model, 'private', False),
                "created_at": str(getattr(model, 'created_at', 'N/A')),
            }
            self.models.append(model_data)
        
        return self.models
    
    def analyze_by_author(self) -> Dict[str, Dict]:
        """Analyze statistics by author"""
        
        author_stats: Dict[str, Dict] = defaultdict(lambda: {
            "count": 0,
            "total_downloads": 0,
            "total_likes": 0,
            "avg_downloads": 0.0,
            "avg_likes": 0.0,
            "models": []
        })
        
        for model in self.models:
            author = model['author']
            stats = author_stats[author]
            stats["count"] += 1
            stats["total_downloads"] += model['downloads']
            stats["total_likes"] += model['likes']
            stats["models"].append(model['model_id'])
        
        # Calculate averages
        for author in author_stats:
            count = author_stats[author]["count"]
            author_stats[author]["avg_downloads"] = float(author_stats[author]["total_downloads"]) / count
            author_stats[author]["avg_likes"] = float(author_stats[author]["total_likes"]) / count
        
        return dict(author_stats)
    
    def get_statistics(self) -> Dict:
        """Get overall statistics"""
        
        if not self.models:
            return {}
        
        downloads = [m['downloads'] for m in self.models]
        likes = [m['likes'] for m in self.models]
        
        stats = {
            "total_models_analyzed": len(self.models),
            "total_downloads": sum(downloads),
            "total_likes": sum(likes),
            "avg_downloads": sum(downloads) / len(downloads) if downloads else 0,
            "avg_likes": sum(likes) / len(likes) if likes else 0,
            "max_downloads": max(downloads) if downloads else 0,
            "min_downloads": min(downloads) if downloads else 0,
            "max_likes": max(likes) if likes else 0,
            "min_likes": min(likes) if likes else 0,
            "unique_authors": len(set(m['author'] for m in self.models)),
            "total_unique_tags": len(set(tag for m in self.models for tag in m['tags']))
        }
        
        return stats
    
    def get_tag_statistics(self) -> Dict[str, int]:
        """Analyze tags across models"""
        
        tag_counts = defaultdict(int)
        
        for model in self.models:
            for tag in model['tags']:
                tag_counts[tag] += 1
        
        return dict(sorted(tag_counts.items(), key=lambda x: x[1], reverse=True))
    
    def display_author_analysis(self, top_n: int = 15) -> None:
        """Display analysis by author"""
        
        author_stats = self.analyze_by_author()
        
        # Sort by model count
        sorted_authors = sorted(
            author_stats.items(),
            key=lambda x: x[1]['total_downloads'],
            reverse=True
        )[:top_n]
        
        print(f"\n{'='*100}")
        print(f"{'Top Authors by Total Downloads':<50}")
        print(f"{'='*100}")
        print(f"{'Author':<25} | {'Models':<8} | {'Avg Downloads':<15} | {'Avg Likes':<10} | {'Total DL':<15}")
        print(f"{'-'*100}")
        
        for author, stats in sorted_authors:
            author_short = author[:23] + ".." if len(author) > 25 else author
            avg_dl = int(stats["avg_downloads"])
            avg_likes = int(stats["avg_likes"])
            total_dl = stats["total_downloads"]
            
            print(f"{author_short:<25} | {stats['count']:<8} | {avg_dl:<15} | {avg_likes:<10} | {total_dl:<15}")
        
        print(f"{'='*100}\n")
    
    def display_statistics(self) -> None:
        """Display overall statistics"""
        
        stats = self.get_statistics()
        
        print(f"\n{'='*80}")
        print(f"{'OVERALL STATISTICS':<80}")
        print(f"{'='*80}")
        
        for key, value in stats.items():
            key_display = key.replace('_', ' ').title()
            if isinstance(value, int):
                print(f"{key_display:<40}: {value:,}")
            else:
                print(f"{key_display:<40}: {value:,.2f}")
        
        print(f"{'='*80}\n")
    
    def display_top_tags(self, top_n: int = 20) -> None:
        """Display most common tags"""
        
        tags = self.get_tag_statistics()
        top_tags = list(tags.items())[:top_n]
        
        print(f"\n{'='*60}")
        print(f"{'Top {0} Tags Across Models':<60}".format(top_n))
        print(f"{'='*60}")
        print(f"{'Tag':<40} | {'Count':<10}")
        print(f"{'-'*60}")
        
        for tag, count in top_tags:
            tag_short = tag[:38] + ".." if len(tag) > 40 else tag
            print(f"{tag_short:<40} | {count:<10}")
        
        print(f"{'='*60}\n")
    
    def save_analysis(self, filename: str) -> None:
        """Save complete analysis to JSON"""
        
        analysis_data = {
            "timestamp": datetime.now().isoformat(),
            "statistics": self.get_statistics(),
            "author_analysis": self.analyze_by_author(),
            "tag_statistics": self.get_tag_statistics(),
            "models": self.models
        }
        
        with open(filename, 'w') as f:
            json.dump(analysis_data, f, indent=2)
        
        print(f"✅ Analysis saved to {filename}")


def main():
    """Main execution"""
    
    analyzer = LLMAnalyzer()
    
    # Fetch models
    analyzer.fetch_all_text_generation_models(limit=200)
    
    # Display analysis
    analyzer.display_statistics()
    analyzer.display_author_analysis(top_n=20)
    analyzer.display_top_tags(top_n=25)
    
    # Save results
    analyzer.save_analysis("llm_analysis.json")


if __name__ == "__main__":
    main()
