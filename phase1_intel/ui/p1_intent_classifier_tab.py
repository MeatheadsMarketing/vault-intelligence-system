# p1_intent_classifier_tab.py
import streamlit as st
import subprocess

st.title("Phase 1: Intent Classifier")
st.markdown("Run message intent classification script.")

if st.button("Classify Intents"):
    result = subprocess.run(["python", "phase1_intel/utilities/message_intent_classifier.py"], capture_output=True, text=True)
    st.code(result.stdout + result.stderr)
