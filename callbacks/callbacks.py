import json
from schemas.models import (
    HealthEvent,
    IncidentHypothesis,
    PredictionReport,
    ChangeRecord,
    IncidentReport
)

def _safe_json(inputs):
    """
    Normalize CrewAI TaskOutput JSON into a dict.
    Handles dict | JSON string | None.
    """
    raw = getattr(inputs, "json", None)

    if isinstance(raw, dict):
        return raw

    if isinstance(raw, str):
        try:
            return json.loads(raw)
        except Exception:
            return {}

    return {}


def monitoring_callback(inputs):
    data = _safe_json(inputs)

    return HealthEvent(
        event_id=data.get("event_id", "UNKNOWN"),
        source=data.get("source", "UNKNOWN"),
        severity=data.get("severity", "INFO"),
        metrics=data.get("metrics", {}),
        timestamp=data.get("timestamp", "")
    ).model_dump()


def analysis_callback(inputs):
    data = _safe_json(inputs)

    return IncidentHypothesis(
        service=data.get("service", "unknown-service"),
        probable_cause="High CPU saturation",
        confidence=0.87,
        blast_radius=[data.get("service", "unknown-service")]
    ).model_dump()


def prediction_callback(inputs):
    data = _safe_json(inputs)

    return PredictionReport(
        failure_type="CPU Exhaustion",
        probability=0.78,
        time_to_failure_minutes=25,
        recommended_action="Scale service"
    ).model_dump()


def remediation_callback(inputs):
    data = _safe_json(inputs)

    return ChangeRecord(
        change_id="CHG-2026-001",
        approved=True,
        executed=True,
        rollback_used=False
    ).model_dump()


def reporting_callback(inputs):
    data = _safe_json(inputs)

    return IncidentReport(
        summary="High CPU caused latency spike in checkout-service",
        sla_impact="SLA breach avoided",
        timeline=[
            "Anomaly detected",
            "Root cause identified",
            "Failure predicted",
            "Auto-remediation executed"
        ],
        actions_taken=["Scaled service"],
        recommendations=["Enable predictive autoscaling"]
    ).model_dump()
