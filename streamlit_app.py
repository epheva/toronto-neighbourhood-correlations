import streamlit as st
import plotly.io as pio

st.set_page_config(
    page_title="Toronto Neighbourhood Correlations",
    layout="wide"
)

fig = pio.read_json("correlation_matrix.json")

fig.update_layout(
    height=1500,
    autosize=True
)

with st.container(width=1500):

    st.plotly_chart(
        fig,
        theme=None,
        width="stretch",
        height=1500,
        config={
            "responsive": True,
            "displaylogo": False
        }
    )