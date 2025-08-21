
import pandas as pd
import io


def generate_summary_trend_sales_per_month_from_df(df: pd.DataFrame) -> str:
    df['YearMonth'] = pd.to_datetime(df['YearMonth'])
    df['Year'] = df['YearMonth'].dt.year

    total_per_year = df.groupby('Year')['Sales'].sum()
    growth = total_per_year.pct_change().round(2) * 100
    max_row = df.loc[df['Sales'].idxmax()]
    avg_sales = df['Sales'].mean()

    summary = f"""
Berikut adalah ringkasan data penjualan bulanan dari tahun {df['Year'].min()} sampai {df['Year'].max()}:

📊 Total Penjualan per Tahun:
""" + "".join([f"- {year}: Rp {value:,.0f}\n" for year, value in total_per_year.items()]) + \
f"""
📈 Pertumbuhan Tahunan:
""" + "".join([f"- {year}: {value:.2f}%\n" for year, value in growth.dropna().items()]) + \
f"""
🌟 Bulan Tertinggi: {max_row['YearMonth'].strftime('%Y-%m')} dengan penjualan Rp {max_row['Sales']:,.2f}
📉 Rata-rata Penjualan Bulanan: Rp {avg_sales:,.2f}
"""
    return summary.strip()


def generate_summary_new_customer(df: pd.DataFrame) -> str:
    # Total keseluruhan & rata-rata bulanan
    total_new_cust = df['New Customers'].sum()
    avg_new_cust = df['New Customers'].mean()

    # Peningkatan signifikan
    df['pct_change'] = df['New Customers'].pct_change() * 100
    max_increase = df.loc[df['pct_change'].idxmax()]
    max_decrease = df.loc[df['pct_change'].idxmin()]

    # Bulan dengan nilai tertinggi & terendah
    max_value = df.loc[df['New Customers'].idxmax()]
    min_value = df.loc[df['New Customers'].idxmin()]

    summary = f"""
📊 **Ringkasan Tren Pelanggan Baru**

✅ Selama periode analisis, total pelanggan baru yang diperoleh adalah **{total_new_cust:,}**, 
dengan rata-rata sekitar **{avg_new_cust:.1f} pelanggan per bulan**.

📈 Bulan dengan peningkatan tertinggi dibanding bulan sebelumnya terjadi pada **{max_increase['YearMonth']}** sebesar **{max_increase['pct_change']:.1f}%** 
(menjadi {int(max_increase['New Customers'])} pelanggan).

📉 Penurunan tajam terjadi pada **{max_decrease['YearMonth']}** sebesar **{abs(max_decrease['pct_change']):.1f}%** 
(menjadi {int(max_decrease['New Customers'])} pelanggan).

🔼 Bulan dengan jumlah pelanggan baru terbanyak adalah **{max_value['YearMonth']}** sebanyak **{int(max_value['New Customers'])} pelanggan**.
🔽 Bulan dengan jumlah pelanggan baru paling sedikit adalah **{min_value['YearMonth']}** sebanyak **{int(min_value['New Customers'])} pelanggan**.

💡 Insight: 
Perlu dianalisis lebih lanjut apakah peningkatan atau penurunan ini berkaitan dengan event promosi, musim liburan, atau strategi akuisisi tertentu.
    """
       
    return summary.strip()




def df_to_tabular_string(df):
    output = io.StringIO()

    # Header
    header = " | ".join(f"{col:<20}" for col in df.columns)
    separator = "-+-".join("-" * 20 for _ in df.columns)
    output.write(header + "\n")
    output.write(separator + "\n")

    # Rows
    for _, row in df.iterrows():
        line = " | ".join(f"{str(val):<20}" for val in row)
        output.write(line + "\n")

    return output.getvalue()

import io

import json

def df_to_json(df, orient="records", indent=2):
    """
    Convert DataFrame ke JSON string.
    
    Parameters:
    - df: DataFrame pandas
    - orient: format JSON, default 'records' (list of dict per row)
              alternatif: 'split', 'index', 'columns', 'values'
    - indent: biar output rapih
    
    Return:
    - string JSON
    """
    return df.to_json(orient=orient, indent=indent, force_ascii=False)



def save_multiple_df_to_tabular_string(dfs: dict) -> str:
    """
    Simpan beberapa DataFrame ke dalam satu string dalam format tabular,
    dengan header dan separator antar bagian.

    Parameter:
    - dfs: dict, key = nama bagian (string), value = DataFrame

    Return:
    - string berisi semua DataFrame dalam format tabular
    """
    output = io.StringIO()
    
    for title, df in dfs.items():
        output.write(f"\n{'=' * 80}\n")
        output.write(f"{title.upper():^80}\n")
        output.write(f"{'=' * 80}\n")

        # Header kolom
        header = " | ".join(f"{col:<20}" for col in df.columns)
        separator = "-+-".join("-" * 20 for _ in df.columns)
        output.write(header + "\n")
        output.write(separator + "\n")

        # Isi baris
        for _, row in df.iterrows():
            line = " | ".join(f"{str(val):<20}" for val in row)
            output.write(line + "\n")

    return output.getvalue()

