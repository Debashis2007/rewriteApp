# Agent-to-Agent Communication in AIMS

## Quick Summary

AIMS implements a **4-stage agent pipeline** where specialized agents collaborate to detect, correlate, analyze, and respond to infrastructure incidents. Each agent communicates via synchronous request-response (critical path) and asynchronous events (notifications).

```
Alert → Normalize → Correlate → Analyze → Recommend
  ↓        ↓          ↓          ↓          ↓
[Agent 1] [Agent 2]  [Agent 3]  [Agent 4] Dashboard
  50ms    200ms      1100ms     150ms     + Integrations
```

**Total: ~1.7 seconds** from raw alert to actionable recommendation with AI analysis

---

## The 4 Agents

### 1️⃣ Alert Ingestion Agent (T+0-50ms)

**What it does**: Normalizes raw alerts from any monitoring system

**Input**: Raw alert from Prometheus/Grafana/CloudWatch
```json
{
  "source": "prometheus",
  "alert": "HighCPU",
  "value": 95
}
```

**Process**:
1. Detect source type (Prometheus, Grafana, CloudWatch, etc.)
2. Normalize to AIMS schema
3. Generate fingerprint for deduplication
4. Check Redis cache for duplicates
5. Store in PostgreSQL
6. Cache fingerprint in Redis

**Output**: Normalized, deduplicated alert
```json
{
  "id": "abc123",
  "source": "prometheus",
  "title": "High CPU Usage",
  "service": "api-server",
  "severity": "critical",
  "status": "new",
  "fingerprint": "sha256_hash",
  "metrics": {"cpu": 95}
}
```

**Communication**: Passes to Correlation Agent

---

### 2️⃣ Correlation Agent (T+200-400ms)

**What it does**: Groups related alerts into incidents

**Input**: Normalized alert from Alert Ingestion Agent

**Process**:
1. Query PostgreSQL for similar alerts in last 10 minutes
2. Calculate correlation score (0.0-1.0) based on:
   - Service match (40%)
   - Category match (30%)
   - Time proximity (20%)
   - Severity level (10%)
3. If score ≥ 0.7: Link to existing incident
4. If score < 0.7: Create new incident

**Example - Cascade Detection**:
```
Alert 1: CPU = 95% (api-server) → T+0
Alert 2: Memory = 87% (api-server) → T+5  ← Similar service
Alert 3: Connection Pool = 100% (api-server) → T+10 ← Same service

Correlation Score = 0.95 (all same service, within 10 minutes)
Action: CREATE Incident #123 linking all 3 alerts
```

**Output**: Incident with grouped alerts
```json
{
  "action": "create",
  "incident_id": "123",
  "correlation_score": 0.95,
  "alerts_linked": 3
}
```

**Communication**: Passes to Analysis Agent

---

### 3️⃣ Analysis Agent (T+500-1500ms)

**What it does**: AI-powered root cause analysis using Ollama LLM

**Input**: Incident with correlated alerts from Correlation Agent

**Process**:
1. Prepare analysis context:
   - Aggregate all metrics
   - Detect patterns (resource exhaustion, network issue, app failure)
   - Gather historical data
2. Build structured prompt for LLM
3. Send to Ollama (local LLM)
4. Ollama processes for ~1 second
5. Parse response
6. Structure results

**Example Interaction**:
```
Analysis Agent sends to Ollama:
───────────────────────────────

Context:
- Service: api-server
- Alerts: [CPU spike, Memory spike, Connection timeouts]
- Patterns: [resource_exhaustion, connectivity_issue]
- Metrics: {cpu: 95%, memory: 87%, connections: 1000/1000}

Ollama responds:
────────────────
{
  "root_cause": "Connection pool exhaustion under high traffic",
  "confidence": 94,
  "evidence": [
    "1000/1000 max connections reached",
    "Connection timeouts increasing exponentially",
    "Database query backlog detected"
  ],
  "actions": [
    "Increase max_connections from 1000 to 1500",
    "Enable connection recycling",
    "Monitor for connection leaks in application code"
  ]
}
```

**Output**: Structured analysis with confidence
```json
{
  "root_cause": "Connection pool exhaustion",
  "confidence": 94,
  "evidence": ["1000/1000 connections", "Timeouts increasing"],
  "recommended_actions": ["Increase max_connections", "Enable recycling"],
  "severity_assessment": "Critical"
}
```

**Special Features**:
- ✅ Fallback mode if Ollama unavailable (rule-based analysis)
- ✅ Configurable LLM models (Mistral, Neural-Chat, Orca-Mini)
- ✅ Cached results for common patterns

**Communication**: Passes to Response Agent

---

