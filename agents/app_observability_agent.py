from crewai import Agent

app_observability_agent = Agent(
    role="Application Observability Agent",
    goal="Analyze application latency, error rates, and traces to find root causes",
    backstory=(
        "An application performance monitoring specialist AI focused on telemetry "
        "and distributed tracing."
    ),
    llm="ollama/llama3",

    verbose=True
)
