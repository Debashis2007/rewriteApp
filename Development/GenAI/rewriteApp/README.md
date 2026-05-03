# Rewrite Professional

Transform your text with AI-powered rewriting. Choose your tone (formal, friendly, assertive) and action (rewrite, shorten, strengthen) to create professional, polished content instantly.

## Quick Start

### 1. Prerequisites
- Python 3.8+
- Node.js 16+ (for web frontend)
- Chrome browser (for extension)

### 2. Backend Setup

```bash
cd backend
pip install -r requirements.txt
cp .env.example .env

# Add your API keys to .env
# OPENAI_API_KEY=sk-...
# ANTHROPIC_API_KEY=sk-...

# Run server
python -m uvicorn src.main:app --reload --port 8000
```

Server starts at `http://localhost:8000`

### 3. Web Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Web app available at `http://localhost:3000`

### 4. Chrome Extension Setup

1. Build/prepare extension files in `extension/` folder
2. Go to `chrome://extensions/`
3. Enable "Developer mode" (toggle, top right)
4. Click "Load unpacked"
5. Select `extension/` directory

## Features

### Tone Options
- **Formal**: Professional, structured language
- **Friendly**: Conversational, approachable tone
- **Assertive**: Confident, strong language

### Actions
- **Rewrite**: Complete text transformation
- **Shorten**: Concise, condensed version
- **Strengthen**: More impactful, persuasive language

### Text Analysis
- Word count
- Character count
- Sentence count
- Average word length
- Detected tone

## API Endpoints

### POST `/rewrite`
Rewrite text with specified tone and action.

```json
{
  "text": "Your text here",
  "tone": "formal",
  "action": "rewrite",
  "context": "Optional context for better results"
}
```

**Response:**
```json
{
  "original": "Your text here",
  "rewritten": "Rewritten text...",
  "tone": "formal",
  "action": "rewrite",
  "analysis": {
    "word_count": 5,
    "char_count": 15,
    "sentence_count": 1,
    "avg_word_length": 3.0,
    "tone_detected": "neutral"
  }
}
```

### POST `/analyze`
Analyze text without rewriting.

### GET `/tones`
Get available tone options.

### GET `/actions`
Get available action options.

### GET `/health`
Health check endpoint.

## Configuration

### Environment Variables

**Backend (.env):**
```
OPENAI_API_KEY=sk-...              # OpenAI API key
ANTHROPIC_API_KEY=sk-...           # Anthropic API key
LLM_PROVIDER=openai                # openai or anthropic
LLM_MODEL=gpt-4-turbo-preview      # Model to use
LOG_LEVEL=INFO                     # Logging level
DEBUG=false                        # Debug mode
CORS_ORIGINS=[...]                 # Allowed CORS origins
```

**Frontend (.env):**
```
REACT_APP_API_URL=http://localhost:8000
```

## Project Structure

```
rewriteApp/
├── backend/
│   ├── src/
│   │   ├── __init__.py
│   │   ├── main.py              # FastAPI app
│   │   ├── config.py            # Configuration
│   │   └── rewriter.py          # Text rewriting logic
│   ├── requirements.txt
│   └── .env.example
├── frontend/
│   ├── src/
│   │   ├── App.jsx              # Main React component
│   │   ├── main.jsx             # Entry point
│   │   └── index.css            # Tailwind styles
│   ├── index.html
│   ├── package.json
│   ├── vite.config.js
│   └── tailwind.config.js
└── extension/
    ├── manifest.json            # Chrome extension config
    ├── src/
    │   ├── popup.html           # Extension popup UI
    │   ├── popup.js             # Popup logic
    │   ├── background.js        # Service worker
    │   └── content.js           # Content script
    └── README.md
```

## Development Workflow

### Running All Services

Terminal 1 (Backend):
```bash
cd backend
python -m uvicorn src.main:app --reload
```

Terminal 2 (Frontend):
```bash
cd frontend
npm run dev
```

Terminal 3 (Chrome Extension):
- Load unpacked from `extension/` directory

### Testing

Backend has type hints and uses Pydantic for validation. Test the API:

```bash
curl -X POST http://localhost:8000/rewrite \
  -H "Content-Type: application/json" \
  -d '{
    "text": "hello world",
    "tone": "formal",
    "action": "rewrite"
  }'
```

## Deployment

### Backend (Vercel/Heroku/Railway)
```bash
cd backend
pip install -r requirements.txt
uvicorn src.main:app --host 0.0.0.0 --port $PORT
```

### Frontend (Vercel/Netlify)
```bash
cd frontend
npm install
npm run build
# Deploy `dist/` folder
```

### Chrome Extension
- Package as `.crx` file
- Submit to [Chrome Web Store](https://chrome.google.com/webstore)

## Pricing Model

- **Web Tool**: Free or freemium (with usage limits)
- **Chrome Extension**: $5 one-time purchase or subscription
- **Enterprise**: Custom API pricing

## Technology Stack

- **Backend**: FastAPI, Pydantic, OpenAI/Anthropic
- **Frontend**: React, Vite, Tailwind CSS
- **Extension**: Vanilla JavaScript, Chrome APIs
- **Async**: asyncio, aiohttp

## Contributing

1. Follow existing code patterns
2. Add type annotations to all functions
3. Test with both OpenAI and Anthropic
4. Update documentation for new features

## License

MIT License - See LICENSE file for details