### 4️⃣ Response Agent (T+1550-1700ms)

**What it does**: Generates actionable recommendations & formats for integrations

**Input**: Analysis result from Analysis Agent

**Process**:
1. Apply rule engine to match analysis to actions
2. Format for dashboard (React Material-UI)
3. Format for integrations (Slack, PagerDuty, OpsGenie)
4. Publish events to Redis for async subscribers

**Recommendation Rules**:
```
IF "cpu exhaustion" AND confidence > 70:
  → Recommend: Scale up replicas

IF "memory" AND confidence > 80:
  → Recommend: Restart service

IF "connection pool":
  → Recommend: Increase max_connections

IF "recent deployment":
  → Recommend: Rollback to previous version

IF root_cause unclear:
  → Recommend: Further investigation
```

**Output Examples**:

Dashboard:
```json
{
  "incident_id": "123",
  "title": "API Server Connection Pool Exhaustion",
  "recommendations": [
    {
      "action": "scale-up",
      "priority": "high",
      "replicas": 3,
      "estimated_time": "2-5 minutes"
    }
  ]
}
```

Slack Integration:
```
🚨 Critical: API Server Connection Pool Exhaustion

Service: api-server
Root Cause: Connection pool exhaustion (94% confidence)
Recommendation: Increase max_connections from 1000 to 1500

[View in Dashboard] [Acknowledge]
```

**Communication**: 
- ✅ Synchronous: Dashboard update
- ✅ Asynchronous: Events published to Redis
- ✅ Webhooks: Slack, PagerDuty, OpsGenie

---

## Communication Patterns

### Pattern 1: Synchronous Request-Response (Critical Path)

Used for: Alert → Incident → Analysis → Response

```
┌─────────────────┐
│ Alert comes in  │
└────────┬────────┘
         │ (synchronous call)
         ▼
┌─────────────────────┐
│ AlertIngestionAgent │ await store_alert()
│ ← Waits for result  │
└────────┬────────────┘
         │ (returns alert_id)
         ▼
┌──────────────────────┐
│ CorrelationAgent     │ await correlate()
│ ← Waits for result   │
└────────┬─────────────┘
         │ (returns incident_id)
         ▼
┌─────────────────────┐
│ AnalysisAgent       │ await analyze()
│ ← Waits for result  │
└────────┬────────────┘
         │ (returns analysis)
         ▼
┌──────────────────────┐
│ ResponseAgent       │ await generate_response()
│ ← Waits for result  │
└────────┬─────────────┘
         │ (returns recommendations)
         ▼
┌─────────────────────┐
│ Return to API caller│
└─────────────────────┘

Advantages:
✓ Data consistency (no race conditions)
✓ Immediate feedback to API caller
✓ Easy to debug (clear call stack)

Trade-off: Slower (~1.7s) vs async
```

### Pattern 2: Asynchronous Event Publishing

Used for: Notifications, integrations, monitoring

```
┌──────────────────┐
│ ResponseAgent    │
│ generates        │ publish_event("incident.analyzed")
│ recommendations  │ publish_event("recommendations.generated")
└────────┬─────────┘
         │ (fire and forget)
         ▼
    ┌─────────────┐
    │ Redis Pub   │
    │ /Sub        │
    └────┬────┬───┘
         │    │
    ┌────▼─┐ ┌▼──────┐
    │Slack │ │Email  │
    │Notif │ │Notif  │
    └──────┘ └───────┘

Advantages:
✓ Non-blocking (fast)
✓ Scalable (subscribers can be on different servers)
✓ Loose coupling (Response Agent doesn't wait)

Trade-off: Eventual consistency (slight delay for notifications)
```

### Pattern 3: Shared Data Store

All agents read/write to the same databases:

```
┌─────────────────────────┐
│  PostgreSQL (Persistent)│
├─────────────────────────┤
│ • alerts                │
│ • incidents             │
│ • incident_responses    │
│ • alert_correlations    │
└───────────┬─────────────┘
            ▲
            │ (SQL queries)
            │
┌───────────┴──┬─────────────────────────┐
│              │                         │
▼              ▼                         ▼
[Agent 1]   [Agent 2]  [Agent 3]  [Agent 4]

┌─────────────────────────┐
│  Redis (Cache - Hot)    │
├─────────────────────────┤
│ • alert:fingerprint:*   │
│ • incident:summary:*    │
│ • analysis:cache:*      │
└───────────┬─────────────┘
            ▲
            │ (fast access)
            │
    [Agent 1] [Agent 2]

Benefits:
✓ Agents don't call each other directly
✓ Data is shared source of truth
✓ Decoupled architecture
✓ Easy to scale agents independently
```

---

## Real-World Timeline: Database Cascade Failure

