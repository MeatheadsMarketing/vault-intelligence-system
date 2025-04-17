# Phase 1 Execution Checklist – `P1-VIS`
## Vault Intelligence System

This file tracks every build task required to complete Phase 1 of the GPT Intelligence Workflow.

---

## Overview
Phase 1 parses your GPT thread archive, extracts all assets (assistants, prompts, shortcuts, tables, scripts), and maps them to the correct “door” categories. Output files serve as the input foundation for Phase 2 libraries.

---

## File Build Checklist

| Task | File | Purpose | Folder | Status |
|------|------|---------|--------|--------|
| Build parser | `thread_parser.py` | Extracts all messages from GPT export | `/phase1_intel/` | [ ] |
| Build table extractor | `thread_table_extractor.py` | Detects, parses, and splits large tables (up to 200+ rows) | `/phase1_intel/` | [ ] |
| Generate door map | `door_manifest.json` | Maps message types to opportunity doors (Streamlit, Shortcuts, etc.) | `/phase1_intel/` | [ ] |
| Summarize intelligence | `phase1_summary.md` | Manual insights summary of key assistants, tools, prompts | `/phase1_intel/` | [ ] |
| Message tagger | `message_intent_classifier.py` | Tags each message with intent type (Build, Validate, Plan) | `/phase1_intel/utilities/` | [ ] |
| Table-to-context linker | `table_context_linker.py` | Connects each table to related assistant or prompt | `/phase1_intel/utilities/` | [ ] |
| Placeholder scanner | `flagged_ideas.csv` | Captures underdeveloped thoughts and TODOs | `/phase1_intel/flags/` | [ ] |
| Table fingerprint matcher | `table_fingerprint_hasher.py` | Groups duplicate table structures across threads | `/phase1_intel/utilities/` | [ ] |
| Merge tool for GPT splits | `thread_merge_tool.py` | Merges GPT exports that were split across multiple runs | `/phase1_intel/flags/` | [ ] |

---

## Phase Gate (PGP-1) Final Pass

| Checkpoint | Description | Status |
|------------|-------------|--------|
| ✅ Structural | All files and folders exist | [ ] |
| ✅ Functional | All `.py` scripts run successfully | [ ] |
| ✅ Dependency | CSV outputs match Phase 2 schema | [ ] |
| ✅ Intentionality | Minimum viable output: 1 assistant, 1 prompt, 3 door types | [ ] |

---

## Notes:
- This phase is the foundation of your entire system.
- If any file is skipped or broken, all downstream phases will fail parsing or sync.
- Run `python phase_gate_verifier.py --phase 1` to auto-check phase health.
