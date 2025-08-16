# core/processor/penyakit_processor.py
from connection.conn import DataLoader

import pandas as pd

import streamlit as st

@st.cache_data
def generate_trend_penyakit(selected_kotas: str) -> pd.DataFrame:
    data = DataLoader()
    df = data.get_penderita_penyakit_hiper_diabet()
    if selected_kotas:
        df_filtered = df[df['nama_kabupaten_kota']==selected_kotas]
    else:
        df_filtered = df.copy()

    df_agg = (
        df_filtered
        .groupby(['tahun','nama_kabupaten_kota', 'jenis_penderita'])['jumlah_penderita']
        .sum()
        .reset_index()
        .sort_values(by='tahun')
    )
    return df_agg
