# core/processor/penyakit_processor.py
from connection.conn import DataLoader
import pandas as pd
import streamlit as st
from statsmodels.tsa.statespace.sarimax import SARIMAX
import numpy as np

import plotly.graph_objects as go

def forecast_trend_peserta_sarimax_ci(df, selected_kota: list[str], forecast_years: int = 2) -> pd.DataFrame:
    df_agg = df.copy()
    all_forecasts = []

    for kota in selected_kota:
        df_kota = df_agg[df_agg['bps_nama_kabupaten_kota'] == kota].copy()

        # Skip kalau data kosong
        if df_kota.empty:
            print(f"[INFO] Data untuk {kota} tidak ditemukan, dilewati.")
            continue

        # Rename kolom
        df_kota = df_kota.rename(columns={'jumlah_ warga_terdaftar_bpjs': 'jumlah'})
        
        # Pastikan format tahun benar
        df_kota['tahun'] = pd.to_datetime(df_kota['tahun'], format='%Y')
        df_kota.set_index('tahun', inplace=True)

        # Fit SARIMAX
        model = SARIMAX(df_kota['jumlah'], order=(1, 1, 1), seasonal_order=(0, 0, 0, 0))
        results = model.fit(disp=False)

        # Forecast dengan CI
        future = results.get_forecast(steps=forecast_years)
        forecast_df = future.predicted_mean.reset_index()
        forecast_df.columns = ['tahun', 'jumlah']
        forecast_df['tipe'] = 'forecast'
        forecast_df['lower_ci'] = future.conf_int().iloc[:, 0].values
        forecast_df['upper_ci'] = future.conf_int().iloc[:, 1].values

        # Historical
        df_hist = df_kota.reset_index()[['tahun', 'jumlah']]
        df_hist['tipe'] = 'actual'
        df_hist['lower_ci'] = None
        df_hist['upper_ci'] = None

        # Tambah nama kota
        df_hist['bps_nama_kabupaten_kota'] = kota
        forecast_df['bps_nama_kabupaten_kota'] = kota

        all_forecasts.append(pd.concat([df_hist, forecast_df], ignore_index=True))

    # Kalau semua kota kosong, return df kosong dengan kolom standar
    if not all_forecasts:
        return pd.DataFrame(columns=['tahun', 'jumlah', 'tipe', 'lower_ci', 'upper_ci', 'bps_nama_kabupaten_kota'])

    df_result = pd.concat(all_forecasts, ignore_index=True)
    df_result.sort_values(['bps_nama_kabupaten_kota', 'tahun'], inplace=True)
    return df_result



def plot_forecast_with_ci(df_forecast):
    fig = go.Figure()

    for kota in df_forecast['bps_nama_kabupaten_kota'].unique():
        df_kota = df_forecast[df_forecast['bps_nama_kabupaten_kota'] == kota].sort_values('tahun')

        # Garis nyambung (actual + forecast)
        fig.add_trace(go.Scatter(
            x=df_kota['tahun'],
            y=df_kota['jumlah'],
            mode='lines+markers',
            name=kota
        ))

        # Tambah marker khusus untuk forecast
        df_fc = df_kota[df_kota['tipe'] == 'forecast']
        fig.add_trace(go.Scatter(
            x=df_fc['tahun'],
            y=df_fc['jumlah'],
            mode='markers',
            name=f"{kota} (Forecast)",
            marker=dict(symbol="circle-open", size=20, line=dict(width=2))
        ))


        # Confidence interval hanya untuk forecast
        df_fc = df_kota[df_kota['tipe'] == 'forecast']
        fig.add_trace(go.Scatter(
            x=pd.concat([df_fc['tahun'], df_fc['tahun'][::-1]]),
            y=pd.concat([df_fc['upper_ci'], df_fc['lower_ci'][::-1]]),
            fill='toself',
            fillcolor='rgba(0, 100, 80, 0.2)',
            line=dict(color='rgba(255,255,255,0)'),
            hoverinfo="skip",
            name=f"{kota} (Confidence Interval)"
        ))

    fig.update_layout(
        title="Trend & Forecast Peserta BPJS per Kota (dengan Confidence Interval)",
        xaxis_title="Tahun",
        yaxis_title="Jumlah Peserta BPJS",
        hovermode="x unified"
    )
    return fig


