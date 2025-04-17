# p5_formatter_viewer.py
import streamlit as st
import os

st.title("Phase 5: GPT Conversation Formatter")
formatter_path = "phase5_formatter/prompts/conversation_formatter.md"

if os.path.exists(formatter_path):
    with open(formatter_path, 'r') as f:
        st.markdown(f.read())
else:
    st.warning("conversation_formatter.md not found.")
