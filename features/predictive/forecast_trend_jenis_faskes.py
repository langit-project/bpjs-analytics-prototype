import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX
import plotly.graph_objects as go




def forecast_trend_faskes_sarimax_ci(df, selected_kota: str, forecast_years: int = 2) -> pd.DataFrame:
    df_agg = df.copy()
    all_forecasts = []

    # Filter ke kabupaten/kota yang dipilih
    df_kota = df_agg[df_agg['nama_kabupaten_kota'] == selected_kota].copy()

    if df_kota.empty:
        print(f"[INFO] Data untuk {selected_kota} tidak ditemukan.")
        return pd.DataFrame(columns=['tahun', 'jumlah_faskes', 'tipe', 'lower_ci', 'upper_ci', 'nama_kabupaten_kota', 'jenis_faskes'])

    # Loop per jenis faskes
    for jenis in df_kota['jenis_faskes'].unique():
        df_jenis = df_kota[df_kota['jenis_faskes'] == jenis].copy()

        # Skip kalau kosong
        if df_jenis.empty:
            continue

        # Rename kolom ke 'jumlah' biar konsisten
        df_jenis = df_jenis.rename(columns={'jumlah_faskes': 'jumlah'})
        
        # Pastikan tahun datetime index
        df_jenis['tahun'] = pd.to_datetime(df_jenis['tahun'], format='%Y')
        df_jenis.set_index('tahun', inplace=True)

        # Fit SARIMAX
        model = SARIMAX(df_jenis['jumlah'], order=(1,1,1), seasonal_order=(0,0,0,0))
        results = model.fit(disp=False)

        # Forecast + CI
        future = results.get_forecast(steps=forecast_years)
        forecast_df = future.predicted_mean.reset_index()
        forecast_df.columns = ['tahun', 'jumlah']
        forecast_df['tipe'] = 'forecast'
        forecast_df['lower_ci'] = future.conf_int().iloc[:, 0].values
        forecast_df['upper_ci'] = future.conf_int().iloc[:, 1].values

        # Historical
        df_hist = df_jenis.reset_index()[['tahun', 'jumlah']]
        df_hist['tipe'] = 'actual'
        df_hist['lower_ci'] = None
        df_hist['upper_ci'] = None

        # Tambah kolom metadata
        df_hist['nama_kabupaten_kota'] = selected_kota
        df_hist['jenis_faskes'] = jenis
        forecast_df['nama_kabupaten_kota'] = selected_kota
        forecast_df['jenis_faskes'] = jenis

        # Gabungkan
        all_forecasts.append(pd.concat([df_hist, forecast_df], ignore_index=True))

    if not all_forecasts:
        return pd.DataFrame(columns=['tahun', 'jumlah', 'tipe', 'lower_ci', 'upper_ci', 'nama_kabupaten_kota', 'jenis_faskes'])

    df_result = pd.concat(all_forecasts, ignore_index=True)
    df_result.sort_values(['jenis_faskes', 'tahun'], inplace=True)
    return df_result

def forecast_trend_faskes_sarimax_ci_summary(df, forecast_years: int = 2) -> pd.DataFrame:
    df_agg = df.copy()
    all_forecasts = []

    # Loop per kabupaten/kota
    for kota in df_agg['nama_kabupaten_kota'].unique():
        df_kota = df_agg[df_agg['nama_kabupaten_kota'] == kota].copy()

        # Skip kalau kosong
        if df_kota.empty:
            continue

        # Loop per jenis faskes
        for jenis in df_kota['jenis_faskes'].unique():
            df_jenis = df_kota[df_kota['jenis_faskes'] == jenis].copy()

            if df_jenis.empty:
                continue

            # Rename kolom ke 'jumlah'
            df_jenis = df_jenis.rename(columns={'jumlah_faskes': 'jumlah'})
            
            # Pastikan tahun datetime index
            df_jenis['tahun'] = pd.to_datetime(df_jenis['tahun'], format='%Y')
            df_jenis.set_index('tahun', inplace=True)

            try:
                # Fit SARIMAX
                model = SARIMAX(df_jenis['jumlah'], order=(1,1,1), seasonal_order=(0,0,0,0))
                results = model.fit(disp=False)

                # Forecast + CI
                future = results.get_forecast(steps=forecast_years)
                forecast_df = future.predicted_mean.reset_index()
                forecast_df.columns = ['tahun', 'jumlah']
                forecast_df['tipe'] = 'forecast'
                forecast_df['lower_ci'] = future.conf_int().iloc[:, 0].values
                forecast_df['upper_ci'] = future.conf_int().iloc[:, 1].values

                # Historical
                df_hist = df_jenis.reset_index()[['tahun', 'jumlah']]
                df_hist['tipe'] = 'actual'
                df_hist['lower_ci'] = None
                df_hist['upper_ci'] = None

                # Tambah metadata
                df_hist['nama_kabupaten_kota'] = kota
                df_hist['jenis_faskes'] = jenis
                forecast_df['nama_kabupaten_kota'] = kota
                forecast_df['jenis_faskes'] = jenis

                # Gabungkan
                all_forecasts.append(pd.concat([df_hist, forecast_df], ignore_index=True))
            
            except Exception as e:
                print(f"[ERROR] Gagal forecast {kota} - {jenis}: {e}")
                continue

    if not all_forecasts:
        return pd.DataFrame(columns=['tahun', 'jumlah', 'tipe', 'lower_ci', 'upper_ci', 'nama_kabupaten_kota', 'jenis_faskes'])

    df_result = pd.concat(all_forecasts, ignore_index=True)
    df_result.sort_values(['nama_kabupaten_kota', 'jenis_faskes', 'tahun'], inplace=True)
    return df_result


def plot_forecast_faskes_with_ci(df_forecast, kota_name: str):
    fig = go.Figure()

    for faskes in df_forecast['jenis_faskes'].unique():
        df_faskes = df_forecast[df_forecast['jenis_faskes'] == faskes].sort_values('tahun')

        # garis actual + forecast
        fig.add_trace(go.Scatter(
            x=df_faskes['tahun'],
            y=df_faskes['jumlah'],
            mode='lines+markers',
            name=faskes
        ))

        # marker forecast
        df_fc = df_faskes[df_faskes['tipe'] == 'forecast']
        fig.add_trace(go.Scatter(
            x=df_fc['tahun'],
            y=df_fc['jumlah'],
            mode='markers',
            name=f"{faskes} (Forecast)",
            marker=dict(symbol="circle-open", size=12, line=dict(width=2))
        ))

        # # CI untuk forecast
        # fig.add_trace(go.Scatter(
        #     x=pd.concat([df_fc['tahun'], df_fc['tahun'][::-1]]),
        #     y=pd.concat([df_fc['upper_ci'], df_fc['lower_ci'][::-1]]),
        #     fill='toself',
        #     fillcolor='rgba(0,100,200,0.2)',
        #     line=dict(color='rgba(255,255,255,0)'),
        #     hoverinfo="skip",
        #     name=f"{faskes} (CI)"
        # ))

    fig.update_layout(
        title=f"Trend & Forecast Jumlah Faskes per Jenis di {kota_name}",
        xaxis_title="Tahun",
        yaxis_title="Jumlah Faskes",
        hovermode="x unified"
    )
    return fig