# Output Format Specification – Vault Intelligence Workflow

This document defines the official schema and formatting expectations for any GPT-generated assistant, prompt, table, manifest, or script intended for use within the system.

---

## ✅ Core Format Types

### 1. Markdown Code Blocks

```python
# filename: script_name.py
def run():
    pass
```

Used for scripts, manifest examples, prompt builders.

---

### 2. Tables (Markdown-Style)

| Field | Description |
|-------|-------------|
| assistant_id | Unique assistant ID |
| name | Descriptive assistant name |
| door_type | Tool, Prompt, Shortcut, etc. |
| status | Concept, Scaffold, Ready, Validated |

---

### 3. Metadata Blocks (`#META:`)

```
#META:
assistant_id: A001
prompt_id: P001
value_class[]: ["builder", "script_generator"]
phase_created: P1
door_type: Tool
status: scaffold
```

Used for structured GPT memory and automated Phase 1 parsing.

---

## ✅ Field Rules

| Field | Required | Type |
|-------|----------|------|
| assistant_id | ✅ | string (e.g. A001) |
| prompt_id | ✅ | string |
| door_type | ✅ | select (Tool, Shortcut, Script, etc.) |
| value_class[] | ⚪ | array of tags |
| status | ✅ | Concept, Scaffold, Ready, Validated |
| phase_created | ✅ | string (P1–P5) |

---

## ✅ Block Sequencing

1. Title Header (##)
2. Markdown code block (optional)
3. Table (if needed)
4. Metadata block (`#META:`)

---

## ✅ Example Output

```
## Streamlit Tool Packager

```python
# package_tool_folder.py
def build():
    print("Packaging")
```

```
#META:
assistant_id: A001
door_type: Tool
value_class[]: ["builder"]
phase_created: P1
status: scaffold
```
```

