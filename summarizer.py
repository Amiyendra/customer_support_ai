from ollama_llm import llm

def summarizer(state: dict) -> dict:
    message = state["customer_message"]
    prompt = f"Summarize the customer issue:\n\n{message}"
    summary = llm.invoke(prompt)
    state["summary"] = summary
    return state
