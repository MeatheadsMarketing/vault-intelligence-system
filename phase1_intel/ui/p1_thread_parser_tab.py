# p1_thread_parser_tab.py
import streamlit as st
import subprocess

st.title("Phase 1: Thread Parser")
st.markdown("Upload a GPT thread export and parse it using `thread_parser.py`.")

uploaded = st.file_uploader("Upload conversation.json", type="json")
if uploaded:
    with open("conversation.json", "wb") as f:
        f.write(uploaded.read())
    st.success("conversation.json uploaded.")

if st.button("Run Thread Parser"):
    result = subprocess.run(["python", "phase1_intel/thread_parser.py"], capture_output=True, text=True)
    st.code(result.stdout + result.stderr)
