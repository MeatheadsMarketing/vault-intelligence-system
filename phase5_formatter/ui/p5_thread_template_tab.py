# p5_thread_template_tab.py
import streamlit as st
import os

st.title("Phase 5: Thread Starter Template")
template_path = "phase5_formatter/templates/thread_scaffolding_template.md"

if os.path.exists(template_path):
    with open(template_path, 'r') as f:
        content = f.read()
        st.text_area("Thread Scaffolding Template", value=content, height=400)
else:
    st.warning("thread_scaffolding_template.md not found.")
