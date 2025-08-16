# features/kpi_metrics/sales.py

import pandas as pd

def calculate_total_sales(df: pd.DataFrame) -> float:
    """
    Menghitung total nilai Sales dari DataFrame.

    Args:
        df (pd.DataFrame): DataFrame yang berisi kolom 'Sales'.

    Returns:
        float: Total nilai sales.
    """
    if 'Sales' not in df.columns:
        raise ValueError("Kolom 'Sales' tidak ditemukan dalam DataFrame.")
    
    return df['Sales'].sum()
