# p5_header_mapper_tab.py
import streamlit as st
import subprocess

st.title("Phase 5: Header Normalizer")
st.markdown("Run `auto_header_mapper.py` to align GPT headers to schema.")

if st.button("Run Header Mapper"):
    result = subprocess.run(["python", "phase5_formatter/utilities/auto_header_mapper.py"], capture_output=True, text=True)
    st.code(result.stdout + result.stderr)