```
T+0:00:00
Database connection pool fills (reached 1000/1000 connections)

T+0:00:05 [Alert 1 fires]
Prometheus detects connection timeout
Sends to AIMS /api/alerts

[ALERT_AGENT] T+0:00:05.000
├─ Receives raw Prometheus alert
├─ Normalizes to AIMS schema
├─ Calculates fingerprint
├─ Checks Redis dedup cache
├─ Stores in PostgreSQL (alert_id: abc123)
└─ Returns normalized alert ✓ (50ms)

T+0:00:05.050 [Alert 2 fires]
Application server detects connection timeouts
[ALERT_AGENT] Processes Alert 2 (50ms) ✓

T+0:00:05.100 [Alert 3 fires]
Monitoring system detects query slowdown
[ALERT_AGENT] Processes Alert 3 (50ms) ✓

[CORRELATION_AGENT] T+0:00:05.150
├─ Receives Alert 1
├─ Queries PostgreSQL: alerts from api-server in last 10 min
├─ Finds Alert 2, Alert 3 (all same service, same 5s window)
├─ Calculates correlation score:
│  ├─ Service match: 100% (all api-server)
│  ├─ Category match: 100% (all connection-related)
│  ├─ Time proximity: 100% (within 5 seconds)
│  └─ Total score: 0.95
├─ Score 0.95 > threshold 0.70: CORRELATE
├─ Creates Incident #1001
│  └─ Links alerts: [abc123, abc124, abc125]
└─ Returns incident_id: 1001 ✓ (200ms)

[ANALYSIS_AGENT] T+0:00:05.350
├─ Receives Incident #1001
├─ Prepares context:
│  ├─ Service: api-server
│  ├─ Alerts: 3 (connection timeout, query slowdown, memory pressure)
│  ├─ Pattern detected: ["connection_exhaustion", "resource_pressure"]
│  └─ Metrics: {connections: 1000, query_time: 2.5s, memory: 87%}
├─ Builds prompt for Ollama
├─ Sends to Ollama LLM →
│
│  [OLLAMA Processing for ~1000ms]
│  Analyzing incident pattern...
│  Detecting connection pool exhaustion...
│  Root cause: Database connection pool at capacity
│
├─ Ollama responds:
│  ├─ Root cause: "Connection pool exhaustion"
│  ├─ Confidence: 94%
│  └─ Actions: [
│      "Increase max_connections to 1500",
│      "Enable connection recycling",
│      "Monitor for connection leaks"
│     ]
├─ Parses response
└─ Returns analysis ✓ (1100ms total)

[RESPONSE_AGENT] T+0:00:06.450
├─ Receives analysis from Analysis Agent
├─ Applies rule engine:
│  ├─ Match: "connection pool" pattern
│  ├─ Confidence: 94% (high)
│  ├─ Action: "Increase max_connections"
│  └─ Priority: HIGH (all alerts critical)
├─ Generates recommendations:
│  ├─ Action 1: Increase max_connections from 1000 to 1500 (CRITICAL)
│  ├─ Action 2: Enable connection recycling (HIGH)
│  └─ Action 3: Review application for leaks (MEDIUM)
├─ Formats for dashboard:
│  ├─ Title: "API Server Connection Pool Exhaustion"
│  ├─ Root Cause: "Connection pool exhaustion (94% confidence)"
│  └─ Recommendations: [3 actions with priorities]
├─ Formats for Slack:
│  ├─ Color: 🔴 RED (critical)
│  ├─ Title: "API Server Connection Pool Exhaustion"
│  └─ Actions: "Increase max_connections, Enable recycling"
├─ Publishes events to Redis:
│  ├─ incident.analyzed {incident_id: 1001}
│  └─ recommendations.generated {count: 3}
└─ Returns complete response ✓ (150ms)

T+0:00:06.600
Dashboard receives response
├─ Incident #1001 marked as "ANALYZED"
├─ Displays root cause: "Connection pool exhaustion"
├─ Shows recommendations with priorities
└─ On-call engineer sees everything

T+0:00:06.650
Slack notification delivered
├─ Title: 🚨 API Server Connection Pool Exhaustion
├─ Root Cause: Connection pool exhaustion (94% confidence)
├─ Top Action: Increase max_connections from 1000 to 1500
└─ [View in Dashboard] [Acknowledge]

On-call Engineer sees full context:
────────────────────────────────────
✓ Root cause identified (94% confidence)
✓ Specific action recommended
✓ Timeline of what happened
✓ Supporting evidence (connection count, query times)
✓ Alternative actions if first doesn't work

Engineer Action:
─────────────────
Executes: "Update database config max_connections=1500"

T+0:00:07
Database accepts new connections
Connection queue drains

T+0:00:30
All metrics return to normal
Incident #1001 auto-resolved

TOTAL TIME: 30 seconds from detection to resolution
WITHOUT AIMS: Would have taken 30+ minutes for manual investigation

Timeline:
  Alert → Normalize: 50ms
  ├─ Correlate: 200ms
  ├─ Analyze: 1100ms
  ├─ Respond: 150ms
  └─ Total: 1500ms (1.5 seconds) ✅
```

