# Deploying AIMS to Hugging Face Spaces

## Step 1: Create a Hugging Face Space

1. Go to: https://huggingface.co/debashis2007
2. Click **"Create new"** → **"Space"**
3. Fill in:
   - **Space name**: `autonomous-incident-management`
   - **Space type**: `Docker` (important!)
   - **Visibility**: `Public` (or Private)
4. Click **"Create Space"**

## Step 2: Clone Your Space

```bash
# After creating the space, clone it
cd /tmp
git clone https://huggingface.co/spaces/debashis2007/autonomous-incident-management
cd autonomous-incident-management
```

## Step 3: Copy AIMS Files

```bash
# From the AIMS project directory
cd /Users/deb/Development/GenAI/AutonomousIncidentManagementSystem

# Copy the appropriate Dockerfile
# Option A: Frontend only (FAST - 2-3 min)
cp Dockerfile.frontend-hf /tmp/autonomous-incident-management/Dockerfile

# Option B: Full stack (COMPLETE - 5-15 min)
# cp Dockerfile.huggingface /tmp/autonomous-incident-management/Dockerfile

# Copy the entire project
cp -r frontend /tmp/autonomous-incident-management/
cp -r backend /tmp/autonomous-incident-management/
cp -r prompts /tmp/autonomous-incident-management/
```

## Step 4: Configure for Deployment

```bash
cd /tmp/autonomous-incident-management

# Create a startup script
cat > start.sh << 'EOF'
#!/bin/bash
cd /app
npm install
npm run build
npm run preview -- --host 0.0.0.0 --port 7860
EOF

chmod +x start.sh
```

## Step 5: Add .dockerignore

```bash
cat > .dockerignore << 'EOF'
node_modules
dist
__pycache__
*.pyc
.git
.env
.DS_Store
.venv
venv
*.log
EOF
```

## Step 6: Push to Hugging Face

```bash
cd /tmp/autonomous-incident-management

git add .
git commit -m "Initial AIMS deployment"
git push origin main

# The space will automatically start building
```

## Step 7: Monitor the Build

1. Go to: https://huggingface.co/spaces/debashis2007/autonomous-incident-management
2. Click **"Build"** tab to see logs
3. Wait for "Successfully built" message
4. Your space URL: `https://debashis2007-autonomous-incident-management.hf.space`

## What Gets Deployed

### Frontend-Only Option (RECOMMENDED)
- ✅ React dashboard
- ✅ Alert management
- ✅ Incident tracking
- ❌ No backend (connect to external API)
- ⏱️ **2-3 minutes to deploy**
- 📦 ~100MB

### Full-Stack Option
- ✅ React frontend
- ✅ FastAPI backend
- ✅ PostgreSQL database
- ✅ Redis cache
- ✅ Ollama LLM support
- ✅ Complete system
- ⏱️ **5-15 minutes to deploy**
- 📦 ~1GB

## Post-Deployment Configuration

### For Full-Stack Deployment

Add environment variables in Space Settings:

```
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=mistral

# Optional: For external services
SLACK_BOT_TOKEN=xoxb-...
EMAIL_SMTP_USER=your-email@gmail.com
```

## Testing Your Deployment

```bash
# Frontend-only
curl https://debashis2007-autonomous-incident-management.hf.space/

# Full-stack API
curl https://debashis2007-autonomous-incident-management.hf.space/api/v1/health
```

## Troubleshooting

**Build Failed:**
- Check the "Build" tab for error messages
- Ensure Docker file is correct
- Check that all required files are present

**Space Not Responding:**
- Check available hardware (CPU/RAM)
- Review logs in "Build" section
- Try restarting the space in settings

**Connection Refused:**
- Ensure ports are correctly configured
- Check Dockerfile for port exposure
- Verify environment variables

## Dashboard Access

After deployment:

```
https://debashis2007-autonomous-incident-management.hf.space
```

You'll see:
- Real-time system health
- Alert management interface
- Incident tracking
- AI-powered insights (with Ollama in full-stack)

## Making Changes

To update your deployment:

```bash
cd /tmp/autonomous-incident-management
# Make your changes
git add .
git commit -m "Update configuration"
git push origin main

# Space automatically rebuilds
```

## Share Your Space

Your space URL:
```
https://huggingface.co/spaces/debashis2007/autonomous-incident-management
```

You can:
- ✅ Share the URL with team members
- ✅ Embed in your portfolio
- ✅ Use as a demo
- ✅ Integrate with other services

---

## Quick Reference

| Step | Command |
|------|---------|
| Clone | `git clone https://huggingface.co/spaces/debashis2007/autonomous-incident-management` |
| Copy Files | `cp -r frontend backend prompts /tmp/autonomous-incident-management/` |
| Copy Docker | `cp Dockerfile.frontend-hf Dockerfile` |
| Deploy | `git add . && git commit -m "Deploy" && git push` |
| Monitor | Visit **Build** tab on HF Space |
| Access | `https://debashis2007-autonomous-incident-management.hf.space` |

---

## Next: Authenticate with Hugging Face

```bash
# If not authenticated, login first
huggingface-cli login

# Follow the prompts to authenticate with your token
```

You can get your token from: https://huggingface.co/settings/tokens

