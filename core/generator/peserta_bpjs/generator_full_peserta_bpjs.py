from connection.conn import DataLoader


import streamlit as st

@st.cache_data
def generate_full_peserta_bpjs():
    data = DataLoader()
    df = data.get_peserta_bpjs()
    return df

