
from connection.conn import DataLoader


import streamlit as st

@st.cache_data
def generate_peserta_bpjs_summary():
    data = DataLoader()
    df = data.get_peserta_bpjs()

    df = (
        df
        .groupby(['tahun', 'bps_nama_kabupaten_kota'])['jumlah_ warga_terdaftar_bpjs']
        .sum()
        .reset_index(name='jumlah_ warga_terdaftar_bpjs')
        .sort_values(by='tahun')
    )
    return df