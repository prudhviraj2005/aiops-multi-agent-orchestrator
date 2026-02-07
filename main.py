from crewai import Crew

# Agents
from agents.noc_monitoring_agent import noc_monitoring_agent
from agents.cloud_infra_agent import cloud_infra_agent
from agents.app_observability_agent import app_observability_agent
from agents.predictive_agent import predictive_agent
from agents.remediation_agent import remediation_agent
from agents.reporting_agent import reporting_agent
from agents.manager_agent import manager_agent

# Tasks
from tasks.monitoring_tasks import monitoring_task
from tasks.analysis_tasks import analysis_task
from tasks.prediction_tasks import prediction_task
from tasks.remediation_tasks import remediation_task
from tasks.reporting_tasks import reporting_task

# ✅ CREATE TASK OBJECTS
# Create Task objects with explicit agents
monitor_task = monitoring_task(noc_monitoring_agent)
analysis = analysis_task(cloud_infra_agent)
predict = prediction_task(predictive_agent)
remediate = remediation_task(remediation_agent)
report = reporting_task(reporting_agent)

# Crew
crew = Crew(
    agents=[
        noc_monitoring_agent,
        cloud_infra_agent,
        app_observability_agent,
        predictive_agent,
        remediation_agent,
        reporting_agent
    ],
    tasks=[
        monitor_task,
        analysis,
        predict,
        remediate,
        report
    ],
    manager_agent=manager_agent,
    memory=False
)

event = {
    "event_id": "EVT-9001",
    "source": "AWS",
    "severity": "SEV2",
    "service": "checkout-service",
    "metrics": {
        "cpu": 95,
        "latency_ms": 1200,
        "error_rate": 8.2
    },
    "timestamp": "2026-02-07T14:45:00Z"
}

if __name__ == "__main__":
    result = crew.kickoff(inputs=event)
    print("\n=== FINAL INCIDENT REPORT ===\n")
    print(result)
