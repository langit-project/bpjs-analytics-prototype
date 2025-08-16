from connection.conn import DataLoader

import streamlit as st

@st.cache_data
def generate_geo_faskes_jenis(selected_jenis_faskes:str, selected_tahun:int):
    data = DataLoader()
    df = data.get_faskes_jenis()
    if selected_jenis_faskes:
        df = df[df['jenis_faskes']==selected_jenis_faskes]
    if selected_tahun:
        df = df[df['tahun'] == selected_tahun]
    df_agg = df.groupby(["kode_kabupaten_kota","tahun",'nama_kabupaten_kota', 'jenis_faskes'])['jumlah_faskes'].sum().reset_index(name='jumlah_faskes').sort_values(by='jumlah_faskes', ascending=False)
            
    return df_agg