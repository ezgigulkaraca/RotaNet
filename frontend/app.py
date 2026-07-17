import streamlit as st
import pandas as pd

from backend.ai_service import get_ai_insights

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

    st.subheader("AI Configuration")

    api_key = st.text_input(
        "Gemini API Key",
        type="password",
        placeholder="Paste your Gemini API Key"
    )

    st.divider()

    st.subheader("Datasets")

    drivers_file = st.file_uploader(
        "Drivers Dataset",
        type=["csv", "xlsx"]
    )

    vehicles_file = st.file_uploader(
        "Vehicles Dataset",
        type=["csv", "xlsx"]
    )

    deliveries_file = st.file_uploader(
        "Deliveries Dataset",
        type=["csv", "xlsx"]
    )

    st.divider()

    optimize_button = st.button(
        "Start Optimization",
        use_container_width=True
    )

# --------------------------------------------------
# Dataset Loading
# --------------------------------------------------

def load_dataset(uploaded_file):

    if uploaded_file is None:
        return None

    if uploaded_file.name.endswith(".csv"):
        return pd.read_csv(uploaded_file)

    return pd.read_excel(uploaded_file)


drivers = load_dataset(drivers_file)
vehicles = load_dataset(vehicles_file)
deliveries = load_dataset(deliveries_file)

# --------------------------------------------------
# KPI Cards
# --------------------------------------------------

driver_count = len(drivers) if drivers is not None else 0
vehicle_count = len(vehicles) if vehicles is not None else 0
delivery_count = len(deliveries) if deliveries is not None else 0

total_weight = 0

if deliveries is not None:

    if "Weight" in deliveries.columns:
        total_weight = deliveries["Weight"].sum()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Drivers", driver_count)

with col2:
    st.metric("Vehicles", vehicle_count)

with col3:
    st.metric("Deliveries", delivery_count)

with col4:
    st.metric("Total Weight (kg)", total_weight)

st.divider()

# --------------------------------------------------
# Main Layout
# --------------------------------------------------

left, right = st.columns([2, 1])

# --------------------------------------------------
# LEFT PANEL
# --------------------------------------------------

with left:

    st.subheader("Delivery Dataset")

    if deliveries is not None:
        st.dataframe(deliveries, use_container_width=True)

    else:
        st.info("Upload Deliveries Dataset to continue.")

    st.divider()

    st.subheader("Interactive Map")

    st.info("Map integration will be added in the next version.")
    # --------------------------------------------------
# RIGHT PANEL
# --------------------------------------------------

with right:

    st.subheader("AI Insights")

    if optimize_button:

        if api_key == "":
            st.warning("Please enter your Gemini API Key.")

        elif drivers is None or vehicles is None or deliveries is None:
            st.warning("Please upload Drivers, Vehicles and Deliveries datasets.")

        else:

            with st.spinner("AI is analyzing logistics operations..."):

                try:

                    ai_result = get_ai_insights(
                        api_key,
                        drivers,
                        vehicles,
                        deliveries
                    )

                    st.success("Optimization completed successfully.")

                    st.markdown(ai_result)

                except Exception as e:

                    st.error(f"AI Error: {e}")

    else:

        st.info("Press 'Start Optimization' to generate an AI operation plan.")

    st.divider()

    st.subheader("Operational Summary")

    st.write(f"Drivers: **{driver_count}**")
    st.write(f"Vehicles: **{vehicle_count}**")
    st.write(f"Deliveries: **{delivery_count}**")
    st.write(f"Total Weight: **{total_weight} kg**")

    st.write("---")

    st.metric("Fleet Utilization", "-- %")
    st.metric("Estimated Fuel", "-- L")
    st.metric("Estimated Cost", "-- ₺")
    st.metric("Estimated CO₂", "-- kg")

st.divider()

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.caption(
    "RotaNet | AI-Powered Logistics Operations Decision Support Platform"
)
