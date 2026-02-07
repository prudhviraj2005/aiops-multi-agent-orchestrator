from crewai import Agent

remediation_agent = Agent(
    role="Remediation & Deployment Agent",
    goal="Execute safe auto-remediation with rollback and governance",
    backstory=(
        "A Site Reliability Engineering automation AI that performs controlled "
        "remediation actions with rollback plans."
    ),
    llm="ollama/llama3",
    verbose=True
)
