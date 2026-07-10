import streamlit as st

st.set_page_config(
    page_title="RotaNet",
    page_icon="🚛",
    layout="wide"
)

st.title("RotaNet")

st.subheader("AI-Powered Logistics Decision Support Platform")

st.markdown("---")

st.header("Upload Dataset")

uploaded_file = st.file_uploader(
    "Upload a CSV or Excel file",
    type=["csv", "xlsx"]
)

st.markdown("---")

vehicle_count = st.number_input(
    "Number of Vehicles",
    min_value=1,
    value=3
)

st.button("Optimize Route")
