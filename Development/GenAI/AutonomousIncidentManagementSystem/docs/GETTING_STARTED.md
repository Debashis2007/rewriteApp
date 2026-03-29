# Getting Started - Autonomous Incident Management System

Welcome! This guide will walk you through setting up and using the AIMS framework.

---

## 📋 Prerequisites

Before you begin, ensure you have:
- **Docker** (v20.10+) and **Docker Compose** (v2.0+)
- **Python 3.10+** (if running without Docker)
- **Git** (for version control)
- **API Keys** (optional but recommended):
  - OpenAI API key (for GPT-4 access)
  - Anthropic API key (for Claude access)
  - Slack Bot token (for notifications)

### Check Prerequisites
```bash
# Check Docker
docker --version
docker-compose --version

# Check Python
python3 --version

# Check Git
git --version
```

---

## 🚀 Quick Start (5 minutes with Docker)

### Step 1: Clone the Repository
```bash
cd /Users/deb/Development/GenAI/AutonomousIncidentManagementSystem
```

### Step 2: Set Up Environment Variables
```bash
# Copy the template
cp backend/.env.template backend/.env

# Edit the .env file with your settings
# Minimum required:
# - OPENAI_API_KEY=your-key-here
# - ANTHROPIC_API_KEY=your-key-here (optional)

nano backend/.env
```

### Step 3: Start All Services
```bash
# Start PostgreSQL, Redis, and Backend API
docker-compose up --build

# Output should show:
# postgres_1 | database system is ready to accept connections
# redis_1   | Ready to accept connections
# backend_1 | INFO:     Uvicorn running on http://0.0.0.0:8000
```

### Step 4: Verify Services
```bash
# Open new terminal tab
curl http://localhost:8000/health

# Expected response:
# {"status":"healthy","timestamp":"2026-03-28T...","version":"0.1.0"}
```

### Step 5: Access API Documentation
```
# Open in browser:
http://localhost:8000/docs           # Swagger UI
http://localhost:8000/redoc          # ReDoc documentation
```

✅ **You're running!** The system is now ready to use.

---

## 🔧 Local Setup (Without Docker)

### Step 1: Install Python Dependencies
```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install packages
pip install -r requirements.txt
```

### Step 2: Set Up Databases
```bash
# Start PostgreSQL (if not already running)
# macOS: brew services start postgresql@15
# Linux: sudo systemctl start postgresql

# Start Redis
# macOS: brew services start redis
# Linux: sudo systemctl start redis-server

# Verify connections
psql -U postgres -c "SELECT 1"
redis-cli ping  # Should respond: PONG
```

### Step 3: Create Environment File
```bash
# Copy template
cp .env.template .env

# Edit with your API keys
nano .env
```

### Step 4: Initialize Database
```bash
# Run in Python shell
python3 -c "
from src.database import init_db
init_db()
print('Database initialized successfully!')
"
```

### Step 5: Start Backend Server
```bash
# Run the server
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000

# Or use the provided task:
# VS Code: Ctrl+Shift+B (Run Build Task)
```

---

## 📡 Using the API

### 1. Send Your First Alert

```bash
curl -X POST http://localhost:8000/api/v1/alerts \
  -H "Content-Type: application/json" \
  -d '{
    "source": "prometheus",
    "alert_name": "HighCPUUsage",
    "severity": "HIGH",
    "description": "CPU usage exceeds 80%",
    "service": "api-server",
    "tags": {
      "environment": "production",
      "region": "us-east-1"
    }
  }'

# Response:
# {
#   "id": "alert_12345",
#   "status": "NEW",
#   "source": "prometheus",
#   "created_at": "2026-03-28T10:30:00Z"
# }
```

### 2. Get Recent Alerts

```bash
curl http://localhost:8000/api/v1/alerts

# Response (paginated):
# {
#   "items": [
#     {
#       "id": "alert_12345",
#       "source": "prometheus",
#       "status": "NEW",
#       ...
#     }
#   ],
#   "total": 1,
#   "page": 1,
#   "per_page": 20
# }
```

### 3. Correlate Alerts

