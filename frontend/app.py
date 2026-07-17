import streamlit as st
import pandas as pd

from ai_engine import get_ai_recommendation

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="RotaNet",
    page_icon="🚛",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("RotaNet")
st.caption("AI-Powered Logistics Operations Decision Support Platform")

st.divider()
# --------------------------------------------------
# Sidebar
# --------------------------------------------------

with st.sidebar:

    st.header("Operations Panel")

    st.markdown("### AI Configuration")

    api_key = st.text_input(
        "Gemini API Key",
        type="password",
        placeholder="Enter your Gemini API Key"
    )

    st.divider()

    st.markdown("### Dataset")

    uploaded_file = st.file_uploader(
        "Upload Drivers / Vehicles / Deliveries",
        type=["csv", "xlsx"]
    )

    st.divider()

    st.markdown("### Optimization Settings")

    num_vehicles = st.number_input(
        "Available Vehicles",
        min_value=1,
        value=3,
        step=1
    )

    optimize = st.button(
        "Start Optimization",
        use_container_width=True
    )
    # --------------------------------------------------
# Main Dashboard
# --------------------------------------------------

st.subheader("Operations Dashboard")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Drivers", "--")

with col2:
    st.metric("Vehicles", "--")

with col3:
    st.metric("Deliveries", "--")

with col4:
    st.metric("Estimated Cost", "--")

st.divider()

left_col, right_col = st.columns([2, 1])
with left_col:

    st.subheader("Optimization Results")

    result_placeholder = st.empty()

    st.info("Optimization results will be displayed here.")

    st.subheader("Interactive Route Map")

    map_placeholder = st.empty()

    st.info("Route visualization will appear here.")
    with right_col:

    st.subheader("AI Insights")

    ai_placeholder = st.empty()

    st.info("AI recommendations will appear here.")

    st.subheader("Operational Summary")

    st.info("Fleet utilization and operational metrics will appear here.")
