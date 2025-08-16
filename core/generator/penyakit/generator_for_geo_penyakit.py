from connection.conn import DataLoader

import pandas as pd

import streamlit as st

@st.cache_data
def generate_geo_data_penyakit(selected_penyakit:str, selected_tahun:int):
    data = DataLoader()
    df = data.get_penderita_penyakit_hiper_diabet()
    if selected_penyakit:
        df = df[df['jenis_penderita'].isin(selected_penyakit)]
    if selected_tahun:
        df = df[df['tahun'] == selected_tahun]
    df_agg = df.groupby(["kode_kabupaten_kota","tahun",'nama_kabupaten_kota', 'jenis_penderita'])['jumlah_penderita'].sum().reset_index(name='Total jumlah penderita').sort_values(by='Total jumlah penderita', ascending=False)
            
    return df_agg