# p5_message_wrapper_tab.py
import streamlit as st
import subprocess

st.title("Phase 5: GPT Message Wrapper")
st.markdown("Run `gpt_message_wrapper.py` to structure legacy GPT outputs.")

if st.button("Wrap Messages"):
    result = subprocess.run(["python", "phase5_formatter/utilities/gpt_message_wrapper.py"], capture_output=True, text=True)
    st.code(result.stdout + result.stderr)
