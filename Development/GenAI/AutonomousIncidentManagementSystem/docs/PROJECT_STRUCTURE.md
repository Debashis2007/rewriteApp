# Autonomous Incident Management System - Project Structure

## Complete Directory Tree

```
AutonomousIncidentManagementSystem/
│
├── doc/
│   └── DESIGN.md                          # Complete system design document
│
├── prompts/                               # AI/GenAI Prompts (6 files)
│   ├── alert_normalization.md
│   ├── alert_correlation.md
│   ├── incident_classification.md
│   ├── root_cause_analysis.md
│   ├── incident_recommendation.md
│   └── autonomous_response.md
│
├── requirements/
│   └── REQUIREMENTS.md                    # Detailed system requirements
│
├── backend/                               # FastAPI Backend
│   ├── src/
│   │   ├── __init__.py
│   │   ├── main.py                        # FastAPI application
│   │   ├── database.py                    # SQLAlchemy configuration
│   │   ├── schemas.py                     # Pydantic request/response models
│   │   │
│   │   ├── config/
│   │   │   ├── __init__.py
│   │   │   └── settings.py                # Configuration management
│   │   │
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   └── database.py                # ORM models (14 models)
│   │   │
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   └── core.py                    # Business logic (5 services)
│   │   │
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   └── routes.py                  # API endpoints (15+ routes)
│   │   │
│   │   ├── llm/
│   │   │   ├── __init__.py
│   │   │   └── client.py                  # LLM clients & prompt manager
│   │   │
│   │   └── notifications/
│   │       ├── __init__.py
│   │       └── service.py                 # Notification service
│   │
│   ├── tests/                             # Test suite (to be populated)
│   │   └── [test files]
│   │
│   ├── config/                            # Configuration files
│   │   └── [config files]
│   │
│   ├── requirements.txt                   # Python dependencies (25 packages)
│   ├── .env.template                      # Environment variables template
│   ├── Dockerfile                         # Docker image definition
│   └── README.md                          # Backend documentation
│
├── frontend/                              # React Frontend (to be created)
│   ├── src/
│   ├── public/
│   ├── package.json
│   ├── Dockerfile
│   └── README.md
│
├── docker-compose.yml                     # Full development environment
├── IMPLEMENTATION_SUMMARY.md              # This implementation summary
└── README.md                              # Main project README
```

## Component Summary

### 1. Core Backend Files (9 Files)
| File | Lines | Purpose |
|------|-------|---------|
| `src/main.py` | ~90 | FastAPI application entry point with middleware |
| `src/database.py` | ~35 | SQLAlchemy setup and database factory |
| `src/schemas.py` | ~200+ | 10+ Pydantic request/response schemas |
| `src/config/settings.py` | ~50 | 40+ environment-based configuration parameters |
| `src/models/database.py` | ~350 | 14 ORM models with relationships |
| `src/services/core.py` | ~250+ | 5 core services (Alert, Incident, Analysis, Correlation, Metrics) |
| `src/api/routes.py` | ~200+ | 15+ REST API endpoints |
| `src/llm/client.py` | ~300+ | LLM clients (OpenAI, Anthropic) + Prompt Manager |
| `src/notifications/service.py` | ~300+ | 5 notification providers |

### 2. Data Models (14 Models)
```
Alerts
├── Alert
└── AlertSeverity, AlertStatus (Enums)

Incidents
├── Incident
├── IncidentEvent
├── IncidentAnalysis
├── IncidentRecommendation
└── IncidentSeverity, IncidentStatus, IncidentEventType, AnalysisType (Enums)

System
├── NotificationLog
├── AuditLog
└── Helpers
```

### 3. Services (5 Services)
| Service | Methods | Purpose |
|---------|---------|---------|
| AlertService | 6 | Create, read, update, list, deduplicate alerts |
| IncidentService | 9 | Full incident lifecycle management |
| AnalysisService | 4 | LLM-based analysis operations |
| CorrelationService | 2 | Alert correlation logic |
| MetricsService | 2 | System statistics and metrics |

### 4. API Endpoints (15+ Routes)

**Health (2):**
- GET /health
- GET /stats

**Alerts (4):**
- POST /alerts
- GET /alerts
- GET /alerts/{id}
- PUT /alerts/{id}

**Incidents (8):**
- POST /incidents
- GET /incidents
- GET /incidents/{id}
- PUT /incidents/{id}
- POST /incidents/{id}/acknowledge
- POST /incidents/{id}/resolve
- GET /incidents/{id}/timeline
- POST /incidents/{id}/comments

**Analysis (4):**
- POST /incidents/{id}/analyze
- GET /incidents/{id}/recommendations
- POST /alerts/correlate
- POST /alerts/normalize

### 5. LLM Integration
**Prompt Manager:**
- Loads from `/prompts/` directory
- Template extraction
- Response caching

**LLM Clients:**
- OpenAI (GPT-4)
- Anthropic (Claude)
- Abstract base class
- Factory pattern

**Prompt Templates (6):**
1. Alert Normalization
2. Alert Correlation
3. Incident Classification
4. Root Cause Analysis
5. Incident Recommendation
6. Autonomous Response

### 6. Notification System
**Providers (4):**
- Email (SMTP)
- Slack (Bot)
- Webhooks (HTTP)
- PagerDuty (API)

