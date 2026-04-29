# ImmigrationChatbot

Expert AI chatbot for immigration and career planning guidance, powered by open-source LLMs and immigration-specific knowledge.

**Features:**
- 🎯 Immigration expertise: H1B, L1, Green Cards, O-1, NIW visa guidance
- 🧠 Powered by Ollama (llama3.1:8b) - fully open source, local deployment
- 💬 Real-time streaming responses with markdown formatting
- 🔄 Session memory and conversation history
- 📱 Clean, modern chat UI with Next.js
- ⚡ FastAPI backend with CORS enabled
- 🐳 Docker/Docker Compose for one-click deployment

## Quick Start (Docker)

```bash
git clone https://github.com/Debashis2007/ImmigrationChatbot.git
cd ImmigrationChatbot
docker-compose up -d
```

Then visit:
- **Frontend:** http://localhost:3000
- **API:** http://localhost:8000
- **Health:** http://localhost:8000/health

---

## Architecture

```
┌─────────────────────────────────────┐
│   Frontend (Next.js + React)        │
│   - Chat UI                         │
│   - Markdown rendering              │
│   - Session management              │
└──────────────┬──────────────────────┘
               │ /api/chat/stream
┌──────────────▼──────────────────────┐
│   Backend (FastAPI)                 │
│   - Message routing                 │
│   - Session memory (SQL)            │
│   - Knowledge base integration      │
└──────────────┬──────────────────────┘
               │
      ┌────────▼────────┐
      │   Ollama LLM    │
      │  (llama3.1:8b)  │
      │                 │
      │ Immigration     │
      │ Knowledge Base  │
      └─────────────────┘
```

---

## Local Development Setup

### Prerequisites
- Python 3.11+
- Node.js 18+
- Ollama (for LLM) or OpenAI API key

### Backend Setup

```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -U pip
pip install -e .

# Configure environment
cp .env.example .env
# Edit .env with your settings

# Start Ollama (if using local LLM)
ollama serve
# In another terminal:
ollama pull llama3.1:8b

# Run backend
python -m uvicorn immigration_chatbot.api:app --reload --port 8000
```

### Frontend Setup

```bash
cd frontend
npm install
npm run dev

# Visit http://localhost:3000
```

---

## Configuration

### Environment Variables

**Backend (.env)**
```bash
# LLM Provider
LLM_ENABLED=true
LLM_PROVIDER=ollama              # or 'openai'
LLM_TIMEOUT_SECONDS=30

# Ollama (local)
OLLAMA_BASE_URL=http://localhost:11434/v1
OLLAMA_MODEL=llama3.1:8b
OLLAMA_API_KEY=ollama

# OpenAI (alternative)
OPENAI_API_KEY=sk-...
OPENAI_MODEL=gpt-4o-mini

# Database
MEMORY_BACKEND=sql               # or 'firebase'
DATABASE_URL=sqlite:///./chatbot.db

# API Auth (optional)
API_AUTH_ENABLED=false
API_AUTH_KEY=your_secure_key
```

**Frontend (.env.local)**
```bash
NEXT_PUBLIC_API_BASE_URL=http://localhost:8000
NEXT_PUBLIC_API_KEY=
```

---

## API Endpoints

### Health Check
```bash
curl http://localhost:8000/health
```

### Chat (non-streaming)
```bash
curl -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{
    "session_id": "user-123",
    "message": "What is H1B visa?"
  }'
```

### Chat (streaming with SSE)
```bash
curl -N -X POST http://localhost:8000/api/chat/stream \
  -H "Content-Type: application/json" \
  -d '{
    "session_id": "user-123",
    "message": "Tell me about green card timeline"
  }'
```

---

## Deployment

### Docker Compose (Recommended)

```bash
docker-compose up -d

# Check status
docker-compose ps

# View logs
docker-compose logs -f backend
docker-compose logs -f frontend

# Stop
docker-compose down
```

### Cloud Platforms

Full deployment guides available in [DEPLOYMENT.md](DEPLOYMENT.md):

