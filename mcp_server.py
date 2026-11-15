from langsmith import Client, tracing_context

destination = input("LangSmith destination type (agent/project): ").strip().lower()
if destination == "agent":
    os.environ.pop("LANGSMITH_PROJECT", None)
    os.environ["LANGSMITH_AGENT_ID"] = input("Agent ID: ").strip()
    os.environ["LANGSMITH_AGENT_ENVIRONMENT"] = input(
        "Environment (for example local): "
    ).strip()
elif destination == "project":
    os.environ.pop("LANGSMITH_AGENT_ID", None)
    os.environ.pop("LANGSMITH_AGENT_ENVIRONMENT", None)
    os.environ["LANGSMITH_PROJECT"] = input("Project name: ").strip()
else:
    raise ValueError("Enter agent or project, then rerun this cell.")

endpoint = input("LangSmith API URL (blank for default US): ").strip()
if endpoint:
    os.environ["LANGSMITH_ENDPOINT"] = endpoint
workspace_id = input("Workspace ID (blank if unnecessary): ").strip()
if workspace_id:
    os.environ["LANGSMITH_WORKSPACE_ID"] = workspace_id
smith_key = getpass("LangSmith API key: ").strip()
smith_client = Client(api_key=smith_key)
print("Tracing client configured.")
