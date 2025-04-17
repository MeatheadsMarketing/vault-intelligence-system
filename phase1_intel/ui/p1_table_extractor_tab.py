# p1_table_extractor_tab.py
import streamlit as st
import subprocess

st.title("Phase 1: Table Extractor")
st.markdown("Run the table extractor script to pull markdown tables from parsed messages.")

if st.button("Extract Tables"):
    result = subprocess.run(["python", "phase1_intel/thread_table_extractor.py"], capture_output=True, text=True)
    st.code(result.stdout + result.stderr)
