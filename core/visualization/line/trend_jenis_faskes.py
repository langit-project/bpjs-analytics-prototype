
import plotly.express as px
import pandas as pd

import streamlit as st

@st.cache_data
def plot_trend_jenis_faskes(df: pd.DataFrame, selected_kota:str):
    title = (
        f"Pertumbuhan Jumlah Faskes {selected_kota}"
    )

    fig = px.line(
    df,
    x="tahun",
    y="jumlah_faskes",
    color="jenis_faskes",
    markers=True,
    color_discrete_sequence=px.colors.sequential.Tealgrn,
    title=title
)

    
    return fig