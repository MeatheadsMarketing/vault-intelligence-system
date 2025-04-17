# p5_output_schema_viewer.py
import streamlit as st
import os

st.title("Phase 5: Output Format Schema")
schema_path = "phase5_formatter/docs/output_format_spec.md"

if os.path.exists(schema_path):
    with open(schema_path, 'r') as f:
        st.markdown(f.read())
else:
    st.warning("output_format_spec.md not found.")
