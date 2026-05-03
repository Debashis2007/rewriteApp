# Getting Started with Rewrite Professional

## 5-Minute Quick Start

### Step 1: Clone & Install (2 min)

```bash
cd rewriteApp
```

#### Backend
```bash
cd backend
pip install -r requirements.txt
cp .env.example .env
```

#### Frontend
```bash
cd ../frontend
npm install
```

### Step 2: Configure API Keys (1 min)

Edit `backend/.env`:
```bash
OPENAI_API_KEY=sk-your-key-here
# OR
ANTHROPIC_API_KEY=sk-your-key-here
```

### Step 3: Run Services (2 min)

**Terminal 1 - Backend:**
```bash
cd backend
python -m uvicorn src.main:app --reload
# Runs at http://localhost:8000
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
# Runs at http://localhost:3000
```

**Terminal 3 - Chrome Extension:**
1. Go to `chrome://extensions/`
2. Enable "Developer mode" (top right)
3. Click "Load unpacked"
4. Select `/path/to/rewriteApp/extension`

## What You Can Do Now

### Web App
1. Visit `http://localhost:3000`
2. Paste text in left box
3. Select tone & action
4. Click "Rewrite"
5. See results in right box

### Chrome Extension
1. Click extension icon in toolbar
2. Paste text
3. Choose tone & action
4. Click rewrite
5. Copy result

## Testing the API

```bash
curl -X POST http://localhost:8000/rewrite \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Hi there, I wanted to reach out",
    "tone": "formal",
    "action": "rewrite"
  }'
```

## Troubleshooting

### Backend won't start
- Check Python version: `python --version` (needs 3.8+)
- Check port 8000 is free: `lsof -i :8000`
- Install requirements: `pip install -r requirements.txt`

### Frontend won't start
- Check Node version: `node --version` (needs 16+)
- Clear cache: `rm -rf node_modules && npm install`
- Check port 3000 is free: `lsof -i :3000`

### API keys not working
- Verify keys in `.env` are valid
- Check `LLM_PROVIDER` is set correctly
- Test with curl command above

### Extension not connecting
- Ensure backend is running at `http://localhost:8000`
- Check `extension/src/popup.js` has correct `API_BASE_URL`
- Reload extension in `chrome://extensions/`

## Next Steps

### Customize Text Options
1. Edit `backend/src/rewriter.py`
2. Add new `Tone` or `RewriteAction` enum value
3. Add guidance prompt in `action_guidance` dict
4. Update `frontend/src/App.jsx` select options

### Deploy to Production
- **Backend**: Vercel, Heroku, Railway, AWS Lambda
- **Frontend**: Vercel, Netlify
- **Extension**: Chrome Web Store

### Add New Features
- Custom context/instructions
- Save/history of rewrites
- Batch processing
- API keys management
- User accounts

See `README.md` for full documentation and `DEPLOYMENT.md` for production setup.
