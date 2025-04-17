# vault_ui_launcher.py
# Master visualization dashboard for Vault Intelligence Workflow

import streamlit as st
import os

PHASES = {
    "P1 – Vault Intelligence System": "phase1_intel",
    "P2 – Opportunity Library": "phase2_libraries",
    "P3 – Packaging System": "phase3_packages",
    "P4 – Validation Framework": "phase4_validation",
    "P5 – GPT Format Layer": "phase5_formatter"
}

PHASE_CHECKLIST = {
    "phase1_intel": [
        "thread_parser.py",
        "thread_table_extractor.py",
        "door_manifest.json",
        "phase1_summary.md",
        "utilities/message_intent_classifier.py",
        "utilities/table_context_linker.py",
        "utilities/table_fingerprint_hasher.py",
        "flags/thread_merge_tool.py",
        "flags/flagged_ideas.csv"
    ],
    "phase2_libraries": [
        "docs/notion_template_schema.md",
        "scripts/notion_loader.py",
        "scripts/asset_type_normalizer.py",
        "scripts/multi_tag_sync.py",
        "utilities/library_health_check.py",
        "utilities/assistant_similarity_checker.py"
    ],
    "phase3_packages": [
        "assistant_packager.py",
        "manifest_generator.py",
        "zip_packager.py",
        "ui/streamlit_assistant_launcher.py",
        "meta/version_manifest.json",
        "logs/run_log.txt",
        "utilities/package_validator.py",
        "logs/execution_summary_writer.py"
    ],
    "phase4_validation": [
        "validator.py",
        "run_assistant_test.py",
        "logs/system_run_log.csv",
        "sync/push_to_notion.sh",
        "sync/push_to_github.sh",
        "ui/status_dashboard.py",
        "logs/error_log_sync.py",
        "utilities/usage_counter.py"
    ],
    "phase5_formatter": [
        "prompts/conversation_formatter.md",
        "docs/output_format_spec.md",
        "settings/gpt_mode_presets.json",
        "templates/thread_scaffolding_template.md",
        "utilities/gpt_message_wrapper.py",
        "utilities/auto_header_mapper.py",
        "tools/prompt_suggestion_engine.py"
    ]
}

def check_file_exists(phase, rel_path):
    full_path = os.path.join(phase, rel_path)
    return os.path.exists(full_path)

def main():
    st.set_page_config("Vault Intelligence Launcher", layout="wide")
    st.title("Vault Intelligence Launcher – System Control UI")

    selected_phase = st.selectbox("Select a Phase to View:", list(PHASES.keys()))
    phase_folder = PHASES[selected_phase]

    st.subheader(f"{selected_phase} Checklist Validation")
    files = PHASE_CHECKLIST.get(phase_folder, [])

    total = len(files)
    completed = 0
    for file in files:
        if check_file_exists(phase_folder, file):
            st.success(f"✅ {file}")
            completed += 1
        else:
            st.error(f"❌ {file}")

    st.markdown(f"**Phase Completion:** `{completed}/{total}` files")
    st.progress(completed / total)

if __name__ == "__main__":
    main()
