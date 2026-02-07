from crewai import Agent

predictive_agent = Agent(
    role="Predictive Maintenance Agent",
    goal="Predict failures and recommend preventive actions",
    backstory=(
        "An AI trained on historical incidents and system trends to forecast "
        "failures before they occur."
    ),
    llm="ollama/llama3",

    verbose=True
)
