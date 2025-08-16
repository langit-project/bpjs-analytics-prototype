from connection.conn import DataLoader
import streamlit as st

@st.cache_data
def generate_bar_faskes_jenis(selected_kota:str,tahun:int):
    data = DataLoader()
    df = data.get_faskes_jenis()
    if selected_kota:
        df = df[df['nama_kabupaten_kota']==selected_kota]
    if tahun:
        df = df[df['tahun'] == tahun]
    df = (
                df.groupby(['nama_kabupaten_kota','jenis_faskes', 'tahun'])['jumlah_faskes']
                .sum()
                .reset_index(name='jumlah_faskes')
                .sort_values(by='jumlah_faskes', ascending=False)
            )
    return df