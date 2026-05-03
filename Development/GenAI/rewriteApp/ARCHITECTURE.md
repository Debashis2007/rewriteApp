# Architecture Overview

## System Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                     USER INTERFACES                         │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────────────┐      ┌──────────────────┐             │
│  │  Web Browser     │      │  Chrome Browser  │             │
│  │  (React App)     │      │  (Extension)     │             │
│  └────────┬─────────┘      └────────┬─────────┘             │
│           │                         │                       │
│           └──────────────┬──────────┘                       │
│                          │                                  │
├──────────────────────────┼──────────────────────────────────┤
│                   HTTP/JSON (REST API)                      │
├──────────────────────────┼──────────────────────────────────┤
│                          │                                  │
│                    ┌─────▼──────┐                           │
│                    │  FastAPI   │                           │
│                    │  (Backend)  │                           │
│                    └─────┬──────┘                            │
│                          │                                  │
│  ┌───────────────────────┼───────────────────────┐          │
│  │                       │                       │          │
│  ▼                       ▼                       ▼          │
│ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐         │
│ │  Rewriter    │ │   Config     │ │  Error       │         │
│ │  Engine      │ │  Management  │ │  Handling    │         │
│ └──────┬───────┘ └──────────────┘ └──────────────┘         │
│        │                                                   │
│        │  (Async/Await)                                   │
│        │                                                   │
│ ┌──────▼──────────────────────────┐                        │
│ │   LLM Service Layer              │                       │
│ │  (Provider Abstraction)          │                       │
│ ├──────────┬──────────────────────┤                        │
│ │ OpenAI  │ Anthropic             │                        │
│ │ Client  │ Client                │                        │
│ └────┬────┴───────┬────────────────┘                        │
│      │            │                                        │
├──────┼────────────┼────────────────────────────────────────┤
│      │            │                                        │
│      ▼            ▼                                        │
│   ┌─────────┐ ┌──────────┐                                │
│   │ OpenAI  │ │ Anthropic│                                │
│   │ API     │ │ API      │                                │
│   └─────────┘ └──────────┘                                │
│                                                           │
└───────────────────────────────────────────────────────────┘
```

## Data Flow

### Request Flow
```
User Input (Text)
    ↓
UI Validation (length, empty check)
    ↓
HTTP POST /rewrite
    ├─ text: str
    ├─ tone: "formal" | "friendly" | "assertive"
    ├─ action: "rewrite" | "shorten" | "strengthen"
    └─ context: str (optional)
    ↓
Backend Processing
    ├─ Validate request
    ├─ Prepare prompt with tone guidance
    ├─ Call LLM (OpenAI/Anthropic)
    ├─ Analyze text (word count, tone detection, etc.)
    └─ Return response
    ↓
Response JSON
    ├─ original: str
    ├─ rewritten: str
    ├─ tone: str
    ├─ action: str
    └─ analysis: {word_count, char_count, sentence_count, ...}
    ↓
UI Update
    ├─ Display rewritten text
    ├─ Show analysis metrics
    ├─ Hide loading spinner
    └─ Enable copy button
```

## Component Interactions

### Backend Components

```
FastAPI App
├── Endpoints
│   ├── POST /rewrite          → TextRewriter.rewrite()
│   ├── POST /analyze          → TextRewriter.analyze()
│   ├── GET /tones             → Tone enum values
│   ├── GET /actions           → RewriteAction enum values
│   └── GET /health            → {"status": "healthy"}
│
├── TextRewriter (async)
│   ├── _get_llm_client()      → Lazy initialization
│   ├── rewrite()              → LLM call with prompt engineering
│   └── analyze()              → Text metrics & tone detection
│
└── Configuration
    └── Settings (from .env)
        ├── API keys
        ├── Model selection
        ├── CORS origins
        └── Logging level
```

### Frontend Components

```
React App
├── App.jsx (Main Component)
│   ├── State
│   │   ├── originalText
│   │   ├── rewrittenText
│   │   ├── tone
│   │   ├── action
│   │   ├── loading
│   │   ├── error
│   │   └── analysis
│   │
│   ├── Handlers
│   │   ├── handleRewrite()     → POST /rewrite
│   │   ├── handleCopy()        → clipboard.writeText()
│   │   ├── handleSwap()        → swap texts
│   │   └── handleClear()       → reset state
│   │
│   └── Render Sections
│       ├── Original text box
│       ├── Rewritten text box
│       ├── Controls (tone, action, buttons)
│       ├── Error display
│       └── Analysis panel
```

### Chrome Extension

```
Extension
├── manifest.json              → Permissions, icons, scripts
├── popup.html/js             → User interface
│   ├── Input textarea
│   ├── Tone selector
│   ├── Action selector
│   ├── Output display
│   └── Copy button
│
├── background.js             → Service worker
│   └── Message handling
│
└── content.js                → Injected scripts
    └── Context menu integration
```

## Technology Stack

### Backend
- **Framework**: FastAPI 0.104.1
- **Async Runtime**: asyncio, aiohttp
- **Validation**: Pydantic 2.5.0
- **LLM Integration**: OpenAI 1.3.0, Anthropic 0.7.0
- **Retry Logic**: tenacity 8.2.3
- **CORS**: fastapi.middleware.cors
- **Server**: uvicorn

### Frontend
- **Framework**: React 18.2.0
- **Build Tool**: Vite 5.0.0
- **HTTP Client**: axios
- **Styling**: Tailwind CSS 3.3.0
- **Icons**: lucide-react
- **UI Library**: HTML5, CSS3, JavaScript ES6+

### Chrome Extension
- **Manifest**: V3 (latest)
- **Language**: Vanilla JavaScript
- **Storage**: Chrome Storage API
- **Permissions**: activeTab, scripting, storage

## Key Features

### Text Rewriting
- **Tone Control**: Formal, Friendly, Assertive
- **Actions**: Rewrite, Shorten, Strengthen
- **Context Support**: Optional context for better results
- **Retry Logic**: Auto-retry on API failures

### Text Analysis
- Word count
- Character count
- Sentence count
- Average word length
- Detected tone heuristics

### User Experience
- Real-time feedback
- Loading states
- Error messages
- Copy-to-clipboard
- Swap original/rewritten
- Local storage for preferences

## Scalability Considerations

### Horizontal Scaling
- Stateless API (no session state)
- All state passed in requests
- LLM clients are thread-safe
- Can run multiple backend instances

### Rate Limiting (Future)
```python
# Add to main.py
from slowapi import Limiter
limiter = Limiter(key_func=get_remote_address)

@app.post("/rewrite")
@limiter.limit("10/minute")
async def rewrite_text(request: RewriteRequest):
    ...
```

### Caching (Future)
```python
from functools import lru_cache
@lru_cache(maxsize=1000)
async def cache_rewrite(text_hash, tone, action):
    # Cache LLM responses
```

### Database (Future)
- Store user history
- Track analytics
- Persist settings
- Use PostgreSQL + SQLAlchemy

## Security

### API Security
- Input validation (length limits, content checks)
- API key protection (environment variables)
- CORS restriction to allowed origins
- Rate limiting (recommended)
- HTTPS in production

### Extension Security
- No persistent storage of sensitive data
- Content scripts don't access user data
- API keys only in server-side `.env`
- Chrome's CSP restrictions

### Frontend Security
- Sanitize user input (Tailwind only)
- No sensitive data in localStorage
- API keys never sent to frontend
- HTTPS only in production

---

For deployment instructions, see `DEPLOYMENT.md`
For quick start, see `QUICKSTART.md`
For full documentation, see `README.md`
