# core/processor/penyakit_processor.py
from connection.conn import DataLoader

import pandas as pd

import streamlit as st

@st.cache_data
def generate_trend_peserta(selected_kota: list[str]) -> pd.DataFrame:
    data = DataLoader()
    df = data.get_peserta_bpjs()

    if selected_kota:
        df_filtered = df[df['bps_nama_kabupaten_kota'].isin(selected_kota)]
    else:
        df_filtered = df.copy()

    df_agg = (
        df_filtered
        .groupby(['tahun', 'bps_nama_kabupaten_kota'])['jumlah_ warga_terdaftar_bpjs']
        .sum()
        .reset_index()
        .sort_values(by='tahun')
    )


    return df_agg
