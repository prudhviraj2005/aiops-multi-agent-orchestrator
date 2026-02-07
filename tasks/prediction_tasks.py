from crewai import Task
from callbacks.callbacks import prediction_callback
from schemas.models import PredictionReport

def prediction_task(agent):
    return Task(
        description="Predict failure",
        expected_output="PredictionReport JSON",
        agent=agent,
        callback=prediction_callback,
        output_json=PredictionReport
    )
