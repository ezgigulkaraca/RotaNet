import streamlit as st
import pandas as pd 
from backend.ai_service import get_route_insights

# -------------------------------
# Page Configuration
# -------------------------------

st.set_page_config(
    page_title="RotaNet",
    page_icon="🚛",
    layout="wide"
)

# -------------------------------
# Header
# -------------------------------

st.title("RotaNet")
st.caption("AI-Powered Logistics Operations Decision Support Platform")

st.divider()

# -------------------------------
# Sidebar
# -------------------------------

with st.sidebar:

    st.header("Operations Panel")

    st.subheader("AI Configuration")

    api_key = st.text_input(
        "Gemini API Key",
        type="password"
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

# -------------------------------
# Dataset Loading
# -------------------------------

drivers = None
vehicles = None
deliveries = None

try:

    if drivers_file is not None:

        if drivers_file.name.endswith(".csv"):
            drivers = pd.read_csv(drivers_file)
        else:
            drivers = pd.read_excel(drivers_file)

    if vehicles_file is not None:

        if vehicles_file.name.endswith(".csv"):
            vehicles = pd.read_csv(vehicles_file)
        else:
            vehicles = pd.read_excel(vehicles_file)

    if deliveries_file is not None:

        if deliveries_file.name.endswith(".csv"):
            deliveries = pd.read_csv(deliveries_file)
        else:
            deliveries = pd.read_excel(deliveries_file)

except Exception as e:

    st.error(e)

# -------------------------------
# KPI
# -------------------------------

driver_count = len(drivers) if drivers is not None else 0
vehicle_count = len(vehicles) if vehicles is not None else 0
delivery_count = len(deliveries) if deliveries is not None else 0

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Drivers", driver_count)

with col2:
    st.metric("Vehicles", vehicle_count)

with col3:
    st.metric("Deliveries", delivery_count)

with col4:

    if deliveries is not None and "Weight" in deliveries.columns:
        total_weight = deliveries["Weight"].sum()
    else:
        total_weight = 0

    st.metric("Total Weight (kg)", total_weight)

st.divider()

# -------------------------------
# Layout
# -------------------------------

left, right = st.columns([2,1])

# -------------------------------
# Left Side
# -------------------------------

with left:

    st.subheader("Optimization Results")

    if deliveries is not None:

        st.dataframe(deliveries)

    else:

        st.info("Upload delivery dataset.")

    st.divider()

    st.subheader("Interactive Map")

    st.info("Route map will be displayed here.")

# -------------------------------
# Right Side
# -------------------------------

with right:

    st.subheader("AI Insights")

    if optimize_button:

        if api_key == "":

            st.warning("Please enter Gemini API Key.")

        elif deliveries is None:

            st.warning("Please upload datasets.")

        else:

            st.success("Optimization started.")
            metrics = {
    "total_distance": 1250
}

route_summary = """
İstanbul → Bursa → İzmir → Ankara
"""

try:
    ai_result = get_route_insights(metrics, route_summary)
    st.markdown(ai_result)

except Exception as e:
    st.error(e)


try:
    ai_result = get_route_insights(metrics, route_summary)
    st.markdown(ai_result)

except Exception as e:
    st.error(e)

    else:

        st.info("Press 'Start Optimization'.")

    st.divider()

    st.subheader("Operational Summary")

    st.write(f"Drivers : **{driver_count}**")

    st.write(f"Vehicles : **{vehicle_count}**")

    st.write(f"Deliveries : **{delivery_count}**")

    st.write("Fleet Utilization : -- %")

    st.write("Estimated Cost : --")

    st.write("Estimated Fuel : --")

    st.write("Estimated CO₂ : --")
