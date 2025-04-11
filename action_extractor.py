from ollama_llm import llm

def action_extractor(state: dict) -> dict:
    message = state["customer_message"]
    prompt = f"Extract clear, actionable steps for support team based on this issue:\n\n{message}\n\nReturn them as a numbered list."
    actions = llm.invoke(prompt)
    state["actions"] = actions
    return state
