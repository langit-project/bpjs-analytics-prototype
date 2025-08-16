from connection.conn import DataLoader

import streamlit as st

@st.cache_data
def generate_faskes_rs_instansi(selected_kota:str,tahun:int):
    data = DataLoader()
    df = data.get_faskes_jenisrs_intansi()
    if selected_kota:
        df = df[df['nama_kabupaten_kota'].isin(selected_kota)]
    if tahun:
        df = df[df['tahun'] == tahun]
    df = (
                df.groupby(['nama_kabupaten_kota', 'kepemilikan', 'jenis_rumah_sakit', 'tahun'])['jumlah_faskes']
                .sum()
                .reset_index(name='jumlah_faskes')
                .sort_values(by='jumlah_faskes', ascending=False)
            )
    return df