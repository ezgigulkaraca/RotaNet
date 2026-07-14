from typing import List

import pandas as pd
import plotly.express as px
import streamlit as st


def show_charts(df: pd.DataFrame, route: List[int]) -> None:
    """
    Display operational charts.

    Parameters
    ----------
    df : pd.DataFrame
        Delivery dataset.

    route : List[int]
        Optimized route.
    """

    st.subheader("Operational Analytics")

    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:

        demand_chart = px.bar(
            df,
            x=df.index.astype(str),
            y="demand",
            title="Demand by Delivery Point",
            labels={
                "x": "Delivery Point",
                "demand": "Demand"
            }
        )

        demand_chart.update_layout(
            xaxis_title="Delivery Point",
            yaxis_title="Demand",
            margin=dict(l=20, r=20, t=50, b=20)
        )

        st.plotly_chart(
            demand_chart,
            use_container_width=True
        )

    with chart_col2:

        route_chart = px.line(
            x=list(range(len(route))),
            y=route,
            markers=True,
            title="Optimized Route Sequence",
            labels={
                "x": "Visit Order",
                "y": "Location ID"
            }
        )

        route_chart.update_layout(
            margin=dict(l=20, r=20, t=50, b=20)
        )

        st.plotly_chart(
            route_chart,
            use_container_width=True
        )

    st.divider()

    summary_chart = px.pie(
        df,
        names=df.index.astype(str),
        values="demand",
        title="Demand Distribution"
    )

    st.plotly_chart(
        summary_chart,
        use_container_width=True
    )
