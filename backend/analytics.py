from typing import Any


COST_PER_KM = 12.50
CO2_PER_KM = 0.27


def calculate_metrics(
    total_distance: float,
    route: list[int]
) -> dict[str, Any]:
    """
    Calculate business metrics for the optimization dashboard.

    Parameters
    ----------
    total_distance : float
        Total optimized route distance in kilometers.

    route : list[int]
        Optimized route.

    Returns
    -------
    dict[str, Any]
        Dictionary containing calculated business metrics.
    """

    total_stops = max(len(route) - 2, 0)

    estimated_cost = total_distance * COST_PER_KM

    co2_emission = total_distance * CO2_PER_KM

    average_distance_per_stop = (
        total_distance / total_stops
        if total_stops > 0
        else 0.0
    )

    return {
        "total_distance": round(total_distance, 2),
        "total_stops": total_stops,
        "estimated_cost": round(estimated_cost, 2),
        "co2_emission": round(co2_emission, 2),
        "average_distance": round(average_distance_per_stop, 2),
    }
