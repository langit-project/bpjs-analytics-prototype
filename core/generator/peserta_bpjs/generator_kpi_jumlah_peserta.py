import pandas as pd

import streamlit as st

@st.cache_data
def filter_peserta(df: pd.DataFrame, tahun: int, list_kabkota: list):
    """
    Filter DataFrame berdasarkan tahun dan daftar kabupaten/kota.
    Mengembalikan DataFrame hasil filter dan total peserta.

    Parameters
    ----------
    df : pd.DataFrame
        Data BPJS
    tahun : int
        Tahun yang ingin difilter
    list_kabkota : list
        Daftar kabupaten/kota

    Returns
    -------
    tuple
        (df_filtered, total_peserta)
    """
    df["tahun"] = df["tahun"].astype(int)
    df_filtered = df[
        (df["tahun"] == tahun) &
        (df["bps_nama_kabupaten_kota"].isin(list_kabkota))
    ]
    total_peserta = df_filtered["jumlah_ warga_terdaftar_bpjs"].sum()

    return total_peserta
