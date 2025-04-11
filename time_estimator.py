from ollama_llm import llm

def time_estimator(state: dict) -> dict:
    summary = state["summary"]
    resolution = state["suggested_resolution"]
    prompt = f"Estimate how long it would take to resolve this issue:\n\nIssue Summary: {summary}\nSuggested Fix: {resolution}\n\nRespond with time estimate in plain text (e.g., 'We estimate this may take 4 hours, since similar issues involved firmware rollback and coordination with the hardware team.')."
    time = llm.invoke(prompt)
    state["estimated_time"] = time
    return state