---

## Communication Architecture Diagram

```
    ┌──────────────────────────────────────────────────┐
    │          API Gateway / Load Balancer             │
    └─────────────────────┬────────────────────────────┘
                          │
                          ▼
    ┌──────────────────────────────────────────────────┐
    │  FastAPI Backend (Main Application)              │
    │                                                   │
    │  POST /api/alerts ← Receives raw alerts          │
    │  GET /api/incidents ← Query incidents            │
    │  GET /api/responses ← Get recommendations        │
    │  POST /api/responses/execute ← Execute action    │
    └─────────────────────┬────────────────────────────┘
                          │
          ┌───────────────┼───────────────┐
          │               │               │
          ▼               ▼               ▼
    ┌──────────┐  ┌──────────────┐  ┌──────────────┐
    │PostgreSQL│  │    Redis     │  │ Ollama LLM   │
    │          │  │              │  │              │
    │ Alerts   │  │ Fingerprints │  │ Text Gen     │
    │ Incidents│  │ Cache        │  │ Analysis     │
    │Responses │  │ Sessions     │  │              │
    └────┬─────┘  └──────┬───────┘  └──────┬───────┘
         │               │                 │
         └───────────────┼─────────────────┘
                         │
    ┌────────────────────┴──────────────────────┐
    │          AGENT PIPELINE                    │
    │                                            │
    │  [1]        [2]        [3]        [4]     │
    │ Alert   →  Correl  →  Analysis  → Response
    │ Agent     Agent      Agent        Agent    │
    │ 50ms     200ms      1100ms       150ms     │
    │                                            │
    └────────────────────┬───────────────────────┘
                         │
         ┌───────────────┼───────────────┐
         │               │               │
         ▼               ▼               ▼
    ┌─────────┐   ┌──────────┐   ┌──────────┐
    │Dashboard│   │   Slack  │   │PagerDuty │
    │(React)  │   │  (Sync)  │   │ (Async)  │
    │         │   │ WebHook  │   │ Event    │
    └─────────┘   └──────────┘   └──────────┘
```

---

## Key Features of This Architecture

✅ **Fast**: 1.7 seconds from alert to recommendation
✅ **Autonomous**: No human needed until action execution
✅ **Intelligent**: Uses Ollama LLM for root cause analysis
✅ **Scalable**: Each agent can run independently
✅ **Resilient**: Fallback to rule-based analysis if LLM fails
✅ **Integrated**: Slack, PagerDuty, OpsGenie support out-of-box
✅ **Observable**: Comprehensive logging and metrics
✅ **Free**: Uses open-source Ollama (zero LLM cost)

---

## Code Example: End-to-End

```python
from src.agents import (
    AlertIngestionAgent,
    CorrelationAgent,
    AnalysisAgent,
    ResponseAgent
)

# Initialize agents
alert_agent = AlertIngestionAgent(db, redis)
correlation_agent = CorrelationAgent(db, redis)
analysis_agent = AnalysisAgent(llm_client)
response_agent = ResponseAgent()

# Process alert through pipeline
async def process_alert(raw_alert):
    # Stage 1: Ingest
    alert_result = await alert_agent.ingest_alert(raw_alert)
    
    # Stage 2: Correlate
    correlation_result = await correlation_agent.correlate_alerts(
        alert_result['alert']
    )
    
    # Stage 3: Analyze
    analysis_result = await analysis_agent.analyze_incident(
        correlation_result['incident']
    )
    
    # Stage 4: Respond
    response_result = await response_agent.generate_response(
        analysis_result['analysis'],
        correlation_result['incident']
    )
    
    return {
        "alert": alert_result,
        "incident": correlation_result,
        "analysis": analysis_result,
        "recommendations": response_result
    }
```

---

## Summary

**AIMS agents communicate through a sophisticated pipeline:**

1. **Synchronous** for critical path (ensures consistency)
2. **Asynchronous** for integrations (fast, scalable)
3. **Shared data store** for coordination (decoupled)
4. **External services** for LLM and notifications

This creates a **fast, intelligent, and autonomous** incident management system that reduces MTTR (Mean Time To Recovery) from 30+ minutes to under 2 minutes.