```bash
curl -X POST http://localhost:8000/api/v1/analysis/correlate \
  -H "Content-Type: application/json" \
  -d '{
    "alert_ids": ["alert_12345", "alert_12346"],
    "time_window_seconds": 300
  }'

# Response:
# {
#   "correlated": true,
#   "correlation_reason": "Same service, related error patterns",
#   "confidence": 0.92,
#   "incident_id": "inc_001"
# }
```

### 4. Analyze Incident (LLM)

```bash
curl -X POST http://localhost:8000/api/v1/analysis/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "incident_id": "inc_001",
    "llm_provider": "openai"
  }'

# Response:
# {
#   "analysis_id": "analysis_123",
#   "classification": "Infrastructure",
#   "severity": "CRITICAL",
#   "summary": "Multiple API servers experiencing high CPU load...",
#   "root_cause": "Database query timeout causing..."
# }
```

### 5. Get Recommendations

```bash
curl -X POST http://localhost:8000/api/v1/analysis/recommendations \
  -H "Content-Type: application/json" \
  -d '{
    "incident_id": "inc_001",
    "llm_provider": "openai"
  }'

# Response:
# {
#   "recommendations": [
#     {
#       "action": "Scale API servers horizontally",
#       "priority": "HIGH",
#       "estimated_time": "5 minutes",
#       "commands": ["kubectl scale deployment api-server --replicas=5"]
#     }
#   ]
# }
```

### 6. Send Notifications

```bash
curl -X POST http://localhost:8000/api/v1/incidents/inc_001/notify \
  -H "Content-Type: application/json" \
  -d '{
    "channels": ["slack", "email"],
    "message": "Custom notification message",
    "include_analysis": true
  }'

# Response:
# {
#   "notification_ids": [
#     "notif_slack_123",
#     "notif_email_456"
#   ],
#   "status": "sent"
# }
```

---

## 🤖 Using LLM Integration

### Configure LLM Provider

#### Option 1: OpenAI (Default)
```bash
# Set in .env
LLM_PROVIDER=openai
OPENAI_API_KEY=sk-...
OPENAI_MODEL=gpt-4
```

#### Option 2: Anthropic
```bash
# Set in .env
LLM_PROVIDER=anthropic
ANTHROPIC_API_KEY=sk-ant-...
ANTHROPIC_MODEL=claude-3-sonnet-20240229
```

### Use LLM for Analysis

```python
# In your Python code:
from src.llm.client import LLMFactory

# Create client (uses provider from settings)
llm_client = LLMFactory.create_client()

# Get a prompt template
prompt_template = llm_client.prompt_manager.get_prompt_template(
    "alert_correlation"
)

# Use it to analyze
response = await llm_client.chat([
    {
        "role": "user",
        "content": prompt_template.format(
            alerts=alert_list,
            time_window=300
        )
    }
])

# Parse result
import json
result = json.loads(response)
```

### Available Prompts

Located in `/prompts` directory:

1. **alert_normalization.md** - Normalize alerts from different sources
2. **alert_correlation.md** - Group related alerts
3. **incident_classification.md** - Categorize incidents
4. **root_cause_analysis.md** - Identify root causes
5. **incident_recommendation.md** - Generate remediation steps
6. **autonomous_response.md** - Plan automated responses

---

## 🔔 Setting Up Notifications

### Slack Notifications

```bash
# 1. Create Slack App at https://api.slack.com/apps
# 2. Enable Bot Token Scopes:
#    - chat:write
#    - chat:write.public
#    - files:write

# 3. Set in .env
SLACK_BOT_TOKEN=xoxb-...
SLACK_CHANNEL=alerts

# 4. Test
curl -X POST http://localhost:8000/api/v1/incidents/inc_001/notify \
  -H "Content-Type: application/json" \
  -d '{"channels": ["slack"]}'
```

### Email Notifications

```bash
# Set in .env
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your-email@gmail.com
SMTP_PASSWORD=app-specific-password
SMTP_FROM=alerts@yourdomain.com

# Recipients are set per-incident or per-user
```

### Webhook Notifications

```bash
# Set in .env
WEBHOOK_URL=https://your-service/webhooks/incidents

# System will POST incident data to this URL
# Payload includes: incident_id, status, analysis, recommendations
```

### PagerDuty Notifications

```bash
# Set in .env
PAGERDUTY_API_KEY=xxx
PAGERDUTY_SERVICE_ID=xxx

# System will automatically create/update incidents in PagerDuty
```

---

## 📊 Example Workflows

