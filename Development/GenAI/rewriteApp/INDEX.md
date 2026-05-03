# Rewrite Professional - File Index

Quick navigation guide for the rewriteApp project.

## 📖 Start Here

**New to the project?**
1. Read: [`README.md`](README.md) — Project overview
2. Follow: [`QUICKSTART.md`](QUICKSTART.md) — Get running in 5 minutes
3. Review: [`ARCHITECTURE.md`](ARCHITECTURE.md) — Understand the design

## 📂 Backend (Python/FastAPI)

### Core Files
| File | Purpose | Key Classes |
|------|---------|------------|
| [`backend/src/main.py`](backend/src/main.py) | REST API server | `FastAPI`, endpoints |
| [`backend/src/rewriter.py`](backend/src/rewriter.py) | Text rewriting logic | `TextRewriter`, `Tone`, `RewriteAction` |
| [`backend/src/config.py`](backend/src/config.py) | Settings & env management | `Settings` |
| [`backend/requirements.txt`](backend/requirements.txt) | Python dependencies | - |
| [`backend/.env.example`](backend/.env.example) | Environment template | - |

### API Endpoints
- `POST /rewrite` — Rewrite text with tone & action
- `POST /analyze` — Analyze text metrics
- `GET /tones` — List available tones
- `GET /actions` — List available actions
- `GET /health` — Health check

### Key Functions
```python
TextRewriter.rewrite(text, tone, action, context) → str
TextRewriter.analyze(text) → dict
```

## 🎨 Frontend (React/JavaScript)

### Core Files
| File | Purpose |
|------|---------|
| [`frontend/src/App.jsx`](frontend/src/App.jsx) | Main React component |
| [`frontend/src/main.jsx`](frontend/src/main.jsx) | Entry point |
| [`frontend/src/index.css`](frontend/src/index.css) | Tailwind styles |
| [`frontend/index.html`](frontend/index.html) | HTML shell |
| [`frontend/package.json`](frontend/package.json) | npm dependencies |
| [`frontend/vite.config.js`](frontend/vite.config.js) | Build config |
| [`frontend/tailwind.config.js`](frontend/tailwind.config.js) | Tailwind config |

### Component State
```javascript
const [originalText, setOriginalText] = useState('');
const [rewrittenText, setRewrittenText] = useState('');
const [tone, setTone] = useState('formal');
const [action, setAction] = useState('rewrite');
const [loading, setLoading] = useState(false);
const [error, setError] = useState('');
const [analysis, setAnalysis] = useState(null);
```

### Key Functions
```javascript
handleRewrite()  // POST to /rewrite
handleCopy()     // Copy to clipboard
handleSwap()     // Swap texts
handleClear()    // Reset form
```

## 🔌 Chrome Extension

### Core Files
| File | Purpose |
|------|---------|
| [`extension/manifest.json`](extension/manifest.json) | Extension config |
| [`extension/src/popup.html`](extension/src/popup.html) | UI HTML |
| [`extension/src/popup.js`](extension/src/popup.js) | Popup logic |
| [`extension/src/background.js`](extension/src/background.js) | Service worker |
| [`extension/src/content.js`](extension/src/content.js) | Content script |
| [`extension/README.md`](extension/README.md) | Extension docs |

### Loading the Extension
1. Go to `chrome://extensions/`
2. Enable "Developer mode"
3. Click "Load unpacked"
4. Select the `extension/` folder

## 📚 Documentation

| Document | Purpose |
|----------|---------|
| [`README.md`](README.md) | Complete feature overview, setup, API docs |
| [`QUICKSTART.md`](QUICKSTART.md) | 5-minute setup guide |
| [`DEPLOYMENT.md`](DEPLOYMENT.md) | Production deployment guide |
| [`ARCHITECTURE.md`](ARCHITECTURE.md) | System design & scalability |
| [`PROJECT_SUMMARY.md`](PROJECT_SUMMARY.md) | Project overview |
| [`.github/copilot-instructions.md`](.github/copilot-instructions.md) | AI agent guidance |

## 🔧 Configuration Files

| File | Purpose |
|------|---------|
| `.env.example` | Environment variables template |
| `.gitignore` | Git ignore patterns |
| `package.json` | npm dependencies (frontend) |
| `requirements.txt` | pip dependencies (backend) |
| `vite.config.js` | Vite build configuration |
| `tailwind.config.js` | Tailwind CSS configuration |
| `manifest.json` | Chrome extension manifest |

