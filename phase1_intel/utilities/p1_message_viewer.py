# p1_message_viewer.py
import streamlit as st
import pandas as pd
import os

st.title("Phase 1: Parsed Message Viewer")

csv_file = "parsed_thread_output.csv"

if os.path.exists(csv_file):
    df = pd.read_csv(csv_file)
    st.dataframe(df)
    st.success(f"Loaded {len(df)} parsed messages.")
else:
    st.warning("No parsed_thread_output.csv found. Run the parser first.")
