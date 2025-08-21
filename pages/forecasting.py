import streamlit as st
import plotly.express as px

from utils.custom_style import apply_custom_style

from core.generator.filter.filter_kpi_metric import *


from core.generator.peserta_bpjs.generator_full_peserta_bpjs import generate_full_peserta_bpjs
from core.generator.peserta_bpjs.generator_for_trend_peserta import generate_trend_peserta
from core.generator.penyakit.generator_for_chart_trend_penyakit import generate_trend_penyakit
from core.generator.faskes_jenis.generator_for_trend_faskes_jenis import generate_trend_faskes_jenis


from features.predictive.forecast_trend_peserta_bpjs import forecast_trend_peserta_sarimax_ci,plot_forecast_with_ci
from features.predictive.forecast_trend_jenis_faskes import forecast_trend_faskes_sarimax_ci,plot_forecast_faskes_with_ci
# Apply style
apply_custom_style()


# list_kota = sorted(generate_full_peserta_bpjs()['bps_nama_kabupaten_kota'].unique())
selected_kotas = st.multiselect("Pilih Kabupaten/Kota", filter_kabkot(), default=["KABUPATEN BOGOR"])
df_agg = generate_trend_peserta(selected_kotas)
# forecast ci
df_forecast_ci=forecast_trend_peserta_sarimax_ci(df=df_agg,selected_kota=selected_kotas,forecast_years=3)

# st.dataframe(df_forecast_ci)

st.plotly_chart(plot_forecast_with_ci(df_forecast_ci), use_container_width=True)


st.markdown("---")

with st.container(border=True):
    selected_kotas = st.selectbox("Pilih Kabupaten/Kota", filter_kabkot())
    df_agg_jenis_faskes = generate_trend_faskes_jenis(selected_kota=selected_kotas)
    df_agg_penyakit = generate_trend_penyakit(selected_kotas=selected_kotas)
    df_forecast_jenis_faskes = forecast_trend_faskes_sarimax_ci(df = df_agg_jenis_faskes,selected_kota=selected_kotas)
    plot_jenis_faskes_forcast = plot_forecast_faskes_with_ci(df_forecast_jenis_faskes,selected_kotas)

    col1,col2 = st.columns(2)
    with col1:
        
        # st.dataframe(df_agg_jenis_faskes)
        # st.dataframe(df_forecast_jenis_faskes)
        st.plotly_chart(plot_jenis_faskes_forcast, use_container_width=True)

    with col2:
        st.markdown("dalam perbaikan")
        # st.dataframe(df_agg_penyakit)







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







