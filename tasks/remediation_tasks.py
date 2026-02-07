from crewai import Task
from callbacks.callbacks import remediation_callback
from schemas.models import ChangeRecord

def remediation_task(agent):
    return Task(
        description="Execute remediation",
        expected_output="ChangeRecord JSON",
        agent=agent,
        callback=remediation_callback,
        output_json=ChangeRecord
    )
