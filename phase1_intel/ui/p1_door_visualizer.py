# p1_door_visualizer.py
import streamlit as st
import json
import os

st.title("Phase 1: Door Visualizer")
manifest_file = "phase1_intel/door_manifest.json"

if os.path.exists(manifest_file):
    with open(manifest_file, 'r') as f:
        data = json.load(f)
        st.subheader("Primary Doors")
        st.checkbox("All", value=True)
        for door in data.get("primary_doors", []):
            st.checkbox(door)
        st.subheader("Unseen Doors")
        for door in data.get("unseen_doors", []):
            st.checkbox(door)
else:
    st.warning("door_manifest.json not found.")
