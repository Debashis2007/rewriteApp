# Deploying AIMS to Hugging Face Spaces

This guide walks you through deploying the Autonomous Incident Management System (AIMS) to Hugging Face Spaces.

## Prerequisites

1. **Hugging Face Account** - Create one at https://huggingface.co
2. **Git CLI** - For cloning and pushing to HF repositories
3. **Your System** - Complete AIMS codebase

## Deployment Options

### Option 1: Deploy Frontend Only (Recommended for Speed)

The frontend is a React app that communicates with a backend API. For quick deployment:

1. Go to https://huggingface.co/spaces
2. Click "Create new Space"
3. Fill in:
   - **Space name**: `autonomous-incident-management`
   - **License**: Choose one (MIT recommended)
   - **Space SDK**: Select `Docker`
4. Clone the space
5. Copy your frontend code
6. Push to Hugging Face

### Option 2: Deploy Full Stack (Frontend + Backend)

Deploy the complete system with Docker containers.

## Step-by-Step Setup

### Step 1: Create a Hugging Face Space

```bash
# Navigate to Hugging Face Spaces: https://huggingface.co/spaces
# Click "Create new Space"
# Choose Docker as SDK
# Name it "autonomous-incident-management"
```

### Step 2: Clone the Space Repository

```bash
git clone https://huggingface.co/spaces/<your-username>/autonomous-incident-management
cd autonomous-incident-management
```

### Step 3: Set Up Frontend Deployment

#### Option A: Frontend Only (Simple)

1. Copy the frontend directory to your Space
2. Create a `Dockerfile` (see below)
3. Modify API endpoint to use backend

#### Option B: Frontend + Backend (Complete)

1. Create docker-compose setup
2. Run all services

### Step 4: Frontend Dockerfile

Create `Dockerfile`:

```dockerfile
FROM node:18-alpine AS build

WORKDIR /app

# Copy package files
COPY frontend/package*.json ./

# Install dependencies
RUN npm install

# Copy source code
COPY frontend/src ./src
COPY frontend/index.html .
COPY frontend/vite.config.ts .
COPY frontend/tsconfig.json .
COPY frontend/tsconfig.node.json .

# Build for production
RUN npm run build

# Production stage
FROM node:18-alpine

WORKDIR /app

# Install serve to run the app
RUN npm install -g serve

# Copy built files
COPY --from=build /app/dist ./dist

# Expose port
EXPOSE 7860

# Start the app
CMD ["serve", "-s", "dist", "-l", "7860"]
```

### Step 5: Create app.py (Alternative)

For more flexibility, create `app.py` to run with Gradio:

```python
import os
import subprocess
import signal

def start_servers():
    """Start frontend and backend servers"""
    
    # Get environment variables
    backend_port = os.getenv('BACKEND_PORT', 8001)
    frontend_port = os.getenv('FRONTEND_PORT', 7860)
    
    # Start backend
    backend_process = subprocess.Popen(
        ['python', '-m', 'uvicorn', 'src.main:app', '--host', '0.0.0.0', '--port', str(backend_port)],
        cwd='backend',
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    
    # Start frontend
    frontend_process = subprocess.Popen(
        ['npm', 'run', 'build'],
        cwd='frontend',
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    
    frontend_process.wait()
    
    # Serve frontend
    frontend_serve = subprocess.Popen(
        ['npx', 'serve', '-s', 'dist', '-l', str(frontend_port)],
        cwd='frontend',
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    
    return backend_process, frontend_serve

if __name__ == '__main__':
    backend_proc, frontend_proc = start_servers()
    print(f"✅ Backend running on port 8001")
    print(f"✅ Frontend running on port 7860")
    
    try:
        backend_proc.wait()
        frontend_proc.wait()
    except KeyboardInterrupt:
        backend_proc.terminate()
        frontend_proc.terminate()
```

### Step 6: Create requirements.txt

For backend dependencies:

```
fastapi==0.109.0
uvicorn==0.27.0
sqlalchemy==2.0.25
psycopg2-binary==2.9.9
redis==5.0.1
pydantic==2.5.3
pydantic-settings==2.1.0
openai==1.3.7
anthropic==0.7.11
aiohttp==3.9.1
python-dotenv==1.0.0
```

### Step 7: Environment Variables

Create a `.env` file in your Space:

```env
# Backend
DATABASE_URL=postgresql://aims:aims@localhost:5432/aims
REDIS_URL=redis://localhost:6379
LOG_LEVEL=INFO

# LLM
LLM_PROVIDER=openai
OPENAI_API_KEY=your_key_here
ANTHROPIC_API_KEY=your_key_here

# CORS
CORS_ORIGINS=["http://localhost:3000","http://localhost:7860","*"]

# Notifications
NOTIFICATION_PROVIDERS=email,slack,webhook
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SLACK_BOT_TOKEN=your_token_here
WEBHOOK_URL=your_webhook_url

# Security
SECRET_KEY=your-secret-key-here
```

