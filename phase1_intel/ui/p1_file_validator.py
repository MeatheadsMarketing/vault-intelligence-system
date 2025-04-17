# p1_file_validator.py
import streamlit as st
import os

st.title("Phase 1: File Validator")

PHASE_1_FILES = [
    "phase1_intel/thread_parser.py",
    "phase1_intel/thread_table_extractor.py",
    "phase1_intel/door_manifest.json",
    "phase1_intel/phase1_summary.md",
    "phase1_intel/utilities/message_intent_classifier.py",
    "phase1_intel/utilities/table_context_linker.py",
    "phase1_intel/utilities/table_fingerprint_hasher.py",
    "phase1_intel/flags/thread_merge_tool.py",
    "phase1_intel/flags/flagged_ideas.csv"
]

completed = 0

for file in PHASE_1_FILES:
    if os.path.exists(file):
        st.success(f"✅ {file}")
        completed += 1
    else:
        st.error(f"❌ {file}")

st.markdown(f"**Phase 1 File Completion:** `{completed}/{len(PHASE_1_FILES)}`")
st.progress(completed / len(PHASE_1_FILES))
