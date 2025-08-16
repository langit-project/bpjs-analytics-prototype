import pandas as pd
import streamlit as st


class DataLoader:
    def __init__(self):
        self.path_faskes_jenisrs_instansi = "data/db/data_faskes_rumah_sakit_gabungan.csv"
        self.path_penderita_penyakit = "data/db/data_penderita_diabetes_hipertensi.csv"
        self.path_faskes_jenis = "data/db/jumlah faskes berdasarkan jenis.csv"
        self.path_peserta_bpjs = "data/db/jumlah warga terdaftar peserta bpjs kesehatan.csv"
    

    def get_faskes_jenisrs_intansi(self):
        df = pd.read_csv(self.path_faskes_jenisrs_instansi)
        return df
    def get_penderita_penyakit_hiper_diabet(self):
        df = pd.read_csv(self.path_penderita_penyakit)
        return df
    def get_faskes_jenis(self):
        df = pd.read_csv(self.path_faskes_jenis)
        return df
    def get_peserta_bpjs(self):
        df = pd.read_csv(self.path_peserta_bpjs)
        df['tahun'] = df['tahun'].astype(int)
        return df