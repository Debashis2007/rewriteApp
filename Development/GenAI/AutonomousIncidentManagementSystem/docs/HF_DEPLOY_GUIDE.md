# Deploy to Hugging Face Spaces - Step by Step

Your Autonomous Incident Management System is ready to deploy!

**Target:** https://huggingface.co/spaces/debashis2007/IncidentMgmtSystem

## Quick Start (3 ways to deploy)

### Method 1: Automated Script (Easiest)
```bash
cd /Users/deb/Development/GenAI/AutonomousIncidentManagementSystem
./hf-deploy.sh
```
Follow the prompts - script handles everything!

### Method 2: Manual Deployment (Recommended for full control)
Follow the steps below.

### Method 3: Manual GitHub-style Deployment
Use `git` directly to manage the Space.

---

## Manual Deployment Steps

### Step 1: Create Hugging Face Space (if needed)
1. Go to: https://huggingface.co/spaces
2. Click "Create new Space"
3. Fill in:
   - **Name:** `IncidentMgmtSystem`
   - **Owner:** `debashis2007`
   - **License:** `MIT`
   - **SDK:** `Docker`
4. Click "Create Space"

### Step 2: Clone Space to Your Machine
```bash
git clone https://huggingface.co/spaces/debashis2007/IncidentMgmtSystem
cd IncidentMgmtSystem
```

### Step 3: Choose Deployment Type

#### Option A: Frontend-Only (⚡ RECOMMENDED - 2-3 minutes)
```bash
# Copy frontend files
cp /Users/deb/Development/GenAI/AutonomousIncidentManagementSystem/frontend/* .

# Copy Docker config
cp /Users/deb/Development/GenAI/AutonomousIncidentManagementSystem/Dockerfile.frontend-hf Dockerfile
cp /Users/deb/Development/GenAI/AutonomousIncidentManagementSystem/.dockerignore .

# Clean build artifacts
rm -rf node_modules package-lock.json
```

#### Option B: Full-Stack (🔵 5-15 minutes)
```bash
# Copy all components
mkdir -p backend frontend prompts

cp -r /Users/deb/Development/GenAI/AutonomousIncidentManagementSystem/backend/* backend/
cp -r /Users/deb/Development/GenAI/AutonomousIncidentManagementSystem/frontend/* frontend/
cp -r /Users/deb/Development/GenAI/AutonomousIncidentManagementSystem/prompts/* prompts/

# Copy Docker config
cp /Users/deb/Development/GenAI/AutonomousIncidentManagementSystem/Dockerfile.huggingface Dockerfile
cp /Users/deb/Development/GenAI/AutonomousIncidentManagementSystem/.dockerignore .

# Copy environment template
cp /Users/deb/Development/GenAI/AutonomousIncidentManagementSystem/backend/.env.template backend/.env
```

### Step 4: Clean Build Artifacts
```bash
# Remove build files (keeps space smaller)
find . -name "node_modules" -type d -exec rm -rf {} + 2>/dev/null || true
find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true
find . -name "dist" -type d -exec rm -rf {} + 2>/dev/null || true
```

### Step 5: Deploy to Hugging Face
```bash
# Add all files
git add -A

# Commit
git commit -m "Deploy AIMS - $(date '+%Y-%m-%d')"

# Push to Hugging Face
git push
```

### Step 6: Monitor Build Progress
1. Go to your Space: https://huggingface.co/spaces/debashis2007/IncidentMgmtSystem
2. Click "Logs" tab
3. Watch Docker build progress
4. Wait for build to complete (2-15 minutes depending on option)

### Step 7: Access Your Application
Once build completes:
- Space URL will show your running application
- Dashboard is at: https://huggingface.co/spaces/debashis2007/IncidentMgmtSystem

---

## Configuration

### Frontend-Only
- No configuration needed
- Update API backend URL in `api.ts` if connecting to external backend

### Full-Stack
Optional environment variables in Space Settings → Repository Secrets:

```
# Optional: Use OpenAI instead of Ollama
OPENAI_API_KEY=sk-your-key

# Optional: Use Anthropic instead of Ollama
ANTHROPIC_API_KEY=sk-ant-your-key

# Optional: Enable Slack notifications
SLACK_BOT_TOKEN=xoxb-your-token
```

