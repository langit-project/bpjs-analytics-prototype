# core/chart/trend_penyakit_chart.py

import plotly.express as px
import pandas as pd
import streamlit as st

@st.cache_data
def plot_trend_peserta(df_agg: pd.DataFrame, selected_kota: list[str]):
    title = (
        f"Pertumbuhan Peserta BPJS - {' & '.join(selected_kota)}"
        if selected_kota else "Pertumbuhan Peserta - Semua Kabupaten/Kota"
    )

    fig = px.line(
        df_agg,
        x="tahun",
        y="jumlah_ warga_terdaftar_bpjs",
        color="bps_nama_kabupaten_kota",
        markers=True,
        color_discrete_sequence=px.colors.sequential.Blugrn,
        title=title
    )
    fig.update_layout(
        xaxis_title="Tahun",
        yaxis_title="Jumlah Pserta",
        legend_title="Kabupaten/Kota",
        template="plotly_dark",
    )

    fig.update_xaxes(type='category')

    
    return fig
