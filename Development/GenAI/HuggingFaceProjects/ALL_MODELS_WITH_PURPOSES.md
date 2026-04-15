# 🤖 LLM Models - Purpose & Usage Guide

**Total Models: 200**

This guide explains what each model does and how to use them.

---

## 📚 Model Categories & Purposes

### 1. **Text Generation Models** (Primary Category)
Most models here are **text-generation** models that can:
- Generate coherent text
- Complete sentences or paragraphs
- Answer questions
- Create creative content
- Write code
- Translate text
- Summarize documents

### 2. **Model Size Categories**

**Nano/Mini (< 2B parameters)**
- Purpose: Fast inference, low memory
- Best for: Edge devices, mobile, real-time applications
- Examples: google/gemma-3-270m-it, Qwen/Qwen3-0.6B
- Speed: ⚡⚡⚡ Very Fast
- Quality: ⭐⭐⭐ Decent

**Small (2B - 8B parameters)**
- Purpose: Balanced speed and quality
- Best for: General tasks, local deployment
- Examples: Mistral-7B, Llama-3.2-3B
- Speed: ⚡⚡ Fast
- Quality: ⭐⭐⭐⭐ Good

**Medium (8B - 30B parameters)**
- Purpose: Better reasoning and complex tasks
- Best for: Production applications, research
- Examples: Llama-3.1-8B, Qwen2.5-14B
- Speed: ⚡ Moderate
- Quality: ⭐⭐⭐⭐⭐ Excellent

**Large (30B - 120B parameters)**
- Purpose: Advanced reasoning, complex analysis
- Best for: Enterprise, specialized tasks
- Examples: Llama-3.3-70B, DeepSeek-V3
- Speed: �� Slow (requires GPU)
- Quality: ⭐⭐⭐⭐⭐⭐ Expert-level

---

## 🎯 Popular Models by Use Case

### **For Beginners - Start Here**
- **Qwen/Qwen2.5-7B-Instruct** (12.7M downloads)
  - Purpose: General-purpose conversation and tasks
  - Best for: Learning, experimentation
  - Usage: Easy to run, good quality

- **Meta-Llama/Llama-3.1-8B-Instruct** (7.2M downloads)
  - Purpose: Instruction-following, chat
  - Best for: Friendly models, easy to use
  - Usage: Well-documented, widely supported

- **Mistral-7B** (High popularity)
  - Purpose: General text generation
  - Best for: Fast, reliable baseline
  - Usage: Quick setup and deployment

### **For Code Generation**
- **Qwen/Qwen3-Coder-Next** (Code-focused)
  - Purpose: Write, analyze, debug code
  - Best for: Programming tasks
  - Usage: Trained on code repositories

- **deepseek-ai/deepseek-coder-6.7b-instruct** (6.7B parameters)
  - Purpose: Code generation and understanding
  - Best for: Software development
  - Usage: Specialized for code

- **bigcode/starcoder** (Popular choice)
  - Purpose: Code completion and generation
  - Best for: IDE integration
  - Usage: Multi-language support

### **For Reasoning & Complex Tasks**
- **Qwen/QwQ-32B** (Advanced reasoning)
  - Purpose: Mathematical reasoning, logic
  - Best for: Complex problem-solving
  - Usage: Slower but very accurate

- **DeepSeek-R1** (Reasoning-focused)
  - Purpose: Step-by-step reasoning
  - Best for: Math, science, logic
  - Usage: Chain-of-thought reasoning

- **Meta-Llama/Llama-3.3-70B-Instruct** (Most capable)
  - Purpose: Complex reasoning, analysis
  - Best for: Enterprise applications
  - Usage: Best performance but resource-intensive

### **For Edge/Mobile Deployment**
- **google/gemma-3-270m-it** (270M parameters)
  - Purpose: Ultra-lightweight inference
  - Best for: Mobile, embedded systems
  - Usage: Runs on limited hardware

- **Qwen/Qwen3-0.6B** (600M parameters, 15M downloads)
  - Purpose: Ultra-fast responses
  - Best for: Real-time applications
  - Usage: Minimal memory requirement

- **google/gemma-2-2b-it** (2B parameters)
  - Purpose: Small but capable
  - Best for: Smartphones, IoT devices
  - Usage: Good balance of size/quality