### Workflow 1: Alert → Incident → Analysis → Notification

```bash
#!/bin/bash

# 1. Receive alert from monitoring
ALERT=$(curl -X POST http://localhost:8000/api/v1/alerts \
  -H "Content-Type: application/json" \
  -d '{
    "source": "datadog",
    "alert_name": "DatabaseConnPoolExhausted",
    "severity": "CRITICAL",
    "service": "payment-api"
  }')

ALERT_ID=$(echo $ALERT | jq -r '.id')
echo "Alert created: $ALERT_ID"

# 2. Correlate with other recent alerts
CORRELATED=$(curl -X POST http://localhost:8000/api/v1/analysis/correlate \
  -H "Content-Type: application/json" \
  -d "{\"alert_ids\": [\"$ALERT_ID\"]}")

INCIDENT_ID=$(echo $CORRELATED | jq -r '.incident_id')
echo "Incident created: $INCIDENT_ID"

# 3. Analyze with LLM
ANALYSIS=$(curl -X POST http://localhost:8000/api/v1/analysis/analyze \
  -H "Content-Type: application/json" \
  -d "{\"incident_id\": \"$INCIDENT_ID\", \"llm_provider\": \"openai\"}")

echo "Analysis: $(echo $ANALYSIS | jq -r '.summary')"

# 4. Get recommendations
RECOMMENDATIONS=$(curl -X POST http://localhost:8000/api/v1/analysis/recommendations \
  -H "Content-Type: application/json" \
  -d "{\"incident_id\": \"$INCIDENT_ID\", \"llm_provider\": \"openai\"}")

echo "Recommendations: $(echo $RECOMMENDATIONS | jq '.recommendations[0].action')"

# 5. Send notification
curl -X POST http://localhost:8000/api/v1/incidents/$INCIDENT_ID/notify \
  -H "Content-Type: application/json" \
  -d '{"channels": ["slack", "email"]}'

echo "Notification sent!"
```

### Workflow 2: Autonomous Response (With Safeguards)

```bash
# Get recommendations
RECOMMENDATIONS=$(curl -X POST http://localhost:8000/api/v1/analysis/recommendations \
  -H "Content-Type: application/json" \
  -d '{"incident_id": "inc_001"}')

# Check if action is safe for automation (severity, approval status)
IS_AUTO_SAFE=$(echo $RECOMMENDATIONS | jq '.recommendations[0].auto_executable')

if [ "$IS_AUTO_SAFE" = "true" ]; then
  # Execute automated response
  curl -X POST http://localhost:8000/api/v1/incidents/inc_001/execute-response \
    -H "Content-Type: application/json" \
    -d '{
      "recommendation_id": "rec_123",
      "approval_status": "approved"
    }'
  
  echo "Automated response executed!"
else
  echo "Manual approval required - waiting for operator..."
fi
```

---

## 🧪 Testing the System

### Using Postman/Insomnia

1. Open Postman/Insomnia
2. Import the API spec from: `http://localhost:8000/openapi.json`
3. Use pre-built requests to test endpoints

### Using cURL (Command Line)

```bash
# Get system stats
curl http://localhost:8000/api/v1/stats

# Get all incidents (paginated)
curl "http://localhost:8000/api/v1/incidents?page=1&per_page=10&status=OPEN"

# Get incident timeline
curl http://localhost:8000/api/v1/incidents/inc_001/timeline

# Add comment to incident
curl -X POST http://localhost:8000/api/v1/incidents/inc_001/comments \
  -H "Content-Type: application/json" \
  -d '{"text": "Working on this now"}'
```

### Using Python

```python
import requests
import json

BASE_URL = "http://localhost:8000/api/v1"

# Create alert
alert_response = requests.post(
    f"{BASE_URL}/alerts",
    json={
        "source": "prometheus",
        "alert_name": "TestAlert",
        "severity": "MEDIUM",
        "service": "test-service"
    }
)
alert_id = alert_response.json()["id"]

# Correlate alerts
correlation_response = requests.post(
    f"{BASE_URL}/analysis/correlate",
    json={
        "alert_ids": [alert_id],
        "time_window_seconds": 300
    }
)

# Analyze
analysis_response = requests.post(
    f"{BASE_URL}/analysis/analyze",
    json={
        "incident_id": correlation_response.json()["incident_id"],
        "llm_provider": "openai"
    }
)

print("Analysis:", json.dumps(analysis_response.json(), indent=2))
```

