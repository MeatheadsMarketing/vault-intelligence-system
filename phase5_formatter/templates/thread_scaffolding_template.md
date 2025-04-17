# GPT Thread Starter Template – Vault Intelligence System

This is the official layout for beginning any GPT thread that contributes to the Vault Intelligence Workflow system.

---

## Header Template

```
#THREAD_ROLE: Builder
#TOKENS_PRIORITY: Assistant generation
#PHASE: P3
#GOALS: Generate folder, manifest, and streamlit launcher
```

---

## Instruction Block

Please generate an assistant named **Streamlit Tool Packager**.  
It should:
- Build a folder scaffold with `/scripts/`, `/logs/`, `/meta/`, `/ui/`
- Include a `manifest.json` with assistant_id, prompt_id, script_ref
- Include a `README.md` with summary
- Format output using markdown code blocks

---

## Output Format Expectations

```python
# streamlit_launcher.py
def launch():
    pass
```

```
#META:
assistant_id: A001
prompt_id: P001
phase_created: P3
door_type: Tool
value_class[]: ["builder", "streamlit"]
status: scaffold
```

---

## Prompt Reminders
- Format every file in triple backtick code blocks
- Include `#META:` blocks below code when appropriate
- Always use headers to break sections

This structure ensures all outputs are valid, parsable, and ready for deployment.
