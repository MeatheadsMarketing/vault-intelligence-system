# streamlit_app.py – Launch entry for Vault Intelligence System
import streamlit as st
import subprocess

st.set_page_config(page_title="Vault Intelligence System", layout="wide")
st.title("🧠 Vault Intelligence System – Master Dashboard")

st.markdown("Use the sidebar to navigate through Phase 1 to Phase 5 UI modules.")
st.markdown("Each phase includes file validators, dashboards, and action triggers.")

if st.button("Open Main Launcher"):
    subprocess.Popen(["streamlit", "run", "vault_ui_launcher.py"])
    st.success("Main UI launched.")
