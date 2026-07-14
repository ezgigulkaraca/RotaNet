from typing import List

import folium
import pandas as pd
import streamlit as st
from streamlit_folium import st_folium


def show_route_map(df: pd.DataFrame, route: List[int]) -> None:
    """
    Display the optimized route on an interactive map.

    Parameters
    ----------
    df : pd.DataFrame
        Delivery dataset.

    route : List[int]
        Optimized route returned by OR-Tools.
    """

    if df.empty or len(route) < 2:
        st.warning("No route available for visualization.")
        return

    center_lat = df["latitude"].mean()
    center_lon = df["longitude"].mean()

    route_map = folium.Map(
        location=[center_lat, center_lon],
        zoom_start=11
    )

    coordinates = []

    for order, node in enumerate(route):

        latitude = df.iloc[node]["latitude"]
        longitude = df.iloc[node]["longitude"]

        coordinates.append((latitude, longitude))

        if order == 0:

            folium.Marker(
                location=[latitude, longitude],
                popup="Depot",
                tooltip="Depot",
                icon=folium.Icon(color="green")
            ).add_to(route_map)

        elif order == len(route) - 1:

            folium.Marker(
                location=[latitude, longitude],
                popup="Return to Depot",
                tooltip="Return",
                icon=folium.Icon(color="red")
            ).add_to(route_map)

        else:

            folium.Marker(
                location=[latitude, longitude],
                popup=f"Stop {order}",
                tooltip=f"Stop {order}",
                icon=folium.Icon(color="blue")
            ).add_to(route_map)

    folium.PolyLine(
        coordinates,
        weight=4
    ).add_to(route_map)

    st.subheader("Route Map")

    st_folium(
        route_map,
        width=None,
        height=550
    )
