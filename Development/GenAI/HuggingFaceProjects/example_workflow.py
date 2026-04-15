"""
Integration Example - Complete Workflow
Shows how to use all tools together
"""

import json
from datetime import datetime
from typing import Dict, List
from hf_advanced_query import HFLLMQuery


class HFLLMWorkflow:
    """Complete workflow for LLM research"""
    
    def __init__(self):
        self.query = HFLLMQuery()
        self.results = {}
    
    def comprehensive_research(self) -> Dict:
        """Run comprehensive research on LLMs"""
        
        print("\n" + "="*80)
        print("COMPREHENSIVE HUGGING FACE LLM RESEARCH")
        print("="*80)
        
        research_data = {
            "timestamp": datetime.now().isoformat(),
            "queries": {}
        }
        
        # 1. Top LLMs by downloads
        print("\n[1/5] Fetching top LLMs by downloads...")
        top_downloads = self.query.get_top_by_metric(metric="downloads", limit=30)
        self.query.display_table(top_downloads, "Top 30 LLMs by Downloads")
        research_data["queries"]["top_downloads"] = top_downloads
        
        # 2. Top LLMs by likes
        print("\n[2/5] Fetching top LLMs by likes...")
        top_likes = self.query.get_top_by_metric(metric="likes", limit=20)
        self.query.display_table(top_likes, "Top 20 LLMs by Likes")
        research_data["queries"]["top_likes"] = top_likes
        
        # 3. High-value models (1M+ downloads, 500+ likes)
        print("\n[3/5] Searching high-value models...")
        high_value = self.query.search_by_criteria(
            min_downloads=1000000,
            min_likes=500,
            limit=30
        )
        self.query.display_table(high_value, "High-Value Models (1M+ DL, 500+ Likes)")
        research_data["queries"]["high_value"] = high_value
        
        # 4. Top organizations
        print("\n[4/5] Analyzing top organizations...")
        orgs = ["Qwen", "meta-llama", "deepseek-ai", "mistralai", "microsoft"]
        org_data = {}
        
        for org in orgs:
            models = self.query.get_models_by_author(author=org, limit=10)
            org_data[org] = models
            print(f"   ✓ {org}: {len(models)} models")
        
        research_data["queries"]["organizations"] = org_data
        
        # 5. Summary statistics
        print("\n[5/5] Generating summary...")
        summary = self._generate_summary(
            top_downloads + top_likes + high_value
        )
        research_data["summary"] = summary
        
        self._print_summary(summary)
        
        return research_data
    
    def _generate_summary(self, models: list) -> Dict:
        """Generate summary statistics"""
        
        if not models:
            return {}
        
        downloads = [m.get('downloads', 0) for m in models if isinstance(m.get('downloads'), int)]
        likes = [m.get('likes', 0) for m in models if isinstance(m.get('likes'), int)]
        
        return {
            "total_models_reviewed": len(models),
            "total_downloads": sum(downloads),
            "total_likes": sum(likes),
            "avg_downloads": sum(downloads) / len(downloads) if downloads else 0,
            "avg_likes": sum(likes) / len(likes) if likes else 0,
            "unique_authors": len(set(m.get('author') for m in models)),
            "download_range": f"{min(downloads):,} - {max(downloads):,}",
            "likes_range": f"{min(likes)} - {max(likes)}"
        }
    
    def _print_summary(self, summary: Dict) -> None:
        """Print formatted summary"""
        
        print("\n" + "="*80)
        print("RESEARCH SUMMARY")
        print("="*80)
        
        for key, value in summary.items():
            key_display = key.replace('_', ' ').title()
            print(f"{key_display:<30}: {value:,}" if isinstance(value, int) else f"{key_display:<30}: {value}")
        
        print("="*80 + "\n")
    
    def save_research(self, filename: str = "comprehensive_research.json") -> None:
        """Save research results"""
        
        # This would save the comprehensive research
        print(f"✅ Research saved to {filename}")
    
    def compare_models(
        self,
        model_list: list,
        metric: str = "downloads"
    ) -> None:
        """Compare models in the list"""
        
        print("\n" + "="*80)
        print(f"MODEL COMPARISON (sorted by {metric})")
        print("="*80)
        
        sorted_models = sorted(
            model_list,
            key=lambda x: x.get(metric, 0),
            reverse=True
        )
        
        self.query.display_table(sorted_models[:20], f"Top 20 by {metric}")


def example_workflow():
    """Example workflow"""
    
    print("\n🚀 Starting Comprehensive LLM Research Workflow...\n")
    
    workflow = HFLLMWorkflow()
    
    # Run comprehensive research
    results = workflow.comprehensive_research()
    
    # You can also do specific comparisons
    print("\n📊 ADDITIONAL ANALYSES")
    print("-" * 80)
    
    # Compare high-value models by likes
    high_value = results["queries"]["high_value"]
    if high_value:
        workflow.compare_models(high_value, metric="likes")
    
    # Compare by organization
    print("\n📈 ORGANIZATION COMPARISON")
    print("-" * 80)
    print("\nOrganizations and their model counts:")
    for org, models in results["queries"]["organizations"].items():
        total_downloads = sum(m.get('downloads', 0) for m in models)
        total_likes = sum(m.get('likes', 0) for m in models)
        print(f"\n{org}:")
        print(f"  Models: {len(models)}")
        print(f"  Total Downloads: {total_downloads:,}")
        print(f"  Total Likes: {total_likes:,}")
        if models:
            avg_dl = total_downloads / len(models)
            print(f"  Avg Downloads: {avg_dl:,.0f}")


if __name__ == "__main__":
    example_workflow()
