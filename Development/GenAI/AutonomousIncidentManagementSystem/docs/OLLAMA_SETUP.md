# Ollama Setup Guide

Your Autonomous Incident Management System now uses **Ollama** - a free, local LLM that runs on your machine!

## What is Ollama?

Ollama is a lightweight framework for running large language models locally. It's:
- ✅ **Free** - No API costs
- ✅ **Local** - Runs on your machine
- ✅ **Fast** - For incident management tasks
- ✅ **Private** - Your data stays local
- ✅ **Flexible** - Multiple models supported

## Installation

### 1. Download Ollama
Visit: https://ollama.ai

Download and install for:
- **Mac**: `ollama-darwin.zip` (Apple Silicon or Intel)
- **Linux**: Standalone binary or Docker
- **Windows**: Coming soon (use WSL2 or Docker)

### 2. Start Ollama
```bash
# After installation, Ollama runs as a service
# On Mac: Just open the app
# On Linux: Run the binary or docker

# Verify it's running:
curl http://localhost:11434/api/tags
```

### 3. Pull a Model
```bash
# Pull Mistral (recommended - fast & accurate)
ollama pull mistral

# Or try other models:
ollama pull neural-chat      # Fast, good for chat
ollama pull dolphin-mixtral  # More creative
ollama pull llama2           # Meta's open model
ollama pull orca-mini        # Lightweight
```

Model sizes:
- **Mistral** (7B): ~4GB - Great for incident management
- **Neural-chat** (7B): ~4GB - Good at instructions
- **Dolphin-mixtral** (8x7B): ~45GB - More powerful but slower
- **Llama2** (13B): ~7GB - General purpose
- **Orca-mini** (3B): ~2GB - Lightweight (slower)

## Configuration

The system is already configured for Ollama in `.env.template`:

```env
LLM_PROVIDER=ollama
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=mistral
OLLAMA_TEMPERATURE=0.7
OLLAMA_NUM_PREDICT=2048
```

### Setting Your Model

Edit `backend/.env`:

```bash
# Use different models
OLLAMA_MODEL=mistral              # Default (4GB)
OLLAMA_MODEL=neural-chat          # Fast & good
OLLAMA_MODEL=dolphin-mixtral      # More powerful
OLLAMA_MODEL=orca-mini            # Lightweight
```

## Running the System

### 1. Start Ollama
```bash
# On Mac: Click the Ollama app icon
# On Linux: Run the binary
# Verify: curl http://localhost:11434/api/tags
```

### 2. Start Your AIMS System
```bash
cd /Users/deb/Development/GenAI/AutonomousIncidentManagementSystem

# Copy environment config (already set for Ollama)
cp backend/.env.template backend/.env

# Start with Docker Compose
docker compose up --build

# Frontend: http://localhost:3000
# Backend: http://localhost:8001
```

### 3. Test the System
```bash
# In the browser, go to:
http://localhost:3000

# Test the API:
curl http://localhost:8001/api/v1/health
```

## How It Works

### Alert Analysis
When alerts come in, the system:
1. Sends alert data to Ollama via HTTP
2. Ollama runs Mistral locally
3. Gets correlation analysis
4. No external API calls, no costs!

### Incident Analysis
For incident classification, RCA, and recommendations:
1. System prepares the incident prompt
2. Sends to Ollama endpoint
3. Mistral processes locally
4. Results returned immediately

## Performance & Tuning

### Parameters You Can Adjust

```env
# Temperature (0.0-1.0)
OLLAMA_TEMPERATURE=0.7
# Lower = more focused, Higher = more creative

# Max tokens (max response length)
OLLAMA_NUM_PREDICT=2048
# Lower = faster responses

# Model choice
OLLAMA_MODEL=mistral
# Switch models without code changes
```

### Performance Tips

1. **Use smaller models for speed**: `neural-chat` or `orca-mini`
2. **Use larger models for accuracy**: `dolphin-mixtral` or `llama2`
3. **Adjust temperature**: 0.3 for analysis, 0.7 for creativity
4. **Monitor memory**: Check `ollama logs` if it's slow
5. **Use GPU**: If available, Ollama uses it automatically

## Troubleshooting

### Ollama Not Responding
```bash
# Check if running
curl http://localhost:11434/api/tags

# Check logs (Mac)
log stream --predicate 'process == "Ollama"'

# Restart Ollama
# Kill process and restart the app
```

### Model Not Pulled
```bash
# List available models
ollama list

# Pull the model
ollama pull mistral

# Verify
curl http://localhost:11434/api/tags
```

### Slow Responses
```bash
# Check available memory
free -h

# Switch to lighter model
OLLAMA_MODEL=orca-mini

# Or increase resources:
# Stop Ollama, then give more CPU/RAM, restart
```

### Connection Refused
```bash
# Check if Ollama is running
ps aux | grep ollama

# Check port 11434 is open
lsof -i :11434

# Start Ollama
ollama serve

# Or on Mac:
open /Applications/Ollama.app
```

## Switching Back to OpenAI/Anthropic

If you want to use paid APIs:

1. Update `.env`:
```env
LLM_PROVIDER=openai
OPENAI_API_KEY=sk-your-key...
```

2. Or:
```env
LLM_PROVIDER=anthropic
ANTHROPIC_API_KEY=sk-ant-your-key...
```

3. Restart backend:
```bash
docker compose restart backend
```

## Comparing Models

| Model | Size | Speed | Quality | Best For |
|-------|------|-------|---------|----------|
| Orca-mini | 2GB | ⚡⚡⚡ | Good | Lightweight |
| Mistral | 4GB | ⚡⚡ | Excellent | **Recommended** |
| Neural-chat | 4GB | ⚡⚡ | Good | Chat tasks |
| Llama2 | 7GB | ⚡ | Excellent | General purpose |
| Dolphin-Mixtral | 45GB | 💻 | Excellent | Complex tasks |

## Example Prompts

The system uses predefined prompts in `/prompts/`:
- `alert_correlation.md` - Correlate alerts
- `incident_classification.md` - Classify incidents
- `root_cause_analysis.md` - RCA analysis
- `incident_recommendation.md` - Remediation suggestions

All prompts are optimized for Mistral's capabilities.

## Next Steps

1. ✅ Install Ollama
2. ✅ Pull Mistral model
3. ✅ Update `.env` (already done!)
4. ✅ Start Docker services
5. ✅ Access frontend at http://localhost:3000

## Documentation Links

- **Ollama**: https://ollama.ai
- **Models**: https://ollama.ai/library
- **API**: https://github.com/ollama/ollama/blob/main/docs/api.md
- **Discord**: https://discord.gg/ollama

## Support

### Getting Help

```bash
# Ollama help
ollama help

# Check model details
ollama show mistral

# Pull latest version of model
ollama pull mistral:latest
```

### Common Issues

**Issue**: "Connection refused"
**Solution**: Ensure Ollama is running and accessible at `http://localhost:11434`

**Issue**: "Model not found"
**Solution**: Run `ollama pull mistral` first

**Issue**: "Out of memory"
**Solution**: Use smaller model like `orca-mini` or `neural-chat`

**Issue**: "Slow responses"
**Solution**: Reduce `OLLAMA_NUM_PREDICT` or use smaller model

## Free Forever!

Unlike OpenAI ($0.03-0.06 per 1K tokens) or Anthropic ($0.8-2.4 per 1M tokens):
- **Ollama**: $0.00 (zero cost)
- **Your machine**: Already paid for
- **No rate limits**: Run as much as you want
- **100% private**: Data never leaves your system

Enjoy incident management with zero LLM costs! 🚀
