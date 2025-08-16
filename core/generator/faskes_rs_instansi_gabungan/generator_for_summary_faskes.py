from connection.conn import DataLoader

import streamlit as st

@st.cache_data
def generate_kepemilikan_faskes_summary():
    data = DataLoader()
    df = data.get_faskes_jenisrs_intansi()
    df = (
                df.groupby(['nama_kabupaten_kota', 'kepemilikan', 'jenis_rumah_sakit', 'tahun'])['jumlah_faskes']
                .sum()
                .reset_index(name='jumlah_faskes')
                .sort_values(by=['tahun','jumlah_faskes'], ascending=False)
            )
    return df
