from crewai import Task
from callbacks.callbacks import analysis_callback
from schemas.models import IncidentHypothesis

def analysis_task(agent):
    return Task(
        description="Analyze root cause",
        expected_output="IncidentHypothesis JSON",
        agent=agent,
        callback=analysis_callback,
        output_json=IncidentHypothesis
    )
