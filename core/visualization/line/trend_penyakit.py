# core/chart/trend_penyakit_chart.py

import plotly.express as px
import pandas as pd
import streamlit as st

@st.cache_data
def plot_trend_penyakit(df_agg: pd.DataFrame, selected_kotas: str):
    title = (
        f"Trend Penyakit {selected_kotas} "
    )

    fig = px.line(
        df_agg,
        x="tahun",
        y="jumlah_penderita",
        color="jenis_penderita",
        markers=True,
        color_discrete_map={
            "Hipertensi": "#1E90FF",  # Dodger Blue
            "Diabetes": "#32CD32"     # Lime Green
        },
        title=title
    )
    fig.update_layout(
        xaxis_title="Tahun",
        yaxis_title="Jumlah Penderita",
        legend_title="Jenis Penyakit",
        template="plotly_dark",
    )
    
    return fig
