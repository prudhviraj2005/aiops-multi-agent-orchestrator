from crewai import Agent

cloud_infra_agent = Agent(
    role="Cloud Infrastructure Agent",
    goal="Correlate multi-cloud infrastructure signals and identify infra-level issues",
    backstory=(
        "A multi-cloud reliability engineer AI specializing in AWS, Azure, and GCP "
        "infrastructure correlation."
    ),
    llm="ollama/llama3",

    verbose=True
)
