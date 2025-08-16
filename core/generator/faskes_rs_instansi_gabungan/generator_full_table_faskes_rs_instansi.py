from connection.conn import DataLoader

import streamlit as st

@st.cache_data
def generate_full_jenisrs_instansi():
    data = DataLoader()
    df = data.get_faskes_jenisrs_intansi()
    return df

