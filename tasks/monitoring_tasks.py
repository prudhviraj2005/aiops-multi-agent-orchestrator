from crewai import Task
from callbacks.callbacks import monitoring_callback
from schemas.models import HealthEvent

def monitoring_task(agent):
    return Task(
    description="Normalize incoming event",
    expected_output="HealthEvent JSON",
    agent=agent,
    callback=monitoring_callback,
    output_json=HealthEvent


)

