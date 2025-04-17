# p5_file_validator.py
import streamlit as st
import os

st.title("Phase 5: File Completion Validator")

PHASE_5_FILES = [
    "phase5_formatter/prompts/conversation_formatter.md",
    "phase5_formatter/docs/output_format_spec.md",
    "phase5_formatter/settings/gpt_mode_presets.json",
    "phase5_formatter/templates/thread_scaffolding_template.md",
    "phase5_formatter/utilities/gpt_message_wrapper.py",
    "phase5_formatter/utilities/auto_header_mapper.py",
    "phase5_formatter/tools/prompt_suggestion_engine.py"
]

completed = 0
for file in PHASE_5_FILES:
    if os.path.exists(file):
        st.success(f"✅ {file}")
        completed += 1
    else:
        st.error(f"❌ {file}")

st.markdown(f"**Phase 5 File Completion:** `{completed}/{len(PHASE_5_FILES)}`")
st.progress(completed / len(PHASE_5_FILES))