Otherwise, system uses **Ollama** (free, no keys needed).

---

## What You Get

### Frontend-Only
✅ React dashboard with Material-UI  
✅ Real-time alerts management  
✅ Incident tracking  
✅ Visual statistics  
❌ LLM features (requires backend)

### Full-Stack
✅ Everything above PLUS:  
✅ Complete FastAPI backend  
✅ PostgreSQL database  
✅ Redis caching  
✅ Ollama LLM integration  
✅ Alert correlation  
✅ Incident classification  
✅ Root cause analysis  
✅ Recommendations  

---

## Troubleshooting

### Build is taking too long
- Frontend-only should take 2-3 minutes
- Full-stack can take 5-15 minutes
- Very large builds may timeout on free tier
  
**Solution:** Try frontend-only instead

### Docker build fails
1. Check build logs in Space "Logs" tab
2. Look for errors in output
3. Common issues:
   - Missing files: Verify all files copied correctly
   - Dockerfile path wrong: Check Dockerfile exists
   - Package issues: Try deleting `package-lock.json`

**Solution:** Delete and recreate Space, retry

### Can't access Space after build
1. Hard refresh browser: `Cmd+Shift+R` (Mac) or `Ctrl+Shift+R` (Windows)
2. Wait a few seconds for server to start
3. Check Space status in HF interface

**Solution:** Check Logs tab for startup errors

### Connection refused errors
- Frontend-only doesn't need backend
- Full-stack needs internal services running

**Solution:** Check Space Logs for service errors

### Space keeps restarting
- Common on CPU-only tier with large models
- May be out of memory

**Solution:** Upgrade to Pro or use frontend-only

---

## Performance Tips

### For Frontend-Only
- Build time: 2-3 minutes
- Size: ~100MB
- Runtime: Minimal resources
- **Best for:** Quick demos, dashboards

### For Full-Stack
- Build time: 5-15 minutes
- Size: ~1GB+
- Runtime: Moderate resources
- **Best for:** Complete system, full features

### Optimize Further
- Use smaller Docker base images
- Remove test files before deploying
- Compress assets
- Use full-stack only if needed

---

## Sharing Your Space

Once deployed, share at:
```
https://huggingface.co/spaces/debashis2007/IncidentMgmtSystem
```

### Share Options
1. Copy direct URL
2. Embed in website
3. Share via social media
4. Make Space public (default)
5. Add to organization

---

## Updating Your Space

To update after making changes:

```bash
cd path/to/space/repo

# Pull latest
git pull

# Make changes, then:
git add -A
git commit -m "Update description"
git push

# Space auto-rebuilds
```

---

## Cost & Quotas

### Free Tier (Community)
- ✅ Free compute (CPU)
- ✅ Free hosting
- ✅ Unlimited spaces
- ⏱️ May go to sleep if inactive
- ⏱️ ~5-10 minute startup time

### Paid Tiers
- **Pro ($15/month):** GPU, priority support, always on
- **GPU Upgrade:** $0.14-0.50/hour on top of Pro

### Space Quotas
- Storage: 200GB per Space
- Memory: ~8GB on CPU, 24GB on GPU
- Auto-sleep after inactivity

---

## Next Steps

✅ **Option 1:** Run automated script
```bash
./hf-deploy.sh
```

✅ **Option 2:** Follow manual steps above

✅ **Option 3:** Monitor deployment
- Go to: https://huggingface.co/spaces/debashis2007/IncidentMgmtSystem
- Click "Logs" to watch build
- Refresh after 2-15 minutes to see app

---

## Documentation

- **Quick Reference:** HUGGINGFACE_QUICKSTART.md
- **Full Details:** HUGGINGFACE_DEPLOYMENT.md
- **System Setup:** README.md
- **Ollama LLM:** OLLAMA_SETUP.md
- **HF Spaces Docs:** https://huggingface.co/docs/hub/spaces

---

## Questions?

1. Check the troubleshooting section above
2. Review HF Spaces documentation
3. Check Space Logs for errors
4. Visit: https://huggingface.co/docs/hub/spaces

---

## Good Luck! 🚀

Your AIMS system will be live soon!

Enjoy your incident management dashboard on Hugging Face Spaces!
