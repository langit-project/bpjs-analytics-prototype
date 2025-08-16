from connection.conn import DataLoader

import pandas as pd



import streamlit as st

@st.cache_data
def generate_geo_data_peserta(selected_tahun:int):
    data = DataLoader()
    df = data.get_peserta_bpjs()
    if selected_tahun:
        df = df[df['tahun']==selected_tahun]
    else:
        df = df.copy()

    df_agg = df.groupby(["bps_kode_kabupaten_kota","tahun",'bps_nama_kabupaten_kota'])['jumlah_ warga_terdaftar_bpjs'].sum().reset_index(name='jumlah_ warga_terdaftar_bpjs').sort_values(by='jumlah_ warga_terdaftar_bpjs', ascending=False)
            
    return df_agg

# def generate_trend_penyakit(selected_kotas: list[str]) -> pd.DataFrame:
#     data = DataLoader()
#     df = data.get_penderita_penyakit_hiper_diabet()
#     if selected_kotas:
#         df_filtered = df[df['nama_kabupaten_kota'].isin(selected_kotas)]
#     else:
#         df_filtered = df.copy()

#     df_agg = (
#         df_filtered
#         .groupby(['tahun', 'jenis_penderita'])['jumlah_penderita']
#         .sum()
#         .reset_index()
#         .sort_values(by='tahun')
#     )
#     return df_agg