
# def is_significant_change(prev, curr, threshold_pct=50, min_prev_val=10, min_curr_val=10):
#     if prev == 0:
#         return False  # Hindari pembagian dengan nol
#     change_pct = abs((curr - prev) / prev) * 100

#     return (
#         change_pct >= threshold_pct
#         and (prev >= min_prev_val or curr >= min_curr_val)
#     )



def detect_significant_change(df, value_col="New Customers", time_col="YearMonth", 
                              pct_threshold=50, abs_threshold=20):
    df_sorted = df.sort_values(by=time_col).reset_index(drop=True)
    alerts = []

    for i in range(1, len(df_sorted)):
        prev_value = df_sorted.loc[i-1, value_col]
        curr_value = df_sorted.loc[i, value_col]
        date = df_sorted.loc[i, time_col]

        if prev_value == 0:
            continue  # Hindari divide by zero

        change = curr_value - prev_value
        pct_change = (change / prev_value) * 100

        if abs(change) >= abs_threshold and abs(pct_change) >= pct_threshold:
            if change > 0:
                alerts.append(f"📈 Terjadi peningkatan signifikan sebesar {pct_change:.1f}% dari {prev_value} menjadi {curr_value} pada {date}")
            else:
                alerts.append(f"📉 Terjadi penurunan signifikan sebesar {abs(pct_change):.1f}% dari {prev_value} menjadi {curr_value} pada {date}")
    
    return alerts
