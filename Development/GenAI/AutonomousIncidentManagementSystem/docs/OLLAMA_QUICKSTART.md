# Quick Start: AIMS with Ollama (Free LLM)

## 🚀 Get Started in 5 Minutes

### Step 1: Install Ollama (2 min)
```bash
# Download from: https://ollama.ai
# Mac: Download and run installer
# Linux: Download binary or use Docker

# Verify installation:
curl http://localhost:11434/api/tags
```

### Step 2: Pull a Model (1-2 min)
```bash
# Recommended: Mistral (fast, accurate, 4GB)
ollama pull mistral

# Alternative options:
ollama pull neural-chat      # Faster
ollama pull orca-mini        # Lightweight
```

### Step 3: Start Your System (1 min)
```bash
cd /Users/deb/Development/GenAI/AutonomousIncidentManagementSystem

# Config is already set for Ollama
cp backend/.env.template backend/.env

# Start everything
docker compose up --build
```

### Step 4: Open Dashboard (1 min)
```
Browser: http://localhost:3000
```

## ✅ What You Get

| Feature | With Ollama | With OpenAI |
|---------|------------|-----------|
| Cost | $0 | $0.03-0.06/1K tokens |
| Privacy | 100% Local | Cloud |
| Speed | ⚡ Fast | ⚡ Fast |
| Model | Mistral 7B | GPT-4 |
| Setup | 5 minutes | API key required |

## 🎯 Features Ready to Use

✅ **Dashboard**
- Real-time system health
- Alert statistics
- Incident tracking

✅ **Alerts Management**
- Create and track alerts
- AI-powered correlation
- Deduplication

✅ **Incidents**
- Incident lifecycle
- Root cause analysis (AI)
- Recommendations (AI)

## 🔧 Configuration

The system is pre-configured in `.env.template`:

```env
LLM_PROVIDER=ollama
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=mistral
```

### Want to Switch Models?

Edit `backend/.env`:
```bash
# Fast & lightweight
OLLAMA_MODEL=neural-chat

# More powerful
OLLAMA_MODEL=dolphin-mixtral

# Lightweight (2GB)
OLLAMA_MODEL=orca-mini
```

Then restart: `docker compose restart backend`

## 🐛 Troubleshooting

**Q: "Connection refused"**
A: Make sure Ollama is running:
```bash
curl http://localhost:11434/api/tags
# If empty, run: ollama serve
```

**Q: "Model not found"**
A: Pull it first:
```bash
ollama pull mistral
```

**Q: "Slow responses"**
A: Use lighter model:
```env
OLLAMA_MODEL=neural-chat
```

**Q: "Out of memory"**
A: Check available RAM, use smaller model

## 📚 More Information

For detailed setup, model comparisons, and advanced configuration, see:
- `OLLAMA_SETUP.md` - Complete setup guide
- `HUGGINGFACE_DEPLOYMENT.md` - Cloud deployment
- `README.md` - Full documentation

## 🎉 You're All Set!

Enjoy free incident management with no API costs! 🚀

For questions:
1. Check `OLLAMA_SETUP.md`
2. Visit https://ollama.ai
3. Read Ollama docs: https://github.com/ollama/ollama

Happy incident management! 💻✨
