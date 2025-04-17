# p1_summary_panel.py
import streamlit as st
import os

st.title("Phase 1: Summary Panel")
summary_file = "phase1_intel/phase1_summary.md"

if os.path.exists(summary_file):
    with open(summary_file, 'r') as f:
        content = f.read()
        st.markdown(content)
else:
    st.warning("Summary file not found.")
