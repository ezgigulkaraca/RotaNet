import streamlit as st


def show_dashboard(metrics: dict) -> None:
    """
    Display the optimization summary dashboard.

    Parameters
    ----------
    metrics : dict
        Dictionary containing optimization metrics.
    """

    st.subheader("Optimization Summary")

    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    with col1:
        st.metric(
            label="Total Distance",
            value=f"{metrics['total_distance']:.2f} km"
        )

    with col2:
        st.metric(
            label="Total Stops",
            value=metrics["total_stops"]
        )

    with col3:
        st.metric(
            label="Estimated Cost",
            value=f"₺{metrics['estimated_cost']:.2f}"
        )

    with col4:
        st.metric(
            label="CO₂ Emission",
            value=f"{metrics['co2_emission']:.2f} kg"
        )

    st.divider()

    st.subheader("Operational Statistics")

    stat1, stat2 = st.columns(2)

    with stat1:
        st.metric(
            label="Average Distance per Stop",
            value=f"{metrics['average_distance']:.2f} km"
        )

    with stat2:
        st.metric(
            label="Optimization Status",
            value="Completed"
        )