### Step 8: docker-compose.yml (If Using Full Stack)

```yaml
version: '3.8'

services:
  postgres:
    image: postgres:15-alpine
    environment:
      POSTGRES_USER: aims
      POSTGRES_PASSWORD: aims
      POSTGRES_DB: aims
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data

  backend:
    build:
      context: .
      dockerfile: Dockerfile.backend
    ports:
      - "8001:8001"
    environment:
      DATABASE_URL: postgresql://aims:aims@postgres:5432/aims
      REDIS_URL: redis://redis:6379
    depends_on:
      - postgres
      - redis
    volumes:
      - ./backend:/app/backend
      - ./prompts:/app/prompts

  frontend:
    build:
      context: .
      dockerfile: Dockerfile.frontend
    ports:
      - "7860:7860"
    depends_on:
      - backend

volumes:
  postgres_data:
  redis_data:
```

## Deployment Steps

### Local Testing

1. **Build the Docker image:**
   ```bash
   docker build -t aims:latest .
   docker run -p 7860:7860 aims:latest
   ```

2. **Test in browser:**
   ```
   http://localhost:7860
   ```

### Push to Hugging Face

1. **Add files to Space:**
   ```bash
   git add .
   git commit -m "Deploy AIMS to Hugging Face"
   git push
   ```

2. **Monitor deployment:**
   - Go to your Space URL
   - Check "Logs" tab for build status
   - Space will auto-build and deploy

3. **Access your deployment:**
   ```
   https://huggingface.co/spaces/<your-username>/autonomous-incident-management
   ```

## Accessing Your Deployed App

- **Frontend URL**: `https://huggingface.co/spaces/<your-username>/autonomous-incident-management`
- **API Documentation**: Will be embedded in the interface
- **Backend API**: Available at `/api` endpoint (if full stack deployed)

## Environment Variables in HF Spaces

1. Go to Space Settings
2. Click "Repository secrets"
3. Add your secrets:
   - `OPENAI_API_KEY`
   - `ANTHROPIC_API_KEY`
   - `SLACK_BOT_TOKEN`
   - `DATABASE_URL`
   - `REDIS_URL`
   - etc.

## Production Considerations

### Performance Optimization

1. **Frontend Build:**
   - Use production build
   - Enable gzip compression
   - Minimize bundle size

2. **Backend:**
   - Use connection pooling
   - Enable caching
   - Optimize database queries

### Security

1. **API Keys:**
   - Use HF Spaces secrets
   - Never commit to repository
   - Rotate keys regularly

2. **CORS:**
   - Configure for your domain
   - Validate requests
   - Use HTTPS only

### Scaling

For high traffic:
1. Use Hugging Face Pro subscription
2. Enable persistent storage
3. Implement rate limiting
4. Monitor performance metrics

## Troubleshooting

### Build Fails

**Error**: `Docker build failed`
- Check Dockerfile syntax
- Verify all files are present
- Review build logs in Space

### App Crashes

**Error**: `Port already in use`
- Hugging Face uses port 7860
- Update your app to use this port
- Check docker-compose ports

### Database Connection Issues

**Error**: `Cannot connect to database`
- Verify DATABASE_URL in secrets
- Check network connectivity
- Ensure database is running

### CORS Errors

**Error**: `Access-Control-Allow-Origin` missing
- Update CORS_ORIGINS in .env
- Rebuild and redeploy
- Clear browser cache

## API Documentation

Your deployed system includes:

- **Swagger UI**: `/docs` endpoint
- **ReDoc**: `/redoc` endpoint
- **OpenAPI Schema**: `/openapi.json`

## Monitoring & Logs

1. **HF Spaces Logs:**
   - Go to Space Settings
   - Click "Logs" tab
   - View real-time output

2. **Application Logs:**
   - Check backend logs
   - Monitor frontend errors
   - Track API requests

## Next Steps

1. **Customize:**
   - Add your branding
   - Modify UI colors
   - Customize workflows

2. **Integrate:**
   - Connect to your monitoring system
   - Add authentication
   - Implement webhooks

3. **Scale:**
   - Add more services
   - Implement load balancing
   - Optimize performance

## Support & Resources

- **Hugging Face Docs**: https://huggingface.co/docs/hub/spaces
- **Docker Docs**: https://docs.docker.com
- **FastAPI Docs**: https://fastapi.tiangolo.com
- **React Docs**: https://react.dev

---

**Happy deploying! 🚀**