### **For Multilingual Tasks**
- **bigscience/bloom** (Multilingual)
  - Purpose: 46+ languages support
  - Best for: Global applications
  - Usage: Language-agnostic

- **Meta-Llama models**
  - Purpose: Multiple language support
  - Best for: International deployment
  - Usage: Decent multilingual capability

---

## 💡 How to Use These Models

### **Option 1: Via Hugging Face Transformers (Python)**

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load model
model_name = "Qwen/Qwen2.5-7B-Instruct"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Generate text
inputs = tokenizer("Write a poem about coding", return_tensors="pt")
outputs = model.generate(**inputs, max_length=200)
print(tokenizer.decode(outputs[0]))
```

### **Option 2: Via Ollama (Easiest)**

```bash
# Install Ollama from ollama.ai
ollama run llama2
ollama run mistral:7b
ollama run neural-chat
```

### **Option 3: Via LM Studio (GUI)**

1. Download LM Studio from lmstudio.ai
2. Search for a model (e.g., "Mistral 7B")
3. Download and run with one click
4. Use like ChatGPT locally

### **Option 4: Via Hugging Face Inference API**

```python
from huggingface_hub import InferenceClient

client = InferenceClient(model="mistralai/Mistral-7B-Instruct-v0.2")
output = client.text_generation("What is AI?")
print(output)
```

### **Option 5: Via vLLM (Fast Inference)**

```bash
python -m vllm.entrypoints.openai.api_server \
  --model meta-llama/Llama-2-7b-chat-hf
```

---

## 🎓 Model Selection Guide

**Choose based on your needs:**

| Requirement | Best Model | Why |
|------------|-----------|-----|
| **Speed** | Qwen3-0.6B | 600M params = fast |
| **Quality** | Llama-3.3-70B | 70B params = best |
| **Balance** | Qwen2.5-7B | 7B params = good combo |
| **Code** | Qwen3-Coder | Trained on code |
| **Reasoning** | DeepSeek-R1 | Chain-of-thought |
| **Mobile** | Gemma-270M | Ultra-lightweight |
| **Free Tier** | Mistral-7B | Good & popular |
| **Multilingual** | Bloom | 46+ languages |

---

## 📊 Model Statistics


### Top 10 Most Downloaded Models

| Rank | Model | Downloads | Best For |
|------|-------|-----------|----------|
| 1 | Qwen/Qwen3-0.6B | 15,046,236 | General use |
| 2 | openai-community/gpt2 | 13,855,848 | General use |
| 3 | Qwen/Qwen2.5-7B-Instruct | 12,731,921 | General use |
| 4 | Qwen/Qwen2.5-1.5B-Instruct | 10,162,651 | General use |
| 5 | Qwen/Qwen2.5-3B-Instruct | 9,959,750 | General use |
| 6 | deepseek-ai/DeepSeek-V3.2 | 9,952,544 | General use |
| 7 | meta-llama/Llama-3.1-8B-Instruct | 9,429,308 | General use |
| 8 | Qwen/Qwen3-8B | 8,316,099 | General use |
| 9 | Qwen/Qwen3-4B | 7,858,945 | General use |
| 10 | Qwen/Qwen3-1.7B | 7,733,023 | General use |


---

## 🚀 Getting Started Steps

### Step 1: Pick a Model
Based on your use case from the table above.

### Step 2: Choose Installation Method
- **Easiest**: Use Ollama or LM Studio
- **Most Flexible**: Transformers library
- **Most Powerful**: vLLM

### Step 3: Install Dependencies

```bash
# For Transformers
pip install transformers torch

# For Ollama
brew install ollama  # macOS
# Download from ollama.ai (other OS)

# For vLLM
pip install vllm
```

### Step 4: Run Your First Model

```bash
# Option A: Transformers
python3 << 'EOF'
from transformers import pipeline
generator = pipeline("text-generation", model="Qwen/Qwen2.5-7B-Instruct")
result = generator("What is machine learning?")
print(result[0]['generated_text'])
EOF

# Option B: Ollama
ollama run mistral:7b
# Then type your prompt

