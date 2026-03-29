# 🚀 Quick Start: Deploy AIMS to Hugging Face Spaces

## Option 1: Automated Deployment (Recommended)

### Run the deployment script:

```bash
cd /Users/deb/Development/GenAI/AutonomousIncidentManagementSystem
chmod +x deploy-huggingface.sh
./deploy-huggingface.sh
```

The script will:
- ✅ Check prerequisites
- ✅ Guide you through creating a Hugging Face Space
- ✅ Clone the Space repository
- ✅ Prepare AIMS files
- ✅ Push to Hugging Face
- ✅ Start the deployment

---

## Option 2: Manual Deployment

### Step 1: Create a Hugging Face Space

1. Go to https://huggingface.co/spaces
2. Click **"Create new Space"**
3. Fill in the form:
   - **Space name**: `autonomous-incident-management`
   - **License**: MIT
   - **SDK**: Docker
4. Click **"Create space"**

### Step 2: Clone the Space

```bash
# Replace <username> with your Hugging Face username
git clone https://huggingface.co/spaces/<username>/autonomous-incident-management
cd autonomous-incident-management
```

### Step 3: Add AIMS Files

```bash
# Copy frontend (recommended for quick deployment)
cp -r ../AutonomousIncidentManagementSystem/frontend .

# Copy backend (if deploying full stack)
cp -r ../AutonomousIncidentManagementSystem/backend .
cp -r ../AutonomousIncidentManagementSystem/prompts .

# Copy Dockerfile
cp ../AutonomousIncidentManagementSystem/Dockerfile.frontend-hf Dockerfile
# OR for full stack:
# cp ../AutonomousIncidentManagementSystem/Dockerfile.huggingface Dockerfile
```

### Step 4: Create Required Files

**Create `.gitattributes`:**
```
*.bin filter=lfs diff=lfs merge=lfs -text
```

**Create `README.md`:**
```markdown
# Autonomous Incident Management System (AIMS)

An intelligent, AI-powered incident management platform.

## Features

- Real-time alert management
- Incident correlation and analysis
- AI-powered RCA (Root Cause Analysis)
- Multi-channel notifications
- RESTful API

## Usage

Access the dashboard at the Space URL.

## Documentation

- [Full Documentation](https://github.com/debashis2007/aims)
- [API Docs](/docs)

---
Deployed on Hugging Face Spaces with ❤️
```

### Step 5: Push to Hugging Face

```bash
git add .
git commit -m "Deploy AIMS - Autonomous Incident Management System"
git push
```

### Step 6: Monitor Deployment

1. Go to your Space URL
2. Click **"Logs"** tab
3. Wait for Docker build to complete
4. Once deployed, access your app

---

## Frontend-Only vs Full Stack

### 🟢 Frontend Only (Recommended)

**Pros:**
- ✅ Faster deployment (2-3 minutes)
- ✅ Lower resource usage
- ✅ Can use external backend
- ✅ Easy to update

**Cons:**
- ❌ Requires external API backend
- ❌ Limited by HF Spaces resources for backend

**Use when:** You have an existing backend API

**Dockerfile:**
```dockerfile
FROM node:18-alpine AS builder
# ... see Dockerfile.frontend-hf
```

### 🔵 Full Stack Deployment

**Pros:**
- ✅ Complete system in one place
- ✅ No external dependencies
- ✅ Self-contained

**Cons:**
- ❌ Longer deployment (5-15 minutes)
- ❌ Uses more resources
- ❌ Database runs in container (data lost on restart)

**Use when:** You want a complete demo system

**Dockerfile:**
```dockerfile
# Multi-stage build
# ... see Dockerfile.huggingface
```

---

## Environment Variables

### For Frontend-Only:

No special environment variables needed. The frontend will:
- Use `localhost:8001` for local backend
- Use `VITE_API_URL` if set

### For Full Stack:

Set in HF Spaces Settings → Repository Secrets:

```env
OPENAI_API_KEY=your_key_here
ANTHROPIC_API_KEY=your_key_here
SLACK_BOT_TOKEN=your_token_here
DATABASE_URL=postgresql://aims:aims@localhost:5432/aims
REDIS_URL=redis://localhost:6379
```

---

## Accessing Your Deployment

### Frontend URL
```
https://huggingface.co/spaces/<username>/autonomous-incident-management
```

### API Documentation (Full Stack Only)
```
https://huggingface.co/spaces/<username>/autonomous-incident-management/api/docs
```

---

## Troubleshooting

### Build Fails
```
Error: Docker build failed
```
**Solution:**
1. Check Dockerfile syntax
2. Verify all files exist
3. Review build logs
4. Ensure file sizes aren't too large

### App Crashes
```
Error: Application failed to start
```
**Solution:**
1. Check Space logs
2. Verify port is 7860
3. Check environment variables
4. Review application logs

### Can't Connect to API
```
Error: Failed to connect to backend
```
**Solution:**
1. Verify backend is running
2. Check CORS settings
3. Verify API endpoint URL
4. Check network connectivity

### Build Timeout
```
Error: Build exceeded time limit
```
**Solution:**
- Use frontend-only deployment
- Reduce image size
- Remove unnecessary files
- Increase build resources (requires HF Pro)

---

## Performance Tips

### For Frontend-Only:
1. Minify assets
2. Use gzip compression
3. Enable caching headers
4. Lazy load components

### For Full Stack:
1. Use connection pooling
2. Enable Redis caching
3. Optimize database queries
4. Use persistent storage (HF Pro feature)

---

## Updating Your Deployment

### To update the code:

```bash
cd autonomous-incident-management  # HF Space directory
git pull  # Get latest changes from HF
cp -r ../AutonomousIncidentManagementSystem/frontend .
git add .
git commit -m "Update AIMS frontend"
git push
```

The Space will automatically rebuild and deploy.

---

## Next Steps

1. ✅ Deploy to HF Spaces
2. 📝 Add your API keys
3. 🧪 Test the system
4. 🎨 Customize branding
5. 📊 Monitor performance
6. 🔧 Integrate with your services

---

## Resources

- **Hugging Face Docs**: https://huggingface.co/docs/hub/spaces
- **Docker Docs**: https://docs.docker.com
- **FastAPI**: https://fastapi.tiangolo.com
- **React**: https://react.dev

---

## Support

For issues or questions:
1. Check Space logs
2. Review error messages
3. Check HF documentation
4. Create an issue on GitHub

---

**Happy deploying! 🚀**
