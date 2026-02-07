from crewai import Agent

reporting_agent = Agent(
    role="Reporting & Compliance Agent",
    goal="Generate audit-ready incident reports and SLA impact analysis",
    backstory=(
        "A compliance and reporting AI responsible for post-incident analysis "
        "and audit documentation."
    ),
    llm="ollama/llama3",

    verbose=True
)
