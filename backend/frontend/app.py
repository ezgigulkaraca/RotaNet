import streamlit as st

from backend.loader import load_dataset
from backend.distance import create_distance_matrix
from backend.optimizer import optimize_route


st.set_page_config(
    page_title="RotaNet",
    page_icon="🚚",
    layout="wide"
)

st.title("🚚 RotaNet")
st.subheader("AI-Powered Logistics Route Optimization Platform")

st.markdown("---")

uploaded_file = st.file_uploader(
    "Upload Delivery Dataset",
    type=["csv", "xlsx"]
)

vehicle_count = st.number_input(
    "Number of Vehicles",
    min_value=1,
    value=1,
    step=1
)

if uploaded_file is not None:

    try:

        df = load_dataset(uploaded_file)

        st.success("Dataset loaded successfully!")

        st.write("### Dataset Preview")
        st.dataframe(df)

        if st.button("Optimize Route"):

            with st.spinner("Optimizing routes..."):

                distance_matrix = create_distance_matrix(df)

                route, total_distance = optimize_route(distance_matrix)

            st.success("Optimization completed!")

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Total Distance",
                    f"{total_distance:.2f} km"
                )

            with col2:
                st.metric(
                    "Stops",
                    len(route) - 2
                )

            st.write("### Optimized Route")

            st.write(" ➜ ".join(map(str, route)))

    except Exception as e:

        st.error(str(e))
