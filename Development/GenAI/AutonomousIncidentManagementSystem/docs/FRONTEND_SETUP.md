# 🎨 Frontend Setup Guide

## Quick Start (2 minutes)

### Step 1: Open Frontend Directory
```bash
cd /Users/deb/Development/GenAI/AutonomousIncidentManagementSystem/frontend
```

### Step 2: Install Dependencies
```bash
npm install
```

**Wait time**: ~2-3 minutes for first install

### Step 3: Start Development Server
```bash
npm run dev
```

**Expected output:**
```
  VITE v5.0.0  ready in 123 ms

  ➜  Local:   http://localhost:3000/
  ➜  press h to show help
```

### Step 4: Open in Browser
```bash
# Automatically or manually open:
http://localhost:3000
```

### Step 5: Verify Connection
- Check "Dashboard" tab
- Should show "✅ Healthy"
- Should see system statistics

---

## ✅ Verification Checklist

After starting frontend:

- [ ] Frontend loads at http://localhost:3000
- [ ] Dashboard tab shows health status
- [ ] Can see system statistics
- [ ] Alerts tab loads with table
- [ ] Can switch between tabs
- [ ] No console errors in browser DevTools

If any checks fail, see troubleshooting below.

---

## 🧪 Testing the Frontend

### Test 1: View Dashboard
1. Click "Dashboard" tab
2. Check health status (should be ✅ Healthy)
3. Verify 4 statistics cards appear

### Test 2: Create Alert
1. Click "Create Alert" tab
2. Fill form:
   - Source: `prometheus`
   - Source ID: `test_001`
   - Title: `Test Alert from Frontend`
   - Severity: `HIGH`
3. Click "Create Alert"
4. Should see success message

### Test 3: View Alerts
1. Click "Alerts" tab
2. Should see your newly created alert
3. Check pagination (if more than 10 alerts)
4. Click "Refresh" button

### Test 4: View Incidents
1. Click "Incidents" tab
2. Should see incident list (may be empty initially)
3. Click "Refresh" button

---

## 📦 What's Included

### Components
- ✅ **Dashboard** - Health and stats
- ✅ **AlertsList** - View alerts
- ✅ **CreateAlert** - Create new alerts  
- ✅ **IncidentsList** - View incidents

### Features
- ✅ Real-time updates (auto-refresh)
- ✅ Material-UI design
- ✅ Responsive layout
- ✅ Error handling
- ✅ Form validation
- ✅ TypeScript support

---

## 🐛 Troubleshooting

### Problem: "npm: command not found"
**Solution:**
```bash
# Install Node.js from https://nodejs.org/
# Or use Homebrew
brew install node
```

### Problem: "Port 3000 already in use"
**Solution:**
```bash
# Use different port
npm run dev -- --port 3001
```

### Problem: "Cannot connect to backend"
**Solution:**
```bash
# Verify backend is running
curl http://localhost:8001/api/v1/health

# Should return JSON response
# If not, restart backend:
cd ../backend
docker compose up -d
```

### Problem: "npm install fails"
**Solution:**
```bash
# Clear npm cache
npm cache clean --force

# Remove node_modules
rm -rf node_modules

# Reinstall
npm install
```

### Problem: CORS errors in browser console
**Solution:**
- Backend CORS middleware issue
- Restart backend: `docker compose restart backend`
- Check backend .env file

### Problem: "Module not found" errors
**Solution:**
```bash
# Reinstall dependencies
npm install

# Clear cache
npm cache clean --force
```

---

## 📝 Environment Configuration

### Backend URL
Currently hardcoded to `http://localhost:8001`

To change:
1. Edit `src/api.ts`
2. Change `const API_BASE = '...'`
3. Restart frontend: `npm run dev`

### API Proxy
Configured in `vite.config.ts`:
```typescript
proxy: {
  '/api': {
    target: 'http://localhost:8001',
    changeOrigin: true,
  }
}
```

---

## 🚀 Next Steps

After verifying frontend works:

1. **Test the full flow**:
   - Create alert from frontend
   - View in alerts list
   - Check backend API docs (http://localhost:8001/docs)

2. **Customize**:
   - Edit colors in components
   - Add more features
   - Modify API calls

3. **Deploy**:
   - Build: `npm run build`
   - Upload `dist/` folder to web server
   - Point to production API

---

## 📚 Useful Commands

```bash
# Development
npm run dev          # Start dev server
npm run build        # Build for production
npm run preview      # Preview production build
npm run lint         # Check code quality

# Debugging
npm run dev -- --inspect   # Debug mode
npm run build -- --watch   # Watch mode

# Cleaning
npm cache clean --force    # Clear cache
rm -rf node_modules        # Remove dependencies
```

---

## 🎯 API Endpoints Used

The frontend calls these backend endpoints:

```
GET  /api/v1/health              # Health check
GET  /api/v1/stats               # System statistics
GET  /api/v1/alerts              # List alerts
POST /api/v1/alerts              # Create alert
GET  /api/v1/incidents           # List incidents
```

See full API docs: http://localhost:8001/docs

---

## ✨ Success!

Once you see the dashboard loading with system statistics, the frontend is working correctly! 🎉

**Now you can:**
- Create alerts from the UI
- View incident list
- Monitor system health
- Test the full AIMS system

---

**Happy testing! 🚀**
