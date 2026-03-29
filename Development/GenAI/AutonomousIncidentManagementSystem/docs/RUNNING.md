# ✅ System Running! Quick Reference

## 🟢 Status: AIMS is LIVE on port 8001

```
✅ PostgreSQL Database: Running
✅ Redis Cache: Running  
✅ FastAPI Backend: Running
✅ API Documentation: Available
```

---

## 🚀 Quick Start Commands

### 1. Test Health
```bash
curl http://localhost:8001/api/v1/health
```

**Response:**
```json
{
  "status": "healthy",
  "version": "0.1.0",
  "timestamp": "2026-03-28T17:17:57.313456",
  "components": {
    "database": "up",
    "llm": "up",
    "cache": "up"
  }
}
```

### 2. Get Statistics
```bash
curl http://localhost:8001/api/v1/stats
```

### 3. Create an Alert
```bash
curl -X POST http://localhost:8001/api/v1/alerts \
  -H "Content-Type: application/json" \
  -d '{
    "source": "prometheus",
    "source_id": "alert_001",
    "title": "High CPU Usage",
    "description": "CPU usage exceeds 80%",
    "severity": "HIGH",
    "affected_service": ["api-server"],
    "tags": ["production"]
  }'
```

### 4. List All Alerts
```bash
curl http://localhost:8001/api/v1/alerts
```

### 5. Get Alert by ID
```bash
curl http://localhost:8001/api/v1/alerts/{alert_id}
```

---

## 📚 API Documentation

**Swagger UI (Interactive API docs):**
- http://localhost:8001/docs

**ReDoc (Beautiful API docs):**
- http://localhost:8001/redoc

**OpenAPI Schema:**
- http://localhost:8001/openapi.json

---

## 📊 Available Endpoints

### Health Endpoints
- `GET /api/v1/health` - Health check
- `GET /api/v1/stats` - System statistics

### Alert Endpoints
- `POST /api/v1/alerts` - Create alert
- `GET /api/v1/alerts` - List alerts (paginated)
- `GET /api/v1/alerts/{id}` - Get alert details
- `PUT /api/v1/alerts/{id}` - Update alert
- `DELETE /api/v1/alerts/{id}` - Delete alert

### Incident Endpoints
- `POST /api/v1/incidents` - Create incident
- `GET /api/v1/incidents` - List incidents
- `GET /api/v1/incidents/{id}` - Get incident details
- `PUT /api/v1/incidents/{id}` - Update incident
- `POST /api/v1/incidents/{id}/acknowledge` - Acknowledge incident
- `POST /api/v1/incidents/{id}/resolve` - Resolve incident
- `GET /api/v1/incidents/{id}/timeline` - Get incident timeline
- `POST /api/v1/incidents/{id}/comments` - Add comment

### Analysis Endpoints
- `POST /api/v1/analysis/correlate` - Correlate alerts
- `POST /api/v1/analysis/analyze` - Analyze incident (LLM)
- `POST /api/v1/analysis/recommendations` - Get recommendations
- `POST /api/v1/analysis/normalize` - Normalize alert

---

## 🛠️ Manage Services

### View Logs
```bash
# All services
docker compose logs -f

# Just backend
docker compose logs -f backend

# Just database
docker compose logs -f postgres

# Just cache
docker compose logs -f redis
```

### Restart Services
```bash
docker compose restart

# Or restart specific service
docker compose restart backend
```

### Stop Services
```bash
docker compose stop
```

### Start Services
```bash
docker compose up -d
```

### Remove Everything (clean slate)
```bash
docker compose down -v
docker compose up --build -d
```

---

## 🔧 Troubleshooting

### Issue: "Connection refused"
```bash
# Check if services are running
docker compose ps

# Restart services
docker compose restart
```

### Issue: "Port 8001 already in use"
```bash
# Kill process using port
lsof -i :8001
kill -9 <PID>

# Or use different port in docker-compose.yml
```

### Issue: Database connection error
```bash
# Check database logs
docker compose logs postgres

# Verify database is ready
docker compose logs postgres | grep "ready to accept"
```

### Issue: Backend not starting
```bash
# Check full logs
docker compose logs backend

# Rebuild image
docker compose build --no-cache backend
docker compose up -d backend
```

---

## 📖 Example Workflow

### 1. Create Multiple Alerts
```bash
# Alert 1
curl -X POST http://localhost:8001/api/v1/alerts \
  -H "Content-Type: application/json" \
  -d '{
    "source": "datadog",
    "source_id": "dd_001",
    "title": "Database Connection Pool Exhausted",
    "severity": "CRITICAL",
    "affected_service": ["payment-api"],
    "tags": ["database"]
  }'

# Alert 2
curl -X POST http://localhost:8001/api/v1/alerts \
  -H "Content-Type: application/json" \
  -d '{
    "source": "newrelic",
    "source_id": "nr_001",
    "title": "Payment API Response Time High",
    "severity": "HIGH",
    "affected_service": ["payment-api"],
    "tags": ["performance"]
  }'
```

### 2. Check Alert List
```bash
curl http://localhost:8001/api/v1/alerts | python3 -m json.tool
```

### 3. Correlate Alerts (coming soon - needs implementation)
```bash
curl -X POST http://localhost:8001/api/v1/analysis/correlate \
  -H "Content-Type: application/json" \
  -d '{
    "alert_ids": ["alert_id_1", "alert_id_2"],
    "time_window_seconds": 300
  }'
```

---

## 🔑 Environment Variables

Key variables in `backend/.env`:

```
OPENAI_API_KEY=your-key-here          # For GPT-4 analysis
ANTHROPIC_API_KEY=your-key-here       # For Claude analysis
SLACK_BOT_TOKEN=xoxb-...              # For Slack notifications
EMAIL_SMTP_USER=your-email@gmail.com  # For email notifications
LLM_PROVIDER=openai                   # Change to 'anthropic' if preferred
DEBUG=false                           # Set to true for verbose logs
```

---

## 📝 Next Steps

1. **Explore API** - Open http://localhost:8001/docs
2. **Test Endpoints** - Use cURL examples above
3. **Send Alerts** - Integrate with your monitoring tools
4. **Configure Notifications** - Set up Slack, email, webhooks
5. **Review Implementation** - Check `GETTING_STARTED.md`
6. **Start Development** - Begin Phase 2 implementation

---

## 📞 Documentation

- **Getting Started**: `GETTING_STARTED.md`
- **API Usage**: `http://localhost:8001/docs`
- **Architecture**: `doc/DESIGN.md`
- **Requirements**: `requirements/REQUIREMENTS.md`
- **Troubleshooting**: `TROUBLESHOOTING_SETUP.md`

---

## ✨ You're All Set!

The Autonomous Incident Management System is **running and ready to use**! 🚀

Start by:
1. Opening http://localhost:8001/docs in your browser
2. Sending a test alert using cURL
3. Exploring the available endpoints
4. Reading the GETTING_STARTED guide for detailed workflows

**Happy incident managing!** 🎉
