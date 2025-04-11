import streamlit as st
from main_graph import graph
import time


st.set_page_config(
    page_title="AI Customer Support System",
    layout="centered",
    page_icon="🤖",
)


st.markdown("""
    <style>
        .big-title {
            font-size: 36px;


        font-weight: 800;
            
            color: #4B8BBE;
    text-align: center;
             margin-bottom: 20px;
        }


            
        .sub-box {
            background-color: #f1f3f6;
            color: #000; 
            padding: 16px;
            border-radius: 12px;
            margin: 10px 0;
            box-shadow: 0 1px 6px rgba(0,0,0,0.1);
        }
        .footer {
            margin-top: 40px;
            text-align: center;
            font-size: 14px;
            color: #999;
        }
    </style>
""", unsafe_allow_html=True)


st.markdown('<div class="big-title">AI-Powered Customer Support 🤖</div>', unsafe_allow_html=True)

st.markdown("Use this demo to process support queries using a multi-agent LLM system with LangGraph & Ollama.")


with st.container():
    st.subheader("📝 Enter Customer Issue")
    user_message = st.text_area("What is the customer saying?", placeholder="E.g. 'App crashes on launch after update...'", height=150)


if st.button("Run AI Agents"):
    if not user_message.strip():
        st.warning("Please enter a customer message first.")
    else:
        with st.spinner("Running AI agents..."):
            time.sleep(1)
            final_state = graph.invoke({"customer_message": user_message})

        st.success("AI processing complete! 🎉")


        st.subheader("🧾 Output Summary")

        agent_labels = {
            "summary": "📝 Summary",
            "actions": "✅ Extracted Actions",
            "suggested_resolution": "💡 Suggested Resolution",
            "assigned_team": "👥 Assigned Team",
            "estimated_time": "⏳ Estimated Resolution Time",
        }

        for key in ["summary", "actions", "suggested_resolution", "assigned_team", "estimated_time"]:
            if key in final_state:
                st.markdown(f"""
                <div class="sub-box">
                    <strong>{agent_labels[key]}</strong><br>
                    {final_state[key]}
                </div>
                """, unsafe_allow_html=True)


st.markdown('<div class="footer">Built with ❤️ using LangGraph, Ollama & Streamlit</div>', unsafe_allow_html=True)
