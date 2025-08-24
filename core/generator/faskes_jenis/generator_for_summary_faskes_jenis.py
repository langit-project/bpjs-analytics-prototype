from connection.conn import DataLoader
import streamlit as st

@st.cache_data

def generate_faskes_jenis_summary():
    data = DataLoader()
    df = data.get_faskes_jenis()
    df = (
                df.groupby(['nama_kabupaten_kota','jenis_faskes', 'tahun'])['jumlah_faskes']
                .sum()
                .reset_index(name='jumlah_faskes')
                .sort_values(by='jumlah_faskes', ascending=False)
            )
    df['nama_kabupaten_kota'] = df['nama_kabupaten_kota'].astype(str)
    df['jenis_faskes'] = df['jenis_faskes'].astype(str)
    df = df.sort_values(['nama_kabupaten_kota', 'jenis_faskes', 'tahun'])
    return df