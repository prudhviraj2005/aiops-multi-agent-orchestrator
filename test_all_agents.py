from agents.noc_monitoring_agent import noc_monitoring_agent
from agents.cloud_infra_agent import cloud_infra_agent
from agents.app_observability_agent import app_observability_agent
from agents.predictive_agent import predictive_agent
from agents.remediation_agent import remediation_agent
from agents.reporting_agent import reporting_agent
from agents.manager_agent import manager_agent

agents = [
    noc_monitoring_agent,
    cloud_infra_agent,
    app_observability_agent,
    predictive_agent,
    remediation_agent,
    reporting_agent,
    manager_agent
]

for agent in agents:
    print("Loaded:", agent.role)
