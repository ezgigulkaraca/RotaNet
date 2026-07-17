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
