from ollama_llm import llm

def resolution_recommender(state: dict) -> dict:
    summary = state["summary"]
    prompt = f"Based on the summarized issue, suggest a possible resolution:\n\nSummary: {summary}"
    resolution = llm.invoke(prompt)
    state["suggested_resolution"] = resolution
    return state
