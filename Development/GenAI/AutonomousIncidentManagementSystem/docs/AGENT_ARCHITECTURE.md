# Multi-Agent Architecture Documentation

## Overview

AIMS implements a sophisticated multi-agent system where four specialized agents work together in a pipeline to detect, correlate, analyze, and respond to infrastructure incidents. Each agent has a single responsibility and communicates via shared data stores and event systems.

## Agent Pipeline

```
Raw Alert → [Agent 1] → Alert Normalized → [Agent 2] → Incident Correlated 
                                                            ↓
                                                        [Agent 3] → AI Analysis
                                                            ↓
                                                        [Agent 4] → Recommendations
                                                            ↓
                                                      Dashboard + Integrations
```

### Timing Breakdown

- **T+0ms**: Alert received
- **T+50ms**: Alert normalized and stored
- **T+100-400ms**: Correlation analysis
- **T+500-1500ms**: LLM analysis (Ollama processing)
- **T+1550-1700ms**: Response generation
- **Total: ~1.7 seconds** from alert to actionable recommendation

## Agent Details

### 1. Alert Ingestion Agent

**Location**: `backend/src/agents/alert_agent.py`

**Responsibilities**:
- Receive alerts from multiple sources (Prometheus, Grafana, CloudWatch, webhooks)
- Normalize to AIMS schema
- Deduplicate based on fingerprints
- Store in PostgreSQL
- Cache in Redis

**Key Methods**:
```python
async def ingest_alert(raw_alert) -> Dict
    # Main entry point (T+0-50ms)
    # Returns: normalized alert with ID
    
def _normalize_alert(raw_alert) -> Dict
    # Supports: Prometheus, Grafana, CloudWatch, generic
    
async def _check_duplicate(fingerprint) -> int
    # Redis-based dedup counter
```

**Data Flow**:
```
Input:  Raw alert from monitoring system
        {source: "prometheus", alert: "HighCPU", value: 95}

Processing:
    1. Detect source type (T+10ms)
    2. Normalize to schema (T+20ms)
    3. Generate fingerprint (T+30ms)
    4. Check Redis cache (T+40ms)
    5. Store in PostgreSQL (T+45ms)

Output: Normalized alert
        {
            source: "prometheus",
            title: "High CPU Usage",
            severity: "critical",
            service: "api-server",
            fingerprint: "abc123",
            status: "new"
        }
```

### 2. Correlation Agent

**Location**: `backend/src/agents/correlation_agent.py`

**Responsibilities**:
- Find alerts similar to current one
- Calculate correlation scores
- Group into incidents
- Detect cascading failures

**Key Methods**:
```python
async def correlate_alerts(alert) -> Dict
    # Main entry point (T+200-400ms)
    # Returns: incident ID and correlation metadata
    
def _find_similar_alerts(alert) -> List
    # Query PostgreSQL for similar alerts in time window
    
def _calculate_correlation_score(alert, similar) -> float
    # 0.0-1.0 score based on service, category, time, severity
    
async def detect_cascading_failure(incident) -> Optional[Dict]
    # Detect multi-service failure patterns
```

**Correlation Scoring**:
- Service match (40%)
- Category match (30%)
- Time proximity (20%)
- Severity escalation (10%)

**Threshold**: Score ≥ 0.7 = same incident

**Data Flow**:
```
Input: Normalized alert (from AlertIngestionAgent)

Processing:
    1. Query similar alerts: service=X, time < 10min (T+250ms)
    2. Calculate score with each (T+300ms)
    3. If score > 0.7, link to existing incident (T+350ms)
    4. Else, create new incident (T+350ms)

Output: Either:
    Action: "create"
    ├─ incident_id: "123"
    └─ correlation_score: 0.0
    
    OR
    
    Action: "update"
    ├─ incident_id: "456"
    └─ correlation_score: 0.85
```

### 3. Analysis Agent

**Location**: `backend/src/agents/analysis_agent.py`

**Responsibilities**:
- Prepare incident context
- Send to Ollama LLM for analysis
- Parse LLM response
- Structure results

**Key Methods**:
```python
async def analyze_incident(incident) -> Dict
    # Main entry point (T+400-1550ms)
    # Delegates to Ollama, returns structured analysis
    
def _prepare_analysis_context(incident) -> Dict
    # Aggregate metrics, timeline, patterns
    
def _build_analysis_prompt(context) -> str
    # Generate well-structured prompt for LLM
    
async def _structure_analysis(llm_response) -> Dict
    # Parse JSON, extract root cause, confidence, actions
```

