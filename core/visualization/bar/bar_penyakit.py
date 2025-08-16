import pandas as pd
import plotly.express as px
import streamlit as st

@st.cache_data

def plot_jumlah_penderita_per_kabupaten(df: pd.DataFrame):
    # Urutkan kabupaten berdasarkan total jumlah penderita
    fig = px.bar(
            df, x='nama_kabupaten_kota', y='Total jumlah penderita',
            color='jenis_penderita', barmode='group',
            title='Jumlah Penderita Diabetes dan Hipertensi setiap Kab/Kota',
            color_discrete_sequence=px.colors.sequential.Tealgrn_r,
        )
    fig.update_layout(
            xaxis_title='Kota/Kabupaten',
            yaxis_title='Jumlah Penderita',
            template='ggplot2'
        )
    return fig