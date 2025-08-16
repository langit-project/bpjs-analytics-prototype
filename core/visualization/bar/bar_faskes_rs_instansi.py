import pandas as pd
import plotly.express as px

import streamlit as st

@st.cache_data
def plot_jumlah_faskes_rs_instansi(df: pd.DataFrame, selected_kota:str, tahun:int):
    # Urutkan kabupaten berdasarkan total jumlah penderita
    fig = px.bar(
            df, x='kepemilikan', y='jumlah_faskes',
            color='jenis_rumah_sakit', barmode='group',
            title='Jumlah Faskes kepemilikan berdasarkan jenis Rumah Sakit',
            color_discrete_sequence=px.colors.sequential.Tealgrn_r,
        )
    fig.update_layout(
            xaxis_title='Kepemilikan',
            yaxis_title='Faskes',
        )
    return fig