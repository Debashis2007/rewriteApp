"""
Hugging Face Model Downloader
Download and manage LLM models locally
"""

import os
import json
from huggingface_hub import hf_hub_download, snapshot_download
from typing import List, Dict, Optional
from pathlib import Path


class ModelDownloader:
    """Download and manage Hugging Face models"""
    
    def __init__(self, cache_dir: str = "./models"):
        self.cache_dir = cache_dir
        Path(cache_dir).mkdir(parents=True, exist_ok=True)
    
    def download_model(
        self,
        model_id: str,
        revision: str = "main"
    ) -> str:
        """Download a complete model"""
        
        print(f"\n📥 Downloading {model_id}...")
        print(f"   Revision: {revision}")
        print(f"   Cache dir: {self.cache_dir}\n")
        
        try:
            local_dir = snapshot_download(
                repo_id=model_id,
                revision=revision,
                cache_dir=self.cache_dir,
                allow_patterns=["*.safetensors", "*.json", "*.py", "*.md"],
                ignore_patterns=["*.msgpack", "*.h5"]
            )
            
            print(f"✅ Model downloaded successfully to: {local_dir}")
            return local_dir
        
        except Exception as e:
            print(f"❌ Error downloading model: {str(e)}")
            return ""
    
    def download_specific_file(
        self,
        model_id: str,
        filename: str,
        revision: str = "main"
    ) -> Optional[str]:
        """Download a specific file from model"""
        
        print(f"\n📥 Downloading {filename} from {model_id}...")
        
        try:
            file_path = hf_hub_download(
                repo_id=model_id,
                filename=filename,
                revision=revision,
                cache_dir=self.cache_dir
            )
            
            print(f"✅ File downloaded to: {file_path}")
            return file_path
        
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            return None
    
    def list_downloaded_models(self) -> List[str]:
        """List all downloaded models"""
        
        models = []
        
        if os.path.exists(self.cache_dir):
            for item in os.listdir(self.cache_dir):
                item_path = os.path.join(self.cache_dir, item)
                if os.path.isdir(item_path):
                    models.append(item)
        
        return models
    
    def get_model_info(self, model_id: str) -> Dict:
        """Get model information"""
        
        from huggingface_hub import model_info
        
        try:
            info = model_info(model_id)
            return {
                "model_id": info.model_id,
                "created_at": str(info.created_at),
                "last_modified": str(info.last_modified),
                "private": info.private,
                "gated": info.gated,
                "downloads": info.downloads,
                "likes": info.likes,
                "tags": info.tags,
            }
        except Exception as e:
            print(f"Error getting model info: {e}")
            return {}
    
    def estimate_disk_space(self, model_id: str) -> str:
        """Estimate disk space needed"""
        
        info = self.get_model_info(model_id)
        
        if not info:
            return "Unknown"
        
        # Rough estimate based on model type
        # Most LLMs range from 500MB to 50GB
        try:
            from huggingface_hub import list_files_to_download
            
            files = list_files_to_download(model_id)
            total_size = sum(f.size for f in files if hasattr(f, 'size'))
            
            if total_size < 1e9:
                return f"{total_size / 1e6:.0f} MB"
            else:
                return f"{total_size / 1e9:.1f} GB"
        except:
            return "Estimate unavailable"


def main():
    """Example usage"""
    
    downloader = ModelDownloader(cache_dir="./hf_models")
    
    # Example models to download
    example_models = [
        "distilbert/distilgpt2",
        "gpt2",
    ]
    
    print("\n" + "="*80)
    print("HUGGING FACE MODEL DOWNLOADER EXAMPLES")
    print("="*80)
    
    for model_id in example_models:
        print(f"\n📊 Model: {model_id}")
        print("-" * 80)
        
        # Get model info
        info = downloader.get_model_info(model_id)
        if info:
            print(f"   Downloads: {info.get('downloads', 'N/A')}")
            print(f"   Likes: {info.get('likes', 'N/A')}")
            print(f"   Created: {info.get('created_at', 'N/A')}")
        
        # Estimate space
        space = downloader.estimate_disk_space(model_id)
        print(f"   Est. Size: {space}")
    
    print("\n" + "="*80)
    print("USAGE EXAMPLES")
    print("="*80)
    print("""
# Download entire model
from hf_model_downloader import ModelDownloader

downloader = ModelDownloader("./my_models")
local_path = downloader.download_model("meta-llama/Llama-2-7b")

# Download specific file
config_path = downloader.download_specific_file(
    "meta-llama/Llama-2-7b",
    "config.json"
)

# List downloaded models
models = downloader.list_downloaded_models()
print(f"Downloaded: {models}")

# Get model info
info = downloader.get_model_info("meta-llama/Llama-2-7b")
print(f"Model info: {info}")
    """)


if __name__ == "__main__":
    main()
