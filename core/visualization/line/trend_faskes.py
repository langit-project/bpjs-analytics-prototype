
import plotly.express as px
import pandas as pd
color_sequence = [
    "#006d77",  # teal gelap
    "#83c5be",  # teal muda
    "#0077b6",  # biru laut
    "#00b4d8",  # biru cerah
    "#48cae4",  # biru muda
    "#2a9d8f",  # hijau tosca
    "#38b000",  # hijau terang
    "#70e000",  # hijau muda
    "#00a896",  # teal sedang
    "#028090"   # teal kebiruan gelap

]

import streamlit as st

@st.cache_data
def plot_trend_faskes_instansi(df_agg: pd.DataFrame, selected_kota:str,selected_kepemilikan:str):
    title = (
        f"Pertumbuhan Jumlah Faskes {selected_kota} berdasarkan kepemilikan {selected_kepemilikan}"
    )

    fig = px.line(
        df_agg,
        x="tahun",
        y="jumlah_faskes",
        color="jenis_rumah_sakit",
        markers=True,
        color_discrete_sequence=color_sequence,
        title=title
    )
    fig.update_layout(
        xaxis_title="Tahun",
        yaxis_title="Jumlah Faskes",
        legend_title="Jenis Rumah Sakit",
        template="plotly_dark",
    )

    fig.update_xaxes(type='category')
    fig.update_yaxes(dtick=1)

    
    return fig