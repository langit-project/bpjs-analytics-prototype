from core.generator.faskes_jenis.generator_for_summary_faskes_jenis import generate_faskes_jenis_summary
from core.generator.penyakit.generator_table_penyakit import generate_kabkot_penyakit_for_table
from core.generator.peserta_bpjs.generator_full_peserta_bpjs import generate_full_peserta_bpjs
import pandas as pd




import streamlit as st

@st.cache_data
def filter_tahun():
    all_tahun = pd.concat([
    generate_full_peserta_bpjs()["tahun"], 
    generate_faskes_jenis_summary()["tahun"],
    generate_kabkot_penyakit_for_table()["tahun"]
], ignore_index=True).dropna().unique()
    
    tahun_list = sorted(all_tahun)
    return tahun_list

def filter_kabkot():
    all_kabkot = pd.concat([
    generate_full_peserta_bpjs()["bps_nama_kabupaten_kota"], 
    generate_faskes_jenis_summary()["nama_kabupaten_kota"],
    generate_kabkot_penyakit_for_table()["nama_kabupaten_kota"]
], ignore_index=True).dropna().unique()
    
    kabkot_list = sorted(all_kabkot)
    return kabkot_list

def filter_jenis_faskes():
    all_jenis_faskes = generate_faskes_jenis_summary()["jenis_faskes"].dropna().unique().tolist()
    
    jenis_faskes_list = sorted(all_jenis_faskes)
    return jenis_faskes_list

def filter_penderita():
    all_penderita = generate_kabkot_penyakit_for_table()["jenis_penderita"].dropna().unique().tolist()
    
    jenis_penderita_list = sorted(all_penderita)
    return jenis_penderita_list

