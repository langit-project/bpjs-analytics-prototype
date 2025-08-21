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
from features.predictive.forecast_trend_jenis_penyakit import forecast_trend_penyakit_sarimax_ci,plot_forecast_penyakit_with_ci

from features.ai_insight.run_insight_pipeline_predictive import run_insight_multiple_data
# Apply style
apply_custom_style()

if "faskes_vs_penyakit" not in st.session_state:
    st.session_state.faskes_vs_penyakit = None



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
    
    df_forecast_penyakit = forecast_trend_penyakit_sarimax_ci(df = df_agg_penyakit,selected_kota=selected_kotas)
    plot_penyakit_forcast = plot_forecast_penyakit_with_ci(df_forecast=df_forecast_penyakit,kota_name=selected_kotas)
    col1,col2 = st.columns(2)
    with col1:
        st.plotly_chart(plot_jenis_faskes_forcast, use_container_width=True)

    with col2:
        st.plotly_chart(plot_penyakit_forcast, use_container_width=True)
    if st.button("🧠 Generate AI", key="ai forcast faskes vs penyakit"):
        with st.spinner("Generate AI..."):
            # Simpan hasil ke session_state sekali saja
            st.session_state.faskes_vs_penyakit = run_insight_multiple_data(df_forecast_jenis_faskes,df_forecast_penyakit)
            st.success("success")

    # Popover hanya muncul jika sudah ada insight di session_state
    if st.session_state.faskes_vs_penyakit:
        with st.popover("📌 Lihat Insight"):
            st.markdown(st.session_state.faskes_vs_penyakit)










