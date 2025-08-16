def detect_significant_change_jenis_faskes(df, group_col="jenis_faskes",
                                     value_col="jumlah_faskes",
                                     time_col="tahun",
                                     pct_threshold=50, abs_threshold=5):
    """
    Deteksi kenaikan/penurunan signifikan jumlah faskes per jenis faskes di satu kab/kota.
    """
    alerts = []

    for jenis, df_jenis in df.groupby(group_col):
        df_jenis_sorted = df_jenis.sort_values(by=time_col).reset_index(drop=True)

        for i in range(1, len(df_jenis_sorted)):
            prev_value = df_jenis_sorted.loc[i-1, value_col]
            curr_value = df_jenis_sorted.loc[i, value_col]
            date = df_jenis_sorted.loc[i, time_col]

            if prev_value == 0:
                continue  # Hindari divide by zero

            change = curr_value - prev_value
            pct_change = (change / prev_value) * 100

            if abs(change) >= abs_threshold and abs(pct_change) >= pct_threshold:
                if change > 0:
                    alerts.append(f"📈 {jenis}: peningkatan signifikan {pct_change:.1f}% dari {prev_value} menjadi {curr_value} pada {date}")
                else:
                    alerts.append(f"📉 {jenis}: penurunan signifikan {abs(pct_change):.1f}% dari {prev_value} menjadi {curr_value} pada {date}")

    return alerts
