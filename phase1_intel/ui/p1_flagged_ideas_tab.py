# p1_flagged_ideas_tab.py
import streamlit as st
import pandas as pd
import os

st.title("Phase 1: Flagged Ideas")
csv_file = "phase1_intel/flags/flagged_ideas.csv"

if os.path.exists(csv_file):
    df = pd.read_csv(csv_file)
    df['status'] = df['status'].apply(lambda x: f"🟡 {x}" if x != "done" else "✅ done")
    st.dataframe(df)
else:
    st.warning("No flagged_ideas.csv found.")
