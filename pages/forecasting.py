import streamlit as st
import plotly.express as px

from utils.custom_style import apply_custom_style

from core.generator.peserta_bpjs.generator_full_peserta_bpjs import generate_full_peserta_bpjs
from core.generator.peserta_bpjs.generator_for_trend_peserta import generate_trend_peserta

from features.forecast.forecast_trend_peserta_bpjs import forecast_trend_peserta_sarimax,plot_forecast_line,forecast_trend_peserta_sarimax_ci,plot_forecast_with_ci
# Apply style
apply_custom_style()


list_kota = sorted(generate_full_peserta_bpjs()['bps_nama_kabupaten_kota'].unique())
selected_kotas = st.multiselect("Pilih Kabupaten/Kota", options=list_kota, default=["KABUPATEN BOGOR"])
df_agg = generate_trend_peserta(selected_kotas)
# forecast ci
df_forecast_ci=forecast_trend_peserta_sarimax_ci(df=df_agg,selected_kota=selected_kotas,forecast_years=3)

# st.dataframe(df_forecast_ci)

st.plotly_chart(plot_forecast_with_ci(df_forecast_ci), use_container_width=True)

# df_forecast=forecast_trend_peserta_sarimax(df=df_agg,selected_kota=selected_kotas,forecast_years=3)

# st.dataframe(df_forecast)

# import altair as alt

# chart_actual = alt.Chart(df_forecast).mark_line(point=True).encode(
#     x='tahun:T',
#     y=alt.Y('actual', title='Jumlah Peserta BPJS'),
#     color='bps_nama_kabupaten_kota',
#     tooltip=['bps_nama_kabupaten_kota', 'tahun', 'actual']
# )

# # Plot forecast (garis putus-putus)
# chart_forecast = alt.Chart(df_forecast).mark_line(strokeDash=[5, 5]).encode(
#     x='tahun:T',
#     y='forecast',
#     color='bps_nama_kabupaten_kota',
#     tooltip=['bps_nama_kabupaten_kota', 'tahun', 'forecast']
# )

# st.altair_chart((chart_actual + chart_forecast).properties(
#     title="Trend & Forecast Peserta BPJS per Kota"
# ), use_container_width=True)



# # ======= plotly
# fig = px.line(
#     df_forecast,
#     x="tahun",
#     y="jumlah",
#     color="bps_nama_kabupaten_kota",
#     line_dash="tipe",  # actual = garis solid, forecast = garis putus-putus
#     markers=True,
#     title="Trend & Forecast Peserta BPJS per Kota"
# )

# fig.update_layout(
#     xaxis_title="Tahun",
#     yaxis_title="Jumlah Peserta BPJS",
#     legend_title="Kota",
#     hovermode="x unified"
# )

# st.plotly_chart(fig, use_container_width=True)

# fig = plot_forecast_line(df_forecast)
# st.plotly_chart(fig, use_container_width=True)







