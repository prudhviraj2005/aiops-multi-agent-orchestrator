from pydantic import BaseModel
from typing import List, Dict, Any


class HealthEvent(BaseModel):
    event_id: str
    source: str
    severity: str
    metrics: Dict[str, Any]
    timestamp: str


class IncidentHypothesis(BaseModel):
    service: str
    probable_cause: str
    confidence: float
    blast_radius: List[str]


class PredictionReport(BaseModel):
    failure_type: str
    probability: float
    time_to_failure_minutes: int
    recommended_action: str


class ChangeRecord(BaseModel):
    change_id: str
    approved: bool
    executed: bool
    rollback_used: bool


class IncidentReport(BaseModel):
    summary: str
    sla_impact: str
    timeline: List[str]
    actions_taken: List[str]
    recommendations: List[str]
