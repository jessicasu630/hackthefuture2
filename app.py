import streamlit as st
import requests

st.set_page_config(page_title="SupplyChain Resilience Agent", layout="wide")
st.title("SupplyChain Resilience Agent (Demo)")

# Read Cloud Run URL from Streamlit Secrets
cloud_run_url = ""
try:
    cloud_run_url = st.secrets["CLOUD_RUN_URL"]
except Exception:
    pass

st.sidebar.header("Config")
cloud_run_url = st.sidebar.text_input("Cloud Run URL", value=cloud_run_url).strip()

if not cloud_run_url:
    st.warning("Add CLOUD_RUN_URL in Streamlit Secrets, or paste your Cloud Run URL in the sidebar.")
    st.stop()

base = cloud_run_url.rstrip("/")

col1, col2 = st.columns(2)

with col1:
    st.subheader("1) Pull disruption signals (GDELT)")
    if st.button("Ingest GDELT"):
        r = requests.get(f"{base}/ingest_gdelt", timeout=60)
        st.json(r.json())

with col2:
    st.subheader("2) Health check")
    if st.button("Ping /health"):
        r = requests.get(f"{base}/health", timeout=30)
        st.write(r.text)

st.divider()
st.info("Next step (later): add endpoints like /latest_events and /run_agent to show risk + mitigation plans.")
