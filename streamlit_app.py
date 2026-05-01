import streamlit as st
import uuid

from app.classifier import is_engineering_query
from app.router import route_query
from app.model_handler import query_model
from app.evaluator import score_response, select_best
from app.memory import MemoryStore

# Initialize
st.set_page_config(page_title="Multi-Model AI Chatbot", layout="centered")

st.title("🤖 Engineering Multi-Model AI Chatbot")

if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

if "memory" not in st.session_state:
    st.session_state.memory = MemoryStore()

session_id = st.session_state.session_id
memory = st.session_state.memory

# Chat input
query = st.text_input("Ask your engineering question:")

if st.button("Send"):

    if not query:
        st.warning("Please enter a question.")
    
    elif not is_engineering_query(query):
        st.error("❌ Sorry, this chatbot is only for engineering-related topics.")
    
    else:
        category = route_query(query)

        with st.spinner("Thinking across multiple models..."):

            responses = []

            for model_type in ["math", "code", "theory"]:
                res = query_model(model_type, query)
                score = score_response(res)

                responses.append({
                    "response": res,
                    "score": score,
                    "model": model_type
                })

            best = select_best(responses)

            memory.add(session_id, query, best)

        st.success("✅ Best Response:")
        st.write(best)

# Show chat history
st.subheader("🧠 Chat Memory")

history = memory.get(session_id)

for chat in history[::-1]:
    st.write(f"**You:** {chat['query']}")
    st.write(f"**Bot:** {chat['response']}")
    st.markdown("---")