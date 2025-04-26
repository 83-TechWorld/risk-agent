import streamlit as st
from kri_agent import db_chain

st.set_page_config(page_title="KRI Agent Chat", page_icon="🛡️", layout="wide")

st.title("🛡️ KRI Agent - Manage Risk Indicators")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

prompt = st.chat_input("Ask about KRIs... (Insert, Update, Delete)")

if prompt:
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    try:
        response = db_chain.run(prompt)
    except Exception as e:
        response = f"❌ Error: {str(e)}"

    st.chat_message("assistant").markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