## 🗂️ File Structure by Function

### Text Rewriting Logic
- Main: `backend/src/rewriter.py` (TextRewriter class)
- API: `backend/src/main.py` (POST /rewrite endpoint)
- Frontend: `frontend/src/App.jsx` (handleRewrite function)
- Extension: `extension/src/popup.js` (fetch to API)

### Configuration
- Backend: `backend/src/config.py` (Settings class)
- Backend: `backend/.env.example` (variables)
- Frontend: `frontend/vite.config.js` (API proxy)
- Extension: `extension/src/popup.js` (API_BASE_URL)

### UI Components
- Web: `frontend/src/App.jsx` (single component)
- Extension: `extension/src/popup.html` (HTML structure)
- Extension: `extension/src/popup.js` (JavaScript logic)

## 🚀 Quick Commands

### Backend Development
```bash
cd backend
pip install -r requirements.txt
cp .env.example .env
python -m uvicorn src.main:app --reload
```

### Frontend Development
```bash
cd frontend
npm install
npm run dev
```

### Extension Loading
```
chrome://extensions/ → Load unpacked → extension/
```

### Testing Backend
```bash
curl -X POST http://localhost:8000/rewrite \
  -H "Content-Type: application/json" \
  -d '{"text":"hi","tone":"formal","action":"rewrite"}'
```

## 📋 Common Tasks

### Add a New Tone
1. Edit `backend/src/rewriter.py` → Add to `Tone` enum
2. Add guidance in `action_guidance` dict
3. Update `frontend/src/App.jsx` → Add option to select

### Add a New Action
1. Edit `backend/src/rewriter.py` → Add to `RewriteAction` enum
2. Add guidance in `action_guidance` dict
3. Update `frontend/src/App.jsx` → Add option to select

### Change LLM Provider
1. Edit `backend/.env` → `LLM_PROVIDER=anthropic`
2. Restart backend server
3. System automatically uses Anthropic

### Deploy Backend
See: [`DEPLOYMENT.md`](DEPLOYMENT.md)

### Deploy Frontend
See: [`DEPLOYMENT.md`](DEPLOYMENT.md)

### Publish Extension
See: [`DEPLOYMENT.md`](DEPLOYMENT.md)

## 🔍 Code Review Checklist

Before committing:
- [ ] Type hints on all functions
- [ ] Error handling (try/catch)
- [ ] Input validation
- [ ] Updated documentation
- [ ] Tested changes
- [ ] No API keys in code

## 📊 Project Statistics

- **Total Files**: 27
- **Python Files**: 4 (backend)
- **JavaScript Files**: 6 (extension + config)
- **React Files**: 2 (frontend)
- **Documentation**: 7 markdown files
- **Lines of Code**: ~2000

## 🎓 Learning Path

1. Start: [`QUICKSTART.md`](QUICKSTART.md)
2. Backend: [`backend/src/rewriter.py`](backend/src/rewriter.py)
3. API: [`backend/src/main.py`](backend/src/main.py)
4. Frontend: [`frontend/src/App.jsx`](frontend/src/App.jsx)
5. Extension: [`extension/src/popup.js`](extension/src/popup.js)
6. Design: [`ARCHITECTURE.md`](ARCHITECTURE.md)
7. Deploy: [`DEPLOYMENT.md`](DEPLOYMENT.md)

## 🔗 External Resources

- FastAPI: https://fastapi.tiangolo.com
- React: https://react.dev
- Tailwind: https://tailwindcss.com
- Chrome Extensions: https://developer.chrome.com/docs/extensions/
- OpenAI API: https://platform.openai.com/docs
- Anthropic API: https://docs.anthropic.com

## 💬 Questions?

Check the relevant documentation:
- **Setup Issues**: [`QUICKSTART.md`](QUICKSTART.md)
- **Architecture Questions**: [`ARCHITECTURE.md`](ARCHITECTURE.md)
- **Deployment**: [`DEPLOYMENT.md`](DEPLOYMENT.md)
- **Extension**: [`extension/README.md`](extension/README.md)
- **General**: [`README.md`](README.md)

---

**Last Updated**: May 3, 2026  
**Project Status**: ✅ Ready for Development
