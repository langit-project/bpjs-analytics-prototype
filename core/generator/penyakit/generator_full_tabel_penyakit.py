from connection.conn import DataLoader


import streamlit as st

@st.cache_data
def generate_full_penyakit():
    data = DataLoader()
    df = data.get_penderita_penyakit_hiper_diabet()
    return df

