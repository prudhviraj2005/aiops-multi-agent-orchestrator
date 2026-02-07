from crewai import Agent

manager_agent = Agent(
    role="IT Operations Orchestrator",
    goal="Delegate tasks, enforce safety policies, and resolve conflicts",
    backstory=(
        "A senior IT operations manager AI overseeing incident response, "
        "change approvals, and coordination between agents."
    ),
    llm="ollama/llama3",

    verbose=True
)
