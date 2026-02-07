from crewai import Agent

noc_monitoring_agent = Agent(
    role="NOC Monitoring Agent",
    goal="Detect anomalies and normalize infrastructure health events",
    backstory=(
        "Enterprise NOC analyst AI monitoring infrastructure 24x7 "
        "and generating normalized health events."
    ),
    llm="ollama/llama3",

    verbose=True
)