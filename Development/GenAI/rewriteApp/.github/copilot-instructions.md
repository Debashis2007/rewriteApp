# Copilot Instructions for rewriteApp

## Project Overview

**Rewrite Professional** — A multi-platform AI text rewriting tool with web interface and Chrome extension. Transform text with tone control (formal, friendly, assertive) and actions (rewrite, shorten, strengthen).

## Architecture: 3-Tier Stack

```
Frontend Layer       (React web app + Chrome extension)
                         ↓
API Layer            (FastAPI with async text rewriting)
                         ↓
LLM Service Layer    (OpenAI/Anthropic with lazy initialization)
```

**Core Flow**: Text input → LLM rewriting with tone/action prompt → Text analysis → Response

## Code Organization

| Directory | Purpose |
|-----------|---------|
| `backend/src/main.py` | FastAPI app with `/rewrite`, `/analyze`, `/health` endpoints |
| `backend/src/rewriter.py` | `TextRewriter` class handling LLM calls and text analysis |
| `backend/src/config.py` | `Settings` via Pydantic BaseSettings, loads `.env` |
| `frontend/src/App.jsx` | React component with tone/action selectors, textarea pairs, analysis panel |
| `extension/src/popup.html` | Chrome extension popup UI with form |
| `extension/src/popup.js` | Extension logic handling rewrite requests to backend API |

## Critical Patterns & Conventions

### Building a New Action/Tone
Edit `backend/src/rewriter.py`:
```python
# Add to RewriteAction enum
class RewriteAction(str, Enum):
    CUSTOM = "custom"

# Add to action_guidance dict in rewrite()
action_guidance = {
    RewriteAction.CUSTOM: "Your custom guidance...",
}
```

### API Error Handling
```python
# Pattern: Always validate, return 400/500 with detail
if not request.text or not request.text.strip():
    raise HTTPException(status_code=400, detail="Text cannot be empty")
```

### Frontend Component Pattern
```javascript
// State → Render → Handler
const [text, setText] = useState('');
const handleRewrite = async () => {
  const response = await axios.post(`${API_BASE_URL}/rewrite`, {...});
};
```

### LLM Provider Abstraction
- Use `settings.llm_provider` ("openai" or "anthropic")
- Lazy init: `if self.llm_client is None: from openai import AsyncOpenAI`
- Retry logic: `@retry` decorator from tenacity
- Both return same interface: `{"content": str, "tool_calls": list}`

## Project Setup & Workflows

### Prerequisites & Installation
```bash
python --version  # 3.8+
node --version    # 16+
cd rewriteApp
```

### Running All Services
```bash
# Terminal 1: Backend
cd backend
pip install -r requirements.txt
cp .env.example .env
# Add API keys
python -m uvicorn src.main:app --reload

# Terminal 2: Frontend
cd frontend
npm install
npm run dev

# Terminal 3: Chrome Extension
# chrome://extensions/ → Load unpacked → extension/
```

### Key Dependencies
- `fastapi==0.104.1` — Web framework
- `pydantic==2.5.0` — Validation
- `openai==1.3.0`, `anthropic==0.7.0` — LLM providers
- `react@18`, `axios`, `tailwindcss` — Frontend
- `vite==5.0.0` — Frontend build

## Integration Points

- **LLM Swap**: Change `LLM_PROVIDER` in `.env` → auto-uses `OpenAIClient` or `AnthropicClient`
- **Frontend API**: Axios calls to `${API_BASE_URL}/rewrite` — configurable via env
- **Extension Config**: Edit `API_BASE_URL` in `extension/src/popup.js` for production
- **CORS**: Update `CORS_ORIGINS` in backend `.env` to allow frontend/extension domains

## Testing & Quality

- **Type Safety**: Full type hints in backend, JSX React patterns in frontend
- **Async First**: All backend handlers use `async def`, frontend uses `async/await`
- **Error Boundaries**: Try/catch with `HTTPException` → JSON response
- **UI Feedback**: Loading states, error messages, copy-to-clipboard, text analysis metrics

## Common Customizations

### Add New Tone
1. Add to `Tone` enum in `rewriter.py`
2. Add prompt guidance in `action_guidance` dict
3. Update frontend select dropdown

### Change LLM Model
```bash
# In .env
LLM_MODEL=gpt-4o  # or claude-3-haiku-20240307
```

### Deploy Frontend
```bash
cd frontend
npm run build
# Upload dist/ to Vercel/Netlify
```

### Package Chrome Extension
- Use Chrome Web Store Developer Dashboard
- Upload `.crx` file or zip source

---

**Last Updated:** May 3, 2026  
**Key Files**: `backend/src/main.py` (API), `frontend/src/App.jsx` (UI), `extension/src/popup.html` (Extension)