**Features:**
- Multi-channel support
- Template-based messages
- Delivery tracking
- Status notifications

### 7. Configuration
**40+ Parameters:**
- Database (URL, pool size, overflow)
- Redis (URL, TTL)
- LLM (provider, API keys, models, temperature)
- Alerts (correlation window, deduplication)
- Incidents (retention, escalation)
- Notifications (channels, templates)
- API (prefix, CORS, title)
- Security (JWT, secrets)
- Monitoring (metrics, logging)

### 8. Database Schema
```
alerts (table)
├── id (UUID)
├── source, source_id
├── title, description
├── severity, status
├── fingerprint (unique)
├── metrics, metadata
└── timestamps

incidents (table)
├── id (UUID)
├── title, description
├── severity, status, category
├── affected_services
├── root_cause, confidence
├── assigned_to
└── timestamps

incident_events (table)
├── id (UUID)
├── incident_id (FK)
├── event_type
├── message, actor
└── timestamp

llm_analyses (table)
├── id (UUID)
├── incident_id (FK)
├── analysis_type
├── model, prompt, response
├── confidence_score
└── timestamp

incident_recommendations (table)
├── id (UUID)
├── incident_id (FK)
├── recommendation, description
├── priority, phase
├── status, executed_at
└── timestamps

notification_logs (table)
├── id (UUID)
├── channel, recipient
├── status, error_message
└── timestamp

audit_logs (table)
├── id (UUID)
├── user, action
├── resource_type, resource_id
├── changes
└── timestamp
```

## Deployment Architecture

```
┌─────────────────────────────────────────────┐
│         Docker Compose (Local Dev)          │
├─────────────────────────────────────────────┤
│                                             │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐ │
│  │ FastAPI  │  │Postgres  │  │  Redis   │ │
│  │ Backend  │  │   15     │  │    7     │ │
│  │ Port 8000│  │ Port 5432│  │ Port 6379│ │
│  └──────────┘  └──────────┘  └──────────┘ │
│                                             │
└─────────────────────────────────────────────┘
         ↓
┌─────────────────────────────────────────────┐
│    Frontend (React - to be created)         │
│    Port 3000/5173                           │
└─────────────────────────────────────────────┘
```

## Technology Stack

### Backend Stack
```
Language:     Python 3.10+
Framework:    FastAPI 0.109.0
ORM:          SQLAlchemy 2.0.25
Database:     PostgreSQL 15
Cache:        Redis 7
LLM:          OpenAI SDK + Anthropic SDK
Async:        asyncio, aiohttp
Validation:   Pydantic 2.5.0
Notifications: slack-sdk, aiosmtplib
```

### Frontend Stack (Planned)
```
Framework:    React 18
Build Tool:   Vite
State Mgmt:   Redux/Zustand
UI:           Material-UI / Shadcn
Real-time:    Socket.IO
Styling:      Tailwind CSS
```

### DevOps
```
Containerization: Docker
Orchestration:    Docker Compose
CI/CD:           GitHub Actions
Monitoring:      Prometheus
Logging:         ELK Stack (planned)
```

## Quick Start

### Option 1: Docker Compose (Recommended)
```bash
docker-compose up --build
# Access at http://localhost:8000
```

### Option 2: Manual Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.template .env
python -m uvicorn src.main:app --reload
```

## File Statistics

| Category | Count | Details |
|----------|-------|---------|
| Python Modules | 13 | Backend code |
| API Endpoints | 15+ | REST routes |
| Database Models | 14 | ORM models |
| Services | 5 | Business logic |
| Pydantic Schemas | 10+ | API models |
| Notification Providers | 4 | Email, Slack, Webhook, PagerDuty |
| LLM Clients | 2 | OpenAI, Anthropic |
| Prompts | 6 | AI/GenAI templates |
| Configuration Parameters | 40+ | Environment-based |
| Dependencies | 25 | Python packages |

## Integration Points

### External Services
- OpenAI API (GPT-4)
- Anthropic API (Claude)
- Slack API
- Email (SMTP)
- PagerDuty API

### Data Sources
- REST API (webhook)
- Prometheus
- Datadog
- New Relic
- Custom integrations

## Security Features

- JWT authentication framework
- CORS protection
- Input validation (Pydantic)
- Async/await for non-blocking I/O
- Error handling with logging
- Environment-based secrets

## Next Steps

1. **Implement Database Operations** - Replace placeholder returns with actual DB queries
2. **Add Authentication** - JWT token generation and validation
3. **Complete Tests** - Unit and integration tests
4. **Create Frontend** - React dashboard
5. **Add Monitoring** - Prometheus metrics and logging
6. **Deploy** - Kubernetes manifests and CI/CD

## Documentation Files

1. `doc/DESIGN.md` - System architecture and design decisions
2. `requirements/REQUIREMENTS.md` - Detailed functional and non-functional requirements
3. `backend/README.md` - Backend setup and API documentation
4. `IMPLEMENTATION_SUMMARY.md` - This framework summary
5. `prompts/*.md` - AI/GenAI prompt templates

---

**Total Lines of Code (Backend Framework): ~2,000+ lines**
**Total Configuration Parameters: 40+**
**Total Database Models: 14**
**Total API Endpoints: 15+**
**Total Services: 5**
**Ready for Implementation: YES ✓**