# Option C: LM Studio
# Download LM Studio → Search "Mistral" → Download → Run
```

---

## 🔧 Advanced Usage Tips

### **Quantization (Make models smaller/faster)**
- 4-bit quantization: Uses 75% less memory
- 8-bit quantization: Uses 50% less memory
- GGUF format: Optimized for CPU inference

### **Prompting Tips**
- Be specific: "Write a Python function to..." (not just "Write code")
- Provide context: Include relevant information
- Use examples: Show what you want
- Chain prompts: Break complex tasks into steps

### **Performance Tips**
- Use smaller models locally
- Use larger models via API for quality
- Cache results for repeated queries
- Use GPU when available (10x faster)

---

## 📝 All 200 Models Reference

Below is the complete list with all metadata:


## Complete Model List

| # | Model ID | Downloads | Likes | Author | Purpose |
|---|----------|-----------|-------|--------|---------|
| 1 | MiniMaxAI/MiniMax-M2.7 | 85,549 | 762 | MiniMaxAI | Text Generation |
| 2 | zai-org/GLM-5.1 | 91,474 | 1,231 | zai-org | Text Generation |
| 3 | Jiunsong/supergemma4-26b-uncensored-gguf-v2 | 26,673 | 276 | Jiunsong | Text Generation |
| 4 | LilaRest/gemma-4-31B-it-NVFP4-turbo | 51,148 | 221 | LilaRest | Text Generation |
| 5 | LGAI-EXAONE/EXAONE-4.5-33B | 6,626 | 140 | LGAI-EXAONE | Text Generation |
| 6 | Jiunsong/supergemma4-26b-uncensored-mlx-4bit-v2 | 6,468 | 126 | Jiunsong | Text Generation |
| 7 | unsloth/MiniMax-M2.7-GGUF | 47,368 | 108 | unsloth | Text Generation |
| 8 | nvidia/Gemma-4-31B-IT-NVFP4 | 908,125 | 390 | nvidia | Text Generation |
| 9 | prism-ml/Bonsai-8B-gguf | 81,238 | 595 | prism-ml | Text Generation |
| 10 | Jackrong/Gemopus-4-26B-A4B-it-GGUF | 29,408 | 73 | Jackrong | Text Generation |
| 11 | unsloth/GLM-5.1-GGUF | 33,954 | 146 | unsloth | Text Generation |
| 12 | douyamv/Gemma-4-31B-JANG_4M-CRACK-GGUF | 101,396 | 105 | douyamv | Text Generation |
| 13 | Ex0bit/Gemma4-26B-A4B-PRISM-PRO-DQ-GGUF | 2,729 | 56 | Ex0bit | Text Generation |
| 14 | z-lab/Qwen3.5-27B-DFlash | 7,751 | 67 | z-lab | Text Generation |
| 15 | kai-os/Carnice-9b | 5,970 | 160 | kai-os | Text Generation |
| 16 | zai-org/GLM-5.1-FP8 | 139,907 | 79 | zai-org | Text Generation |
| 17 | AIDC-AI/Marco-Mini-Instruct | 872 | 37 | AIDC-AI | Text Generation |
| 18 | Qwen/Qwen3-Coder-Next | 659,028 | 1,269 | Qwen | Code Generation |
| 19 | Zigeng/DMax-Coder-16B | 905 | 34 | Zigeng | Code Generation |
| 20 | Rta-AILabs/Nandi-Mini-150M-Instruct | 1,026 | 34 | Rta-AILabs | Text Generation |
| 21 | MiniMaxAI/MiniMax-M2.5 | 851,884 | 1,383 | MiniMaxAI | Text Generation |
| 22 | JANGQ-AI/MiniMax-M2.7-JANGTQ | 1,440 | 30 | JANGQ-AI | Text Generation |
| 23 | microsoft/VibeVoice-1.5B | 106,293 | 2,325 | microsoft | Text Generation |
| 24 | kai-os/gemma4-31b-Opus-4.6-reasoning | 384 | 153 | kai-os | Reasoning |
| 25 | meta-llama/Llama-3.1-8B-Instruct | 9,429,308 | 5,697 | meta-llama | Text Generation |
| 26 | Jiunsong/SuperGemma4-31b-abliterated-GGUF | 427 | 26 | Jiunsong | Text Generation |
| 27 | openai/gpt-oss-120b | 3,497,759 | 4,683 | openai | Text Generation |
| 28 | FINAL-Bench/Darwin-27B-Opus | 59 | 25 | FINAL-Bench | Text Generation |
| 29 | unsloth/Qwen3-Coder-Next-GGUF | 206,757 | 577 | unsloth | Code Generation |
| 30 | AIDC-AI/Marco-Nano-Instruct | 1,840 | 28 | AIDC-AI | Text Generation |
| 31 | nvidia/audio-flamingo-next-hf | 840 | 23 | nvidia | Audio |
| 32 | openai/gpt-oss-20b | 6,101,661 | 4,536 | openai | Text Generation |
| 33 | LGAI-EXAONE/EXAONE-4.5-33B-FP8 | 21,777 | 22 | LGAI-EXAONE | Text Generation |
| 34 | deepseek-ai/DeepSeek-R1 | 3,648,980 | 13,173 | deepseek-ai | Text Generation |
| 35 | FINAL-Bench/Darwin-4B-David | 907 | 21 | FINAL-Bench | Text Generation |
| 36 | Youssofal/MiniMax-M2.7-Abliterated-Heretic-GGUF | 2,251 | 21 | Youssofal | Text Generation |
| 37 | LiquidAI/LFM2.5-350M | 38,701 | 273 | LiquidAI | Text Generation |
| 38 | arcee-ai/Trinity-Large-Thinking | 16,937 | 155 | arcee-ai | Reasoning |
| 39 | tiiuae/Falcon-Perception | 10,113 | 101 | tiiuae | Text Generation |
| 40 | zed-industries/zeta-2 | 2,056 | 134 | zed-industries | Text Generation |
| 41 | cyankiwi/MiniMax-M2.7-AWQ-4bit | 4,296 | 19 | cyankiwi | Text Generation |
| 42 | kai-os/Carnice-27b | 1,693 | 30 | kai-os | Text Generation |
| 43 | deepseek-ai/DeepSeek-V3.2 | 9,952,544 | 1,391 | deepseek-ai | Text Generation |
| 44 | Ex0bit/Gemma4-PRISM-PRO-DQ | 492 | 20 | Ex0bit | Text Generation |
| 45 | kai-os/Carnice-27b-GGUF | 4,748 | 27 | kai-os | Text Generation |
| 46 | unsloth/MiniMax-M2.7 | 1,055 | 16 | unsloth | Text Generation |
| 47 | ubergarm/MiniMax-M2.7-GGUF | 1,910 | 16 | ubergarm | Text Generation |
| 48 | unsloth/gpt-oss-20b-GGUF | 239,188 | 665 | unsloth | Text Generation |
| 49 | tiiuae/Falcon-OCR | 5,222 | 73 | tiiuae | OCR |
| 50 | Rta-AILabs/Nandi-Mini-150M | 10,810 | 118 | Rta-AILabs | Text Generation |
| 51 | khazarai/Qwen3-4B-Qwen3.6-plus-Reasoning-Distilled-GGUF | 30,993 | 21 | khazarai | Reasoning |
| 52 | openai-community/gpt2 | 13,855,848 | 3,198 | openai-community | Text Generation |
| 53 | FINAL-Bench/Darwin-31B-Opus | 1,381 | 33 | FINAL-Bench | Text Generation |
| 54 | Qwen/Qwen2.5-7B-Instruct | 12,731,921 | 1,205 | Qwen | Text Generation |
| 55 | meta-llama/Llama-3.2-3B | 1,093,148 | 748 | meta-llama | Text Generation |
| 56 | google/gemma-3-1b-it | 785,813 | 919 | google | Text Generation |
| 57 | google/functiongemma-270m-it | 38,459 | 971 | google | Text Generation |
| 58 | z-lab/Kimi-K2.5-DFlash | 185 | 17 | z-lab | Text Generation |
| 59 | meta-llama/Llama-3.3-70B-Instruct | 460,519 | 2,703 | meta-llama | Text Generation |
| 60 | Qwen/Qwen3-4B-Instruct-2507 | 7,096,367 | 809 | Qwen | Text Generation |
| 61 | prism-ml/Bonsai-8B-mlx-1bit | 42,680 | 172 | prism-ml | Text Generation |
| 62 | Ex0bit/MYTHOS-26B-A4B-PRISM-PRO-DQ-MLX | 239 | 12 | Ex0bit | Text Generation |
| 63 | meta-llama/Llama-3.1-8B | 1,418,878 | 2,152 | meta-llama | Text Generation |
| 64 | Qwen/Qwen3-0.6B | 15,046,236 | 1,189 | Qwen | Text Generation |
| 65 | Qwen/Qwen3-Embedding-8B | 1,764,939 | 652 | Qwen | Embeddings |
| 66 | unsloth/Qwen3-Coder-30B-A3B-Instruct-GGUF | 143,928 | 589 | unsloth | Code Generation |
| 67 | lightonai/LightOnOCR-2-1B | 721,765 | 654 | lightonai | OCR |
| 68 | stepfun-ai/Step-3.5-Flash | 136,878 | 777 | stepfun-ai | Text Generation |
| 69 | litert-community/functiongemma-270m-ft-mobile-actions | 260 | 34 | litert-community | Text Generation |
| 70 | z-lab/Qwen3.5-35B-A3B-DFlash | 3,042 | 28 | z-lab | Text Generation |
| 71 | rednote-hilab/dots.mocr | 102,990 | 99 | rednote-hilab | OCR |
| 72 | bigatuna/Qwen3.5-9b-Sushi-Coder-RL-GGUF | 18,257 | 48 | bigatuna | Code Generation |
| 73 | TrevorJS/gemma-4-26B-A4B-it-uncensored-GGUF | 37,471 | 24 | TrevorJS | Text Generation |
| 74 | 0xSero/gemma-4-21b-a4b-it-REAP | 4,727 | 86 | 0xSero | Text Generation |
| 75 | JANGQ-AI/MiniMax-M2.7-JANG_2L | 2,587 | 11 | JANGQ-AI | Text Generation |
| 76 | flwrlabs/Lizzy-7B | 36 | 11 | flwrlabs | Text Generation |
| 77 | Jiunsong/SuperGemma4-31b-abliterated-mlx-4bit | 145 | 11 | Jiunsong | Text Generation |
| 78 | Qwen/Qwen2.5-1.5B-Instruct | 10,162,651 | 668 | Qwen | Text Generation |
| 79 | Qwen/Qwen3-8B | 8,316,099 | 1,040 | Qwen | Text Generation |
| 80 | Qwen/Qwen3-Embedding-0.6B | 6,091,508 | 979 | Qwen | Embeddings |
| 81 | dphn/Dolphin-Mistral-24B-Venice-Edition | 84,266 | 484 | dphn | Text Generation |
| 82 | ByteDance/Ouro-2.6B-Thinking | 5,348 | 113 | ByteDance | Reasoning |
| 83 | nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16 | 517,997 | 330 | nvidia | Text Generation |
| 84 | nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4 | 1,574,893 | 266 | nvidia | Text Generation |
| 85 | Tesslate/OmniCoder-9B | 28,561 | 580 | Tesslate | Code Generation |
| 86 | kai-os/Carnice-9b-GGUF | 8,010 | 38 | kai-os | Text Generation |
| 87 | DJLougen/Harmonic-27B-GGUF | 2,964 | 36 | DJLougen | Text Generation |
| 88 | ConicCat/Gemma4-Garnet-31B | 538 | 11 | ConicCat | Text Generation |
| 89 | mistralai/Mistral-7B-v0.1 | 850,307 | 4,073 | mistralai | Text Generation |
| 90 | google/gemma-2-2b-it | 365,022 | 1,333 | google | Text Generation |
| 91 | meta-llama/Llama-3.2-1B-Instruct | 4,297,346 | 1,364 | meta-llama | Text Generation |
| 92 | zai-org/GLM-4.7-Flash | 747,632 | 1,665 | zai-org | Text Generation |
| 93 | Jackrong/Qwen3.5-4B-Claude-4.6-Opus-Reasoning-Distilled-GGUF | 304,418 | 102 | Jackrong | Reasoning |
| 94 | chromadb/context-1 | 4,451 | 386 | chromadb | Text Generation |
| 95 | mudler/Qwen3.5-35B-A3B-APEX-GGUF | 116,749 | 81 | mudler | Text Generation |
| 96 | ubergarm/GLM-5.1-GGUF | 9,624 | 20 | ubergarm | Text Generation |
| 97 | JANGQ-AI/MiniMax-M2.7-JANG_3L | 1,977 | 9 | JANGQ-AI | Text Generation |
| 98 | ginigen-ai/Rogue-27B-KR | 914 | 9 | ginigen-ai | Text Generation |
| 99 | mistralai/Mistral-7B-Instruct-v0.2 | 2,261,796 | 3,117 | mistralai | Text Generation |
| 100 | meta-llama/Meta-Llama-3-8B-Instruct | 1,302,422 | 4,472 | meta-llama | Text Generation |
| 101 | meta-llama/Meta-Llama-3-8B | 3,221,335 | 6,514 | meta-llama | Text Generation |
| 102 | meta-llama/Llama-3.2-3B-Instruct | 5,154,556 | 2,093 | meta-llama | Text Generation |
| 103 | Qwen/Qwen3-Coder-30B-A3B-Instruct | 1,670,748 | 1,008 | Qwen | Code Generation |
| 104 | nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16 | 1,595,562 | 712 | nvidia | Text Generation |
| 105 | zai-org/GLM-5 | 496,760 | 1,978 | zai-org | Text Generation |
| 106 | Jackrong/Qwen3.5-35B-A3B-Claude-4.6-Opus-Reasoning-Distilled | 50,642 | 121 | Jackrong | Reasoning |
| 107 | OpenMOSS-Team/moss-video-preview-realtime-sft | 153 | 12 | OpenMOSS-Team | Text Generation |
| 108 | nvidia/Nemotron-Cascade-2-30B-A3B | 315,229 | 473 | nvidia | Text Generation |
| 109 | bartowski/MiniMaxAI_MiniMax-M2.7-GGUF | 8,358 | 8 | bartowski | Text Generation |
| 110 | meta-llama/Llama-2-7b-chat-hf | 434,665 | 4,733 | meta-llama | Text Generation |
| 111 | xai-org/grok-1 | 154 | 2,405 | xai-org | Text Generation |
| 112 | Qwen/Qwen3-4B | 7,858,945 | 596 | Qwen | Text Generation |
| 113 | Qwen/Qwen3-8B-GGUF | 53,630 | 181 | Qwen | Text Generation |
| 114 | saricles/Qwen3-Coder-Next-NVFP4-GB10 | 13,784 | 22 | saricles | Code Generation |
| 115 | sarvamai/sarvam-105b | 20,209 | 259 | sarvamai | Text Generation |
| 116 | z-lab/Qwen3.5-9B-DFlash | 5,569 | 20 | z-lab | Text Generation |
| 117 | unsloth/NVIDIA-Nemotron-3-Super-120B-A12B-GGUF | 81,977 | 112 | unsloth | Text Generation |
| 118 | OpenMOSS-Team/moss-video-preview-base | 45 | 9 | OpenMOSS-Team | Text Generation |
| 119 | prism-ml/Bonsai-4B-gguf | 10,451 | 33 | prism-ml | Text Generation |
| 120 | squ11z1/claude-oss | 1,848 | 10 | squ11z1 | Text Generation |
| 121 | TrevorJS/gemma-4-E4B-it-uncensored-GGUF | 26,784 | 17 | TrevorJS | Text Generation |
| 122 | yifanyu/I-DLM-8B | 654 | 7 | yifanyu | Text Generation |
| 123 | Jackrong/Gemopus-4-26B-A4B-it | 1,523 | 7 | Jackrong | Text Generation |
| 124 | coder3101/gemma-4-21b-a4b-it-REAP-heretic | 749 | 7 | coder3101 | Code Generation |
| 125 | FINAL-Bench/Darwin-4B-Genesis | 477 | 7 | FINAL-Bench | Text Generation |
| 126 | mlx-community/MiniMax-M2.7-4bit-mxfp4 | 2,690 | 7 | mlx-community | Text Generation |
| 127 | Qwen/Qwen2.5-Coder-7B-Instruct | 1,901,175 | 685 | Qwen | Code Generation |
| 128 | Qwen/Qwen2.5-3B-Instruct | 9,959,750 | 440 | Qwen | Text Generation |
| 129 | meta-llama/Llama-3.2-1B | 1,239,214 | 2,359 | meta-llama | Text Generation |
| 130 | deepseek-ai/DeepSeek-V3 | 763,571 | 4,031 | deepseek-ai | Text Generation |
| 131 | deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B | 710,017 | 1,474 | deepseek-ai | Text Generation |
| 132 | Qwen/QwQ-32B | 71,657 | 2,892 | Qwen | Text Generation |
| 133 | litert-community/Gemma3-1B-IT | 18,598 | 567 | litert-community | Text Generation |
| 134 | DeepHat/DeepHat-V1-7B | 11,959 | 130 | DeepHat | Text Generation |
| 135 | Qwen/Qwen3-1.7B | 7,733,023 | 446 | Qwen | Text Generation |
| 136 | mlx-community/gpt-oss-20b-MXFP4-Q8 | 593,534 | 47 | mlx-community | Text Generation |
| 137 | moondream/moondream3-preview | 8,095 | 608 | moondream | Vision |
| 138 | LiquidAI/LFM2-8B-A1B | 62,977 | 351 | LiquidAI | Text Generation |
| 139 | TeichAI/Qwen3-14B-Claude-4.5-Opus-High-Reasoning-Distill-GGUF | 45,748 | 312 | TeichAI | Reasoning |
| 140 | XiaomiMiMo/MiMo-V2-Flash | 62,620 | 710 | XiaomiMiMo | Text Generation |
| 141 | unsloth/GLM-4.7-Flash-GGUF | 126,516 | 601 | unsloth | Text Generation |
| 142 | Qwen/Qwen3-Coder-Next-FP8 | 884,263 | 132 | Qwen | Code Generation |
| 143 | unsloth/MiniMax-M2.5-GGUF | 81,713 | 227 | unsloth | Text Generation |
| 144 | Jackrong/Qwen3.5-2B-Claude-4.6-Opus-Reasoning-Distilled-GGUF | 70,153 | 147 | Jackrong | Reasoning |
| 145 | nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-FP8 | 952,737 | 230 | nvidia | Text Generation |
| 146 | Multilingual-Multimodal-NLP/IndustrialCoder | 1,595 | 57 | Multilingual-Multimodal-NLP | Code Generation |
| 147 | llm-jp/llm-jp-4-8b-thinking | 24,643 | 27 | llm-jp | Reasoning |
| 148 | llm-jp/llm-jp-4-32b-a3b-thinking | 7,032 | 22 | llm-jp | Reasoning |
| 149 | timteh673/Qwen3.5-397B-A17B-Opus-4.6-Reasoning-Uncensored-GGUF | 6,250 | 11 | timteh673 | Reasoning |
| 150 | AIDC-AI/Marco-Nano-Base | 465 | 12 | AIDC-AI | Text Generation |
| 151 | TrevorJS/gemma-4-E4B-it-uncensored | 3,211 | 9 | TrevorJS | Text Generation |
| 152 | TrevorJS/gemma-4-26B-A4B-it-uncensored | 4,705 | 20 | TrevorJS | Text Generation |
| 153 | deadbydawn101/gemma-4-E4B-Agentic-Opus-Reasoning-GeminiCLI-mlx-4bit | 7,624 | 11 | deadbydawn101 | Reasoning |
| 154 | nvidia/audio-flamingo-next-captioner-hf | 220 | 6 | nvidia | Audio |
| 155 | tokinasin/llm-jp-4-8b-instruct-uncensored-ara | 167 | 6 | tokinasin | Text Generation |
| 156 | bigscience/bloom | 5,903 | 4,998 | bigscience | Text Generation |
| 157 | deepseek-ai/DeepSeek-R1-Distill-Llama-70B | 153,300 | 767 | deepseek-ai | Text Generation |
| 158 | deepseek-ai/DeepSeek-R1-Distill-Qwen-7B | 600,275 | 807 | deepseek-ai | Text Generation |
| 159 | moonshotai/Kimi-K2-Instruct | 200,716 | 2,336 | moonshotai | Text Generation |
| 160 | google/gemma-3-270m-it | 124,209 | 577 | google | Text Generation |
| 161 | unsloth/gpt-oss-120b-GGUF | 203,369 | 242 | unsloth | Text Generation |
| 162 | deepseek-ai/DeepSeek-V3.2-Speciale | 19,096 | 694 | deepseek-ai | Text Generation |
| 163 | ArliAI/GLM-4.6-Derestricted-v3 | 1,528 | 59 | ArliAI | Text Generation |
| 164 | MiniMaxAI/MiniMax-M2.1 | 37,137 | 1,276 | MiniMaxAI | Text Generation |
| 165 | Nanbeige/Nanbeige4.1-3B | 335,677 | 1,034 | Nanbeige | Text Generation |
| 166 | RedHatAI/Qwen3-Coder-Next-NVFP4 | 16,506 | 20 | RedHatAI | Code Generation |
| 167 | sarvamai/sarvam-30b | 26,932 | 185 | sarvamai | Text Generation |
| 168 | z-lab/Qwen3.5-4B-DFlash | 4,680 | 14 | z-lab | Text Generation |
| 169 | mconcat/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-NVFP4 | 27,157 | 46 | mconcat | Reasoning |
| 170 | nvidia/MiniMax-M2.5-NVFP4 | 43,111 | 26 | nvidia | Text Generation |
| 171 | dealignai/MiniMax-M2.5-UNCENSORED-JANG_2L | 1,652 | 7 | dealignai | Text Generation |
| 172 | prism-ml/Bonsai-1.7B-gguf | 14,100 | 46 | prism-ml | Text Generation |
| 173 | Jackrong/MLX-Qwopus3.5-9B-v3-4bit | 7,372 | 22 | Jackrong | Text Generation |
| 174 | VillanovaAI/Villanova-2B-2603 | 2,020 | 5 | VillanovaAI | Text Generation |
| 175 | tokenaii/horus | 853 | 10 | tokenaii | Text Generation |
| 176 | TrevorJS/gemma-4-E2B-it-uncensored-GGUF | 22,104 | 20 | TrevorJS | Text Generation |
| 177 | TrevorJS/gemma-4-31B-it-uncensored | 3,097 | 11 | TrevorJS | Text Generation |
| 178 | TrevorJS/gemma-4-31B-it-uncensored-GGUF | 17,070 | 18 | TrevorJS | Text Generation |
| 179 | caiovicentino1/Huihui-Qwopus3.5-27B-v3-abliterated-HLWQ-Q5 | 2,407 | 14 | caiovicentino1 | Text Generation |
| 180 | Jackrong/Qwopus3.5-27B-v3-FP8-vllm-ready | 7,709 | 12 | Jackrong | Text Generation |
| 181 | learning-unit/L1-16B-A3B | 909 | 5 | learning-unit | Text Generation |
| 182 | bartowski/zai-org_GLM-5.1-GGUF | 6,569 | 5 | bartowski | Text Generation |
| 183 | caiovicentino1/Qwopus3.5-27B-v3-HLWQ-v7-GPTQ | 667 | 5 | caiovicentino1 | Text Generation |
| 184 | YTan2000/Qwopus3.5-27B-v3-Abliterated-TQ3_4S | 1,014 | 5 | YTan2000 | Text Generation |
| 185 | dealignai/MiniMax-M2.7-JANG_2L-CRACK | 911 | 5 | dealignai | Text Generation |
| 186 | facebook/opt-125m | 6,617,583 | 243 | facebook | Text Generation |
| 187 | bigcode/starcoder | 10,667 | 2,940 | bigcode | Code Generation |
| 188 | meta-llama/Llama-2-7b | 281 | 4,473 | meta-llama | Text Generation |
| 189 | HuggingFaceH4/zephyr-7b-beta | 113,211 | 1,840 | HuggingFaceH4 | Text Generation |
| 190 | deepseek-ai/deepseek-coder-6.7b-instruct | 124,554 | 490 | deepseek-ai | Code Generation |
| 191 | microsoft/phi-2 | 1,142,987 | 3,446 | microsoft | Text Generation |
| 192 | google/gemma-2b | 158,764 | 1,163 | google | Text Generation |
| 193 | meta-llama/Llama-Guard-3-8B | 122,699 | 288 | meta-llama | Safety |
| 194 | Qwen/Qwen2.5-14B-Instruct-AWQ | 1,918,451 | 33 | Qwen | Text Generation |
| 195 | HuggingFaceTB/SmolLM2-135M-Instruct | 872,750 | 306 | HuggingFaceTB | Text Generation |
| 196 | livekit/turn-detector | 398,146 | 97 | livekit | Text Generation |
| 197 | bartowski/DeepSeek-R1-Distill-Qwen-7B-GGUF | 38,226 | 115 | bartowski | Text Generation |
| 198 | AlicanKiraz0/Cybersecurity-BaronLLM_Offensive_Security_LLM_Q6_K_GGUF | 1,462 | 209 | AlicanKiraz0 | Text Generation |
| 199 | microsoft/Phi-4-mini-instruct | 1,131,785 | 714 | microsoft | Text Generation |
| 200 | deepseek-ai/DeepSeek-V3-0324 | 569,063 | 3,101 | deepseek-ai | Text Generation |
