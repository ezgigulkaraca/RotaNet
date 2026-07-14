import streamlit as st


def calculate_estimated_cost(distance: float) -> float:
    """
    Estimate transportation cost based on total distance.

    Parameters
    ----------
    distance : float
        Total route distance in kilometers.

    Returns
    -------
    float
        Estimated transportation cost.
    """
    COST_PER_KM = 12.50

    return distance * COST_PER_KM


def calculate_co2_emission(distance: float) -> float:
    """
    Estimate CO₂ emissions based on travelled distance.

    Parameters
    ----------
    distance : float
        Total route distance in kilometers.

    Returns
    -------
    float
        Estimated CO₂ emissions in kilograms.
    """
    CO2_PER_KM = 0.27

    return distance * CO2_PER_KM


def show_dashboard(total_distance: float, route: list[int]) -> None:
    """
    Display optimization summary dashboard.

    Parameters
    ----------
    total_distance : float
        Total optimized route distance.

    route : list[int]
        Optimized route.
    """

    estimated_cost = calculate_estimated_cost(total_distance)
    co2_emission = calculate_co2_emission(total_distance)
    total_stops = max(len(route) - 2, 0)

    st.subheader("Optimization Summary")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            label="Total Distance",
            value=f"{total_distance:.2f} km"
        )

    with col2:
        st.metric(
            label="Total Stops",
            value=total_stops
        )

    with col3:
        st.metric(
            label="Estimated Cost",
            value=f"₺{estimated_cost:.2f}"
        )

    with col4:
        st.metric(
            label="CO₂ Emission",
            value=f"{co2_emission:.2f} kg"
        )
