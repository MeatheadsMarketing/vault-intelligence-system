# p5_mode_selector.py
import streamlit as st
import json
import os

st.title("Phase 5: GPT Mode Preset Selector")
preset_path = "phase5_formatter/settings/gpt_mode_presets.json"

if os.path.exists(preset_path):
    with open(preset_path, 'r') as f:
        modes = json.load(f)
        option = st.selectbox("Choose a GPT Mode", list(modes.keys()))
        st.json(modes[option])
else:
    st.warning("gpt_mode_presets.json not found.")