**LLM Integration**:
```python
# Sends to Ollama:
analysis = await llm.analyze_incident(
    alerts=incident.alerts,
    context={
        service: "api-server",
        patterns: ["resource_exhaustion", "connectivity_issue"],
        metrics: {cpu: 95, memory: 87, connections: 1000}
    },
    prompt="Analyze and provide root cause..."
)

# Returns:
{
    "root_cause": "Connection pool exhaustion",
    "confidence": 94,
    "evidence": [
        "1000/1000 max connections reached",
        "Connection timeouts increasing",
        "Database query slowdown"
    ],
    "actions": [
        "Increase max_connections to 1500",
        "Enable connection recycling",
        "Monitor for connection leaks"
    ]
}
```

**Fallback Logic**:
If Ollama unavailable, uses rule-based analysis:
```python
def _fallback_analysis(incident) -> Dict
    # Rule-based analysis without LLM
    # Detects patterns: resource_exhaustion, connectivity_issue, app_failure
    # Returns confidence: 0
```

**Data Flow**:
```
Input: Correlated incident with alerts

Processing:
    1. Prepare context (T+450ms)
       - Aggregate metrics
       - Detect patterns
       - Gather historical data
    
    2. Build prompt (T+480ms)
       - Create detailed context for LLM
    
    3. Send to Ollama (T+500ms)
       - HTTP POST to Ollama API
       - Await response (~1 second)
    
    4. Parse response (T+1500ms)
       - Extract JSON
       - Validate structure

Output: Structured analysis
    {
        root_cause: "Connection pool exhaustion",
        confidence: 94,
        evidence: [...],
        recommended_actions: [...],
        severity_assessment: "Critical"
    }
```

### 4. Response Agent

**Location**: `backend/src/agents/response_agent.py`

**Responsibilities**:
- Generate specific recommendations
- Format for dashboard display
- Format for external integrations
- Publish events to subscribers

**Key Methods**:
```python
async def generate_response(analysis, incident) -> Dict
    # Main entry point (T+1550-1700ms)
    
def _generate_recommendations(analysis, incident) -> List[Dict]
    # Rule engine: matches analysis to actions
    
def _format_dashboard_response(...) -> Dict
    # Material-UI friendly response
    
def _format_integration_payloads(...) -> Dict
    # Slack, PagerDuty, OpsGenie formats
    
async def _publish_events(...) -> None
    # Publish to Redis for subscribers
```

**Recommendation Rules**:
```python
IF root_cause contains "cpu" AND confidence > 70:
    RECOMMEND: Scale up replicas

IF root_cause contains "memory" AND confidence > 80:
    RECOMMEND: Restart service
ELSE:
    RECOMMEND: Increase memory

IF root_cause contains "connection":
    RECOMMEND: Increase max_connections + enable recycling

IF root_cause contains "network":
    RECOMMEND: Investigate DNS, firewall, service discovery

IF root_cause contains "deployment":
    RECOMMEND: Rollback to previous version
```

**Data Flow**:
```
Input: Analysis result

Processing:
    1. Generate recommendations (T+1580ms)
       - Apply rule engine
       - Match analysis to actions
       - Calculate parameters
    
    2. Format for dashboard (T+1600ms)
       - Convert to UI-friendly format
       - Include confidence levels
    
    3. Format for integrations (T+1620ms)
       - Slack: Color-coded message with fields
       - PagerDuty: Severity-mapped event
       - OpsGenie: Priority-mapped alert
    
    4. Publish events (T+1650ms)
       - incident.analyzed event
       - recommendations.generated event

Output: Complete response package
    {
        dashboard: {
            incident_id: "123",
            title: "API Server Performance Degradation",
            analysis: {...},
            recommendations: [
                {
                    action: "scale-up",
                    priority: "high",
                    replicas: 3
                },
                ...
            ]
        },
        integrations: {
            slack: {...},
            pagerduty: {...},
            opsgenie: {...}
        }
    }
```

## Communication Patterns

### 1. Synchronous Request-Response (Critical Path)

```
AlertIngestionAgent
    │ (await)
    ├─→ Store in DB
    ├─→ Increment counter in Redis
    └─→ Return to API
        
    Response blocks caller until complete
    Ensures consistency and immediate feedback
```

### 2. Asynchronous Event Publishing

```
ResponseAgent publishes events:
    ├─ incident.analyzed
    ├─ recommendations.generated
    └─ response.sent
    
    Subscribers listen on Redis channels:
    ├─ Notification Service (Slack/Email)
    ├─ Metrics Service (tracking)
    └─ Archive Service (logging)
    
    Non-blocking, eventual consistency
```

### 3. Shared Data Store

