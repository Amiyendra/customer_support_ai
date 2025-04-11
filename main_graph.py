from typing import TypedDict
from langgraph.graph import StateGraph, END

from agents.summarizer import summarizer
from agents.action_extractor import action_extractor
from agents.resolution_recommender import resolution_recommender
from agents.router import router
from agents.time_estimator import time_estimator

class CustomerSupportState(TypedDict):
    customer_message: str
    summary: str
    actions: str
    suggested_resolution: str
    assigned_team: str
    estimated_time: str



builder = StateGraph(CustomerSupportState)




builder.add_node("summarizer", summarizer)
builder.add_node("action_extractor", action_extractor)
builder.add_node("resolution_recommender", resolution_recommender)
builder.add_node("router", router)
builder.add_node("time_estimator", time_estimator)



builder.set_entry_point("summarizer")
builder.add_edge("summarizer", "action_extractor")
builder.add_edge("action_extractor", "resolution_recommender")
builder.add_edge("resolution_recommender", "router")
builder.add_edge("router", "time_estimator")
builder.add_edge("time_estimator", END)

graph = builder.compile()





if __name__ == "__main__":
    input_state = {
        "customer_message": "After the latest update, my app won't open. It crashes immediately on launch. I need help ASAP."
    }

    final_state = graph.invoke(input_state)

    print("\n🧾 Final Output:")
    for key, value in final_state.items():
        print(f"{key}: {value}\n")
