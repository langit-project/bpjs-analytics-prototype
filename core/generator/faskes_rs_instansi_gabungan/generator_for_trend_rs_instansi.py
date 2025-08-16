from connection.conn import DataLoader

import streamlit as st

@st.cache_data
def generate_faskes_rs_instansi_for_trend(selected_kota:str,selected_kepemilikan:str):
    data = DataLoader()
    df = data.get_faskes_jenisrs_intansi()
    if selected_kota:
        df = df[df['nama_kabupaten_kota'] == selected_kota]
    if selected_kepemilikan:
        df = df[df['kepemilikan'] == selected_kepemilikan]
    df = (
                df.groupby(['nama_kabupaten_kota', 'kepemilikan', 'jenis_rumah_sakit', 'tahun'])['jumlah_faskes']
                .sum()
                .reset_index(name='jumlah_faskes')
                .sort_values(by='tahun')
            )
    return df