# Troubleshooting Setup Issues

## Error: `docker-compose: command not found` or Docker daemon not running

### Problem
```
Cannot connect to the Docker daemon at unix:///Users/deb/.docker/run/docker.sock
docker-compose: command not found
```

### Solutions

#### Solution 1: Start Docker Desktop (Recommended for macOS)

1. **Open Docker Desktop:**
   ```bash
   open /Applications/Docker.app
   ```

2. **Wait for Docker to start** (watch the menu bar for Docker icon)
   - Should show "Docker is running" when ready
   - Takes 30-60 seconds

3. **Verify Docker is running:**
   ```bash
   docker ps
   # Should output: CONTAINER ID   IMAGE   COMMAND...
   ```

#### Solution 2: Use `docker compose` (new syntax)

Modern Docker Desktop includes `docker compose` (without hyphen). Update commands:

**Old:** `docker-compose up --build`
**New:** `docker compose up --build`

```bash
# Navigate to project
cd /Users/deb/Development/GenAI/AutonomousIncidentManagementSystem

# Use docker compose (new syntax)
docker compose up --build
```

#### Solution 3: Install docker-compose separately (if needed)

```bash
# Using Homebrew
brew install docker-compose

# Verify
docker-compose --version
```

---

## Step-by-Step Fix

### Step 1: Start Docker
```bash
# On macOS, open Docker Desktop
open /Applications/Docker.app

# Wait 60 seconds for it to start, then verify:
docker ps
```

**Expected output:**
```
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```

### Step 2: Copy Environment File
```bash
cd /Users/deb/Development/GenAI/AutonomousIncidentManagementSystem
cp backend/.env.template backend/.env
```

### Step 3: Start Services (use correct syntax)

**Option A: Using `docker compose` (recommended)**
```bash
docker compose up --build
```

**Option B: Using `docker-compose`** (if installed)
```bash
docker-compose up --build
```

### Step 4: Wait for Services to Start

You should see output like:
```
postgres_1 | database system is ready to accept connections
redis_1   | Ready to accept connections
backend_1 | INFO:     Uvicorn running on http://0.0.0.0:8000
```

### Step 5: Verify in New Terminal

```bash
# Open new terminal tab (Cmd+T)
sleep 5  # Wait for services to fully start

# Test health check
curl http://localhost:8000/health

# Should return:
# {"status":"healthy","timestamp":"...","version":"0.1.0"}
```

---

## Common Errors & Fixes

### Error 1: Port Already in Use
```
Error: Port 8000 is already in use
```

**Fix:**
```bash
# Stop existing containers
docker compose down

# Or use different port
docker compose up --build -p 8001:8000
```

### Error 2: Database Connection Failed
```
Error: could not connect to server: Connection refused
```

**Fix:**
```bash
# Stop and restart everything
docker compose down -v
docker compose up --build
```

### Error 3: Out of Memory
```
Error: Cannot allocate memory
```

**Fix:**
```bash
# Increase Docker Desktop memory
# Docker Desktop > Settings > Resources > Memory: 4GB or 8GB

# Restart Docker Desktop
pkill -f Docker
sleep 5
open /Applications/Docker.app
```

### Error 4: Python Package Installation Failed
```
error: Failed building wheel for psycopg2
```

**Fix:**
```bash
# Rebuild Docker image from scratch
docker compose down -v
docker system prune -a
docker compose up --build --no-cache
```

---

## Manual Setup (Without Docker)

If you prefer to run without Docker:

### Prerequisites
```bash
# Install PostgreSQL
brew install postgresql@15

# Install Redis
brew install redis

# Install Python packages
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Start Services Manually

```bash
# Terminal 1: Start PostgreSQL
brew services start postgresql@15
# Verify: psql -U postgres -c "SELECT 1"

# Terminal 2: Start Redis
brew services start redis
# Verify: redis-cli ping  # Should return: PONG

# Terminal 3: Start Backend
cd backend
source venv/bin/activate
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

### Test
```bash
# New terminal
curl http://localhost:8000/health
```

---

## Verification Checklist

- [ ] Docker Desktop is running (`docker ps` works)
- [ ] PostgreSQL is running (or Docker container started)
- [ ] Redis is running (or Docker container started)
- [ ] Backend is running (or `uvicorn` process started)
- [ ] Health check returns 200 (`curl http://localhost:8000/health`)
- [ ] API docs accessible (`http://localhost:8000/docs`)

---

## Quick Start Command (All-in-One)

After Docker is running:

```bash
cd /Users/deb/Development/GenAI/AutonomousIncidentManagementSystem && \
cp backend/.env.template backend/.env && \
docker compose up --build
```

Then in another terminal:
```bash
sleep 10 && curl http://localhost:8000/health
```

---

## Need More Help?

Check logs for details:
```bash
# See all services logs
docker compose logs

# See just backend logs
docker compose logs backend

# See just database logs
docker compose logs postgres

# Follow logs in real-time
docker compose logs -f backend
```

---

**Once you see "Uvicorn running on http://0.0.0.0:8000", you're ready to go! 🚀**
