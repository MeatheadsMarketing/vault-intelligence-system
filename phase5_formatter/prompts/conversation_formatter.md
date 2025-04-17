# GPT Conversation Formatting Prompt

This prompt guides GPT to produce outputs that are fully compatible with the Vault Intelligence Workflow.

---

## ✅ Format Expectations:

### 1. Markdown Code Blocks
Use triple backticks with language identifier:
```
```python
# code here
```

```

### 2. Tables (CSV-Parseable)
Use pipe `|` syntax, header row first:

| Column | Description |
|--------|-------------|
| assistant_id | A001 |
| prompt_id | P001 |
| status | draft |

---

### 3. Tag Blocks (for metadata)
Add below each output when applicable:

```
#META:
assistant_id: A001
door_type: Tool
value_class[]: ["builder", "packager"]
phase_created: P1
status: draft
```

---

### 4. Structural Priorities
- Use headers (##, ###) to separate assistant builds
- Include filename if generating a file
- Do NOT generate explanatory text unless requested
- Always wrap JSON in triple backticks

---

### Example Output Structure

## Streamlit Tool Packager

```markdown
# assistant_id: A001
# script_ref: package_tool_folder.py
# door_type: Tool
# status: Scaffold
```

```python
# package_tool_folder.py
def build():
    print("Packaging...")
```

```markdown
#META:
phase_created: P1
value_class[]: ["builder", "automator"]
```

---

GPT should follow this structure every time it’s asked to format an assistant, script, or manifest.
