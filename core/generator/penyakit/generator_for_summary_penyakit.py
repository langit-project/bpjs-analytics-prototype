
from connection.conn import DataLoader


import streamlit as st

@st.cache_data
def generate_penyakit_summary():
    data = DataLoader()
    df = data.get_penderita_penyakit_hiper_diabet()

    df = (
            df.groupby(['tahun','nama_kabupaten_kota', 'jenis_penderita'])['jumlah_penderita']
            .sum()
            .reset_index(name='jumlah_penderita')
            .sort_values(by=["nama_kabupaten_kota",'tahun'])
        )
    return df