# p5_prompt_remix_tab.py
import streamlit as st
import subprocess
import pandas as pd
import os

st.title("Phase 5: Prompt Remix Engine")
st.markdown("Run `prompt_suggestion_engine.py` to generate prompt variants.")

if st.button("Remix Prompts"):
    result = subprocess.run(["python", "phase5_formatter/tools/prompt_suggestion_engine.py"], capture_output=True, text=True)
    st.code(result.stdout + result.stderr)

if os.path.exists("prompt_variants.csv"):
    df = pd.read_csv("prompt_variants.csv")
    st.dataframe(df)