```
All agents read/write to:

PostgreSQL (persistent):
    ├─ alerts
    ├─ incidents
    ├─ incident_responses
    └─ alert_correlations

Redis (cache):
    ├─ alert:fingerprint:*
    ├─ incident:summary:*
    └─ analysis:cache:*
```

## Integration Points

### External Systems

**1. Monitoring Systems** (Inputs)
- Prometheus AlertManager
- Grafana alerts
- CloudWatch SNS
- Custom webhooks

**2. Communication Systems** (Outputs)
- Slack (notifications)
- PagerDuty (escalation)
- OpsGenie (on-call)
- Email (fallback)

**3. Action Execution** (Optional)
- Kubernetes API (scaling)
- Deployment tools (rollback)
- Configuration management (changes)
- Runbook automation (procedures)

## Configuration

### Agent Settings

```python
# backend/.env

# Alert Ingestion
ALERT_CACHE_TTL=300  # 5 minutes

# Correlation
CORRELATION_WINDOW=600  # 10 minutes
CORRELATION_THRESHOLD=0.7  # 0-1 score

# Analysis
OLLAMA_TIMEOUT=2000  # milliseconds
ANALYSIS_CACHE_ENABLED=true

# Response
ENABLE_SLACK_INTEGRATION=true
ENABLE_PAGERDUTY_INTEGRATION=false
ENABLE_OPSGENIE_INTEGRATION=false
```

### Agent Scaling

**Single-process** (Development):
```
1 FastAPI process
└─ All 4 agents inline
```

**Multi-process** (Production):
```
Orchestrator (FastAPI)
├─ AlertIngestionAgent (auto-scaling pool)
├─ CorrelationAgent (auto-scaling pool)
├─ AnalysisAgent (GPU-capable nodes)
└─ ResponseAgent (auto-scaling pool)
```

## Monitoring & Observability

### Metrics

```python
# Prometheus metrics exposed

aims_alert_ingestion_duration_ms
    # How long alert ingestion takes

aims_correlation_score
    # Distribution of correlation scores

aims_llm_analysis_duration_ms
    # Ollama analysis time

aims_recommendation_generation_duration_ms
    # Response agent processing time

aims_incident_end_to_end_duration_ms
    # Total time from alert to response

aims_agent_queue_depth
    # How many items queued for each agent
```

### Logging

```
[ALERT_AGENT] Alert ingestion starting
[ALERT_AGENT] Normalized alert: High CPU Usage
[CORRELATION_AGENT] Processing alert: High CPU Usage
[CORRELATION_AGENT] Found 3 similar alerts
[ANALYSIS_AGENT] Analyzing incident: 123
[ANALYSIS_AGENT] LLM analysis complete (confidence: 94%)
[RESPONSE_AGENT] Generating response for incident: 123
[RESPONSE_AGENT] Generated 2 recommendations
```

## Testing

### Unit Tests

```python
# tests/test_alert_agent.py
def test_normalize_prometheus_alert():
    # Test Prometheus normalization
    
def test_deduplication_fingerprint():
    # Test fingerprint generation and dedup

# tests/test_correlation_agent.py
def test_calculate_correlation_score():
    # Test similarity scoring
    
def test_cascading_failure_detection():
    # Test pattern detection

# tests/test_analysis_agent.py
def test_prepare_analysis_context():
    # Test context preparation
    
def test_fallback_analysis():
    # Test fallback when Ollama unavailable

# tests/test_response_agent.py
def test_generate_recommendations():
    # Test recommendation engine
    
def test_format_slack_message():
    # Test integration formatting
```

### Integration Tests

```python
# tests/test_agent_pipeline.py
async def test_end_to_end_alert_processing():
    """Test full pipeline from alert to response"""
    
    raw_alert = {...}
    
    # Alert Ingestion
    result1 = await ingestion_agent.ingest_alert(raw_alert)
    assert result1['status'] == 'created'
    
    # Correlation
    result2 = await correlation_agent.correlate_alerts(result1['alert'])
    assert 'incident_id' in result2
    
    # Analysis
    result3 = await analysis_agent.analyze_incident(result2['incident'])
    assert result3['analysis']['confidence'] > 0
    
    # Response
    result4 = await response_agent.generate_response(result3['analysis'], result2['incident'])
    assert len(result4['recommendations']) > 0
```

## Future Enhancements

1. **Distributed Agents**: Celery + RabbitMQ for distributed processing
2. **Agent Consensus**: Multiple LLM agents voting on root cause
3. **Autonomous Execution**: ResponseAgent executes actions automatically
4. **Continuous Learning**: Track recommendation effectiveness and adapt
5. **Custom Agents**: Extensible agent framework for domain-specific agents

