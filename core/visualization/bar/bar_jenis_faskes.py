# import pandas as pd
# import plotly.express as px

# import streamlit as st

# @st.cache_data

# def plot_bar_jumlah_jenis_faskes(df: pd.DataFrame, selected_kota:str, tahun:int):
#     # Urutkan kabupaten berdasarkan total jumlah penderita
#     fig = px.bar(
#             df, 
#             x='jenis_faskes',
#             y='jumlah_faskes',
#             color='jenis_faskes',
#             barmode='group',
#             title=f'Jumlah Jenis Faskes di {selected_kota} tahun {tahun}',
#             color_discrete_sequence=px.colors.sequential.Tealgrn_r,
#         )
#     fig.update_layout(
#             bargap=0.05,            # Jarak antar bar sangat rapat
#             height=350,
#             xaxis_title='Jenis Faskes',
#             yaxis_title='Jumlah Faskes',
#             uniformtext_minsize=8,
#             uniformtext_mode='hide'
#         )
#     fig.update_traces(texttemplate='%{y}', textposition='outside')
#     return fig



import pandas as pd
import plotly.express as px
import streamlit as st

@st.cache_data
def plot_bar_jumlah_jenis_faskes(df: pd.DataFrame, selected_kota: str, tahun: int):
    # Urutkan berdasarkan jumlah_faskes
    df_sorted = df.sort_values("jumlah_faskes", ascending=False)

    fig = px.bar(
        df_sorted, 
        x='jenis_faskes',
        y='jumlah_faskes',
        color='jenis_faskes',
        barmode='group',
        title=f'Jumlah Jenis Faskes di {selected_kota} tahun {tahun}',
        color_discrete_sequence=px.colors.sequential.Tealgrn_r,
    )

    fig.update_traces(
        texttemplate='<b>%{y}</b>',  # Angka tebal
        textposition='outside',
        marker_line_width=0           # Hilangkan garis pinggir bar
    )

    fig.update_layout(
        bargap=0.15,                  # Jarak antar bar proporsional
        height=400,
        xaxis_title='Jenis Faskes',
        yaxis_title='Jumlah Faskes',
        uniformtext_minsize=8,
        uniformtext_mode='hide',
        template="simple_white",      # Template clean
        font=dict(size=12)            # Ukuran font pas
    )

    return fig
