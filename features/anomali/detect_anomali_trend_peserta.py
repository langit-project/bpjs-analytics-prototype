def detect_significant_change_trend(df, group_col="bps_nama_kabupaten_kota",
                                    value_col="jumlah_ warga_terdaftar_bpjs",
                                    time_col="tahun", pct_threshold=30, abs_threshold=200):
    """
    Deteksi kenaikan/penurunan signifikan per kab/kota
    """
    alerts = []

    for kab, df_kab in df.groupby(group_col):
        df_kab_sorted = df_kab.sort_values(by=time_col).reset_index(drop=True)
        
        for i in range(1, len(df_kab_sorted)):
            prev_value = df_kab_sorted.loc[i-1, value_col]
            curr_value = df_kab_sorted.loc[i, value_col]
            date = df_kab_sorted.loc[i, time_col]

            if prev_value == 0:
                continue  # Hindari divide by zero

            change = curr_value - prev_value
            pct_change = (change / prev_value) * 100

            if abs(change) >= abs_threshold and abs(pct_change) >= pct_threshold:
                if change > 0:
                    alerts.append(f"📈 {kab}: Peningkatan signifikan {pct_change:.1f}% dari {prev_value} menjadi {curr_value} pada {date}")
                else:
                    alerts.append(f"📉 {kab}: Penurunan signifikan {abs(pct_change):.1f}% dari {prev_value} menjadi {curr_value} pada {date}")
    
    return alerts
