from connection.conn import DataLoader


import streamlit as st

@st.cache_data
def generate_kabkot_penyakit_for_table():
    data = DataLoader()
    df = data.get_penderita_penyakit_hiper_diabet()
    df = (
                df.groupby(["tahun",'nama_kabupaten_kota', 'jenis_penderita'])['jumlah_penderita']
                .sum()
                .reset_index(name='Total jumlah penderita')
                .sort_values(by='Total jumlah penderita', ascending=False)
            )
    return df

