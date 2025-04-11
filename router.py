from ollama_llm import llm

def router(state: dict) -> dict:
    summary = state["summary"]
    prompt = f"Based on this customer issue, which internal team should handle this? (e.g., Technical Support, Billing, Product Team):\n\n{summary}"
    team = llm.invoke(prompt)
    state["assigned_team"] = team
    return state
