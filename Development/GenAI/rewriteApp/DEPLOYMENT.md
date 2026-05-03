# Deployment Guide

## Production Deployment

### Backend Deployment Options

#### Option 1: Railway (Recommended - Easiest)

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login
railway login

# Create new project
railway init

# Deploy
railway up
```

Railway will automatically detect FastAPI and set:
- Start command: `uvicorn src.main:app --host 0.0.0.0 --port $PORT`
- Environment variables via Railway dashboard

#### Option 2: Vercel

```bash
# Install Vercel CLI
npm install -g vercel

# Deploy from backend directory
cd backend
vercel
```

Create `vercel.json`:
```json
{
  "buildCommand": "pip install -r requirements.txt",
  "env": {
    "OPENAI_API_KEY": "@openai_key",
    "ANTHROPIC_API_KEY": "@anthropic_key"
  }
}
```

#### Option 3: Docker + Heroku

1. Create `Dockerfile` in backend:
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

2. Deploy:
```bash
heroku container:push web
heroku container:release web
```

### Frontend Deployment Options

#### Option 1: Vercel (Recommended)

```bash
cd frontend
vercel
```

Vercel auto-detects React + Vite and builds to `dist/`

Add environment variable:
```
REACT_APP_API_URL=https://your-backend-domain.com
```

#### Option 2: Netlify

```bash
cd frontend
netlify deploy --prod --dir=dist
```

Or connect GitHub repo for auto-deploy on push.

#### Option 3: GitHub Pages

```bash
cd frontend
npm run build
# Upload dist/ contents to gh-pages branch
```

### Chrome Extension Deployment

#### Prepare for Chrome Web Store

1. Create a `.crx` file from extension directory
2. Generate private key:
```bash
openssl genrsa -out extension/key.pem 2048
```

3. Create manifest with correct version in `manifest.json`

4. Upload to [Chrome Web Store Developer Dashboard](https://chrome.google.com/webstore)

#### Production API Configuration

Update `extension/src/popup.js`:
```javascript
const API_BASE_URL = 'https://your-production-api.com';
```

Update `extension/manifest.json` host permissions:
```json
"host_permissions": [
  "https://your-production-api.com/*"
]
```

## Environment Variables

### Backend Production

```env
# API Keys
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-...

# LLM Config
LLM_PROVIDER=openai
LLM_MODEL=gpt-4-turbo-preview

# Server
LOG_LEVEL=INFO
DEBUG=false

# CORS - Add production domains
CORS_ORIGINS=["https://yourapp.com","https://app.yourapp.com"]
```

### Frontend Production

```env
REACT_APP_API_URL=https://your-production-api.com
```

## Performance Optimization

### Backend
- Use connection pooling for database
- Cache LLM responses for identical inputs
- Add rate limiting
- Use CDN for static files
- Monitor API response times

### Frontend
- Code splitting with React.lazy()
- Minify and compress assets
- Lazy load components
- Cache API responses locally
- Optimize images

### Extension
- Minimize popup.js size
- Lazy load heavy libraries
- Cache API responses in Chrome storage

## Monitoring & Logging

### Backend
```python
import logging
logger = logging.getLogger(__name__)
logger.info(f"Text rewritten: {len(text)} chars → {len(rewritten)} chars")
```

Set up monitoring:
- Sentry for error tracking
- DataDog for performance metrics
- Log aggregation (ELK stack, Papertrail)

### Frontend
- Google Analytics
- Sentry JavaScript client
- Custom error boundaries

## Database (Optional Future Addition)

For user accounts/history:
```bash
# Backend
pip install sqlalchemy psycopg2

# Create PostgreSQL on Railway/Heroku
# Update models and migrations
```

## SSL/TLS

All production deployments should use HTTPS.
- Vercel/Railway provide free SSL
- Use Let's Encrypt for custom domains

## Cost Estimation

- **Backend (Railway)**: $5-20/month
- **Frontend (Vercel)**: Free tier available
- **Chrome Extension**: One-time Chrome Web Store fee ($5)
- **LLM API**: Based on usage (OpenAI/Anthropic pricing)

## Rollback Strategy

Keep previous versions available:
```bash
# Git tagging
git tag v1.0.0
git push origin v1.0.0

# Revert on Railway/Vercel dashboard
```

## Security Checklist

- [ ] API keys not in git (use .env)
- [ ] HTTPS on all domains
- [ ] CORS configured for production domains
- [ ] Rate limiting enabled
- [ ] Input validation on all endpoints
- [ ] Remove debug logging in production
- [ ] Database encryption at rest
- [ ] Regular security audits
- [ ] Dependencies up to date

---

**Need help?** See README.md for support links.