- **Railway** - Simplest for beginners
- **Heroku** - Classic PaaS deployment
- **AWS ECS** - Enterprise-grade
- **Google Cloud Run** - Serverless
- **DigitalOcean** - Simple VPS

---

## Immigration Knowledge Base

The chatbot includes domain-specific knowledge about:

### Visa Categories
- **H1B:** Specialty occupation (3-6 months processing)
- **L1:** Intracompany transfer (2-4 months)
- **EB Green Card:** Employment-based permanent residence
- **O-1:** Extraordinary ability (2-4 months)
- **NIW:** National interest waiver (1-2 years)

### Key Features
- Current processing timelines
- Country-specific backlogs (India, China, etc.)
- Application requirements per visa type
- Decision trees for visa selection
- Risk flagging and common pitfalls

### Example Questions
- "I'm on F-1, what are my options?"
- "H1B vs L1, which is better?"
- "How long for green card approval?"
- "Draft an email to my employer about sponsorship"

---

## Testing

```bash
# Run unit tests
source .venv/bin/activate
pytest -v

# Test specific module
pytest tests/test_api.py -v
pytest tests/test_engine.py -v
```

---

## Project Structure

```
.
├── src/immigration_chatbot/
│   ├── api.py              # FastAPI routes
│   ├── engine.py           # Business logic
│   ├── knowledge.py        # Immigration knowledge base
│   ├── llm.py              # LLM client
│   ├── memory.py           # Session memory
│   └── cli.py              # CLI interface
├── frontend/
│   ├── pages/              # Next.js pages
│   ├── styles/             # CSS
│   └── package.json
├── tests/
│   ├── test_api.py
│   └── test_engine.py
├── docker-compose.yml      # Full stack Docker
├── Dockerfile.backend      # Backend image
├── Dockerfile.frontend     # Frontend image
├── DEPLOYMENT.md           # Cloud deployment guide
└── README.md               # This file
```

---

## Performance & Limits

| Metric | Value |
|--------|-------|
| Model | llama3.1:8b |
| Timeout | 30 seconds |
| Max message length | 4000 chars |
| Max concurrent sessions | Limited by memory |
| Database | SQLite (dev) / Postgres (prod) |

---

## Common Issues & Solutions

### Ollama Connection Timeout
```bash
# Increase timeout in .env
LLM_TIMEOUT_SECONDS=60

# Restart backend
docker-compose restart backend
```

### Frontend Can't Connect to Backend
```bash
# Check NEXT_PUBLIC_API_BASE_URL
echo $NEXT_PUBLIC_API_BASE_URL

# In development, usually:
NEXT_PUBLIC_API_BASE_URL=http://localhost:8000
```

### Model Not Loading
```bash
# Pull model manually
ollama pull llama3.1:8b

# Or use OpenAI
# Set OPENAI_API_KEY and change LLM_PROVIDER=openai
```

---

## Production Checklist

- [ ] Use PostgreSQL instead of SQLite
- [ ] Enable API authentication
- [ ] Set up HTTPS/SSL
- [ ] Configure logging
- [ ] Set up monitoring
- [ ] Configure backups
- [ ] Use production LLM (consider OpenAI)
- [ ] Add rate limiting
- [ ] Enable CORS for production domains only

---

## Contributing

Contributions welcome! Areas for improvement:

- [ ] Add more visa categories to knowledge base
- [ ] Integrate real USCIS API data
- [ ] Add visa bulletin tracking
- [ ] Implement appointment availability checking
- [ ] Add multi-language support
- [ ] Improve UI/UX
- [ ] Add analytics

---

## License

MIT License - see LICENSE file

---

## Disclaimer

This chatbot provides informational guidance only and does **not** constitute legal advice. Always consult with a qualified immigration attorney for specific cases.

---

## Support

- 📖 [Deployment Guide](DEPLOYMENT.md)
- 🐛 [Issues](https://github.com/Debashis2007/ImmigrationChatbot/issues)
- 💬 [Discussions](https://github.com/Debashis2007/ImmigrationChatbot/discussions)

---

**Made with ❤️ for immigrants navigating the US immigration system**

