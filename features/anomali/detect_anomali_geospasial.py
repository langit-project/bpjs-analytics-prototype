import streamlit as st

def detect_spatial_anomaly(df, group_col, jumlah_col, label, z_threshold=2.5):
    """
    Deteksi anomali berdasarkan Z-score.

    Parameters
    ----------
    df : DataFrame
        Data yang sudah difilter sesuai konteks (tahun, jenis faskes, dll).
    group_col : str
        Nama kolom kategori (misalnya: 'bps_nama_kabupaten_kota' atau 'jenis_faskes').
    jumlah_col : str
        Nama kolom jumlah (misalnya: 'jumlah_faskes' atau 'jumlah_ warga_terdaftar_bpjs').
    label : str, optional
        Label untuk ditampilkan di judul pesan anomali.
    z_threshold : float, optional
        Batas Z-score untuk menentukan anomali.
    """
    mean_val = df[jumlah_col].mean()
    std_val = df[jumlah_col].std()
    df["z_score"] = (df[jumlah_col] - mean_val) / std_val
    df["is_anomaly"] = abs(df["z_score"]) > z_threshold

    anomalies = df[df["is_anomaly"]]

    if not anomalies.empty:
        st.markdown(f":orange-badge[⚠️ Anomali terdeteksi pada {label} berikut:]")
        for _, row in anomalies.iterrows():
            if row["z_score"] > 0:
                st.markdown(f":green-badge[{row[group_col]} → {jumlah_col} jauh di atas rata-rata]")
            else:
                st.markdown(f":red-badge[{row[group_col]} → {jumlah_col} jauh di bawah rata-rata]")
    else:
        st.badge(f"✅ Tidak ada anomali terdeteksi pada {label}.", color="green")
