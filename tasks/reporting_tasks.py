from crewai import Task
from callbacks.callbacks import reporting_callback
from schemas.models import IncidentReport

def reporting_task(agent):
    return Task(
        description="Generate incident report",
        expected_output="IncidentReport JSON",
        agent=agent,
        callback=reporting_callback,
        output_json=IncidentReport
    )