---

## 🐛 Troubleshooting

### Issue: Docker containers won't start
```bash
# Check Docker is running
docker ps

# Check logs
docker-compose logs

# Restart containers
docker-compose down
docker-compose up --build

# Remove and rebuild
docker-compose down -v
docker-compose up --build
```

### Issue: API returns 500 error
```bash
# Check backend logs
docker-compose logs backend

# Verify environment variables
docker exec aims-backend cat /app/.env

# Check database connection
docker-compose logs postgres
```

### Issue: OpenAI API key not working
```bash
# Verify key format
echo $OPENAI_API_KEY  # Should start with 'sk-'

# Test key in .env
OPENAI_API_KEY=your-actual-key-here

# Restart backend
docker-compose restart backend
```

### Issue: Slack notifications not sending
```bash
# Verify token
echo $SLACK_BOT_TOKEN

# Check Slack channel exists
# Verify bot has permission to post

# Test notification endpoint
curl -X POST http://localhost:8000/api/v1/incidents/test/notify \
  -H "Content-Type: application/json" \
  -d '{"channels": ["slack"]}'
```

---

## 📚 Understanding the Architecture

### Request Flow

```
Client Request
    ↓
API Router (src/api/routes.py)
    ↓
Pydantic Validation (src/schemas.py)
    ↓
Service Layer (src/services/core.py)
    ├─ Database Operations (SQLAlchemy)
    ├─ LLM Integration (src/llm/client.py)
    └─ Notifications (src/notifications/service.py)
    ↓
Database (PostgreSQL)
    ↓
Response to Client
```

### File Organization

```
backend/
├── src/
│   ├── main.py                 # FastAPI app entry point
│   ├── database.py             # SQLAlchemy setup
│   ├── schemas.py              # Pydantic models
│   ├── config/
│   │   └── settings.py         # Configuration
│   ├── models/
│   │   └── database.py         # ORM models (14 tables)
│   ├── services/
│   │   └── core.py             # Business logic (5 services)
│   ├── api/
│   │   └── routes.py           # API endpoints (15+)
│   ├── llm/
│   │   └── client.py           # LLM integration
│   └── notifications/
│       └── service.py          # Notification system
├── requirements.txt            # Python dependencies
└── .env.template              # Environment variables
```

---

## 🔑 Key Concepts

### Alert
- Raw event from a monitoring system
- May represent false alarm or noise
- Example: CPU > 80%, Disk space low

### Incident
- Grouped related alerts
- Represents actual operational issue
- Requires investigation and resolution

### Analysis
- LLM-powered insights
- Classification, RCA, recommendations
- Stored for audit trail

### Recommendation
- Remediation steps
- Priority and estimated time
- Can be auto-executed or manual

### Notification
- Alert humans about incidents
- Multi-channel (Slack, email, etc.)
- Includes analysis and recommendations

---

## 📖 Next Steps

1. **Deploy Locally** - Follow Quick Start above
2. **Send Test Alerts** - Use API examples
3. **Configure Notifications** - Set up Slack/email
4. **Review Analysis** - Verify LLM integration
5. **Explore Dashboard** - Access Swagger UI at `/docs`
6. **Read Implementation Guide** - See `backend/README.md`
7. **Review Design** - See `doc/DESIGN.md`
8. **Contribute** - Begin Phase 2 implementation

---

## 📞 Getting Help

- **API Documentation**: http://localhost:8000/docs
- **Architecture Guide**: See `doc/DESIGN.md`
- **Backend Guide**: See `backend/README.md`
- **Requirements**: See `requirements/REQUIREMENTS.md`
- **Prompts**: See `prompts/*.md`

---

## ✅ Checklist

Before going to production:

- [ ] Configure all API keys (OpenAI, Slack, etc.)
- [ ] Set up database backups
- [ ] Configure monitoring and logging
- [ ] Set up SSL/TLS certificates
- [ ] Implement authentication
- [ ] Run full test suite
- [ ] Performance test with load
- [ ] Security audit completed
- [ ] Documentation updated
- [ ] Team trained on platform

---

**You're all set! Start sending alerts and let AIMS do the work! 🚀**
