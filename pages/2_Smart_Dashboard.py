import streamlit as st



from utils.custom_style import apply_custom_style


from core.generator.penyakit.generator_full_tabel_penyakit import generate_full_penyakit
from core.generator.penyakit.generator_table_penyakit import generate_kabkot_penyakit_for_table
from core.generator.penyakit.generator_for_bar_chart import generate_kabkot_penyakit_for_bar
from core.generator.penyakit.generator_for_chart_trend_penyakit import generate_trend_penyakit
from core.generator.penyakit.generator_for_geo_penyakit import generate_geo_data_penyakit
from core.generator.peserta_bpjs.generator_for_geo_peserta_bpjs import generate_geo_data_peserta
from core.generator.peserta_bpjs.generator_full_peserta_bpjs import generate_full_peserta_bpjs
from core.generator.peserta_bpjs.generator_for_trend_peserta import generate_trend_peserta
# from core.generator.faskes_rs_instansi_gabungan.generator_for_bar_rs_instansi import generate_faskes_rs_instansi
# from core.generator.faskes_rs_instansi_gabungan.generator_full_table_faskes_rs_instansi import generate_full_jenisrs_instansi
# from core.generator.faskes_rs_instansi_gabungan.generator_for_trend_rs_instansi import generate_faskes_rs_instansi_for_trend
from core.generator.peserta_bpjs.generator_kpi_jumlah_peserta import filter_peserta
from core.generator.penyakit.generator_kpi_jumlah_penderita import filter_penderita_penyakit
# from core.generator.faskes_rs_instansi_gabungan.generator_kpi_unit_faskes import filter_jumlah_unit_faskes

from core.generator.faskes_jenis.generator_for_bar_faskes_jenis import generate_bar_faskes_jenis
from core.generator.faskes_jenis.generator_for_geo_faskes_jenis import generate_geo_faskes_jenis
from core.generator.faskes_jenis.generator_for_kpi_faskes_jenis import filter_jumlah_unit_faskes_jenis
from core.generator.faskes_jenis.generator_for_summary_faskes_jenis import generate_faskes_jenis_summary
from core.generator.faskes_jenis.generator_for_trend_faskes_jenis import generate_trend_faskes_jenis


from core.generator.filter.filter_kpi_metric import *

from core.visualization.bar.bar_penyakit import plot_jumlah_penderita_per_kabupaten
from core.visualization.line.trend_penyakit import plot_trend_penyakit
from core.visualization.geo.geo_penyakit import plot_geo_penyakit
from core.visualization.geo.geo_peserta import plot_geo_peserta
from core.visualization.line.trend_peserta_bpjs import plot_trend_peserta
# from core.visualization.bar.bar_faskes_rs_instansi import plot_jumlah_faskes_rs_instansi
# from core.visualization.line.trend_faskes import plot_trend_faskes_instansi

from core.visualization.bar.bar_jenis_faskes import plot_bar_jumlah_jenis_faskes
from core.visualization.geo.geo_jenis_faskes import plot_geo_jenis_faskes
from core.visualization.line.trend_jenis_faskes import plot_trend_jenis_faskes

from features.anomali.detect_anomali_geospasial import detect_spatial_anomaly
from features.anomali.detect_anomali_trend_peserta import detect_significant_change_trend
from features.anomali.detect_anomali_trend_jenis_faskes import detect_significant_change_jenis_faskes
from features.anomali.detect_anomali_trend_penyakit import detect_significant_change_jenis_penyakit

from features.ai_insight.run_insight_pipeline import run_insight_pipeline
from features.ai_insight.final_summary import generate_llm_summary 
# Apply style
apply_custom_style()
# st.set_page_config(page_title="Dashboard",layout='wide')

# ==================================================
if "pertumbuhan_peserta" not in st.session_state:
    st.session_state.pertumbuhan_peserta = None
if "penyebaran_peserta" not in st.session_state:
    st.session_state.penyebaran_peserta = None
# if "faskes_kepemilikan" not in st.session_state:
#     st.session_state.faskes_kepemilikan = None
if "bar_jenis_faskes" not in st.session_state:
    st.session_state.bar_jenis_faskes = None
if "map_jenis_faskes" not in st.session_state:
    st.session_state.map_jenis_faskes = None
if "trend_jenis_faskes" not in st.session_state:
    st.session_state.trend_jenis_faskes = None
# if "trend_pertumbuhan_faskes" not in st.session_state:
#     st.session_state.trend_pertumbuhan_faskes = None
if "penyebaran_penyakit" not in st.session_state:
    st.session_state.penyebaran_penyakit = None
if "pertumbuhan_penyakit" not in st.session_state:
    st.session_state.pertumbuhan_penyakit = None



# ==================================================



# --- Layout ---
with st.container():
    st.markdown("""
        <div class="header-container">
            <h1>Dashboard</h1>
        </div>
    """, unsafe_allow_html=True)

# KPI Cards
col1, col2, col3,col4 = st.columns(4)
with col1:
    tahun_pilih = st.selectbox("📆 Pilih Tahun", filter_tahun())
                                                
with col2:
    kabkota_pilih = st.multiselect("Pilih Kabupaten/Kota", filter_kabkot(),default=["KABUPATEN BOGOR"],key="mulsel kabkota kpi")
with col3:
    pilih_penderita = st.multiselect(
    "Pilih Penderita",filter_penderita(),default=["Diabetes"],key="mulsel jenis penderita kpi"
)

with col4:
    pilih_jenis = st.multiselect(
    "Pilih Jenis Faskes",
    filter_jenis_faskes(),default=["POSYANDU"],key="mulsel jenis faskes"
)
col1, col2, col3= st.columns(3)
with col1:
    st.metric("Jumlah Peserta BPJS", f"{int(filter_peserta(generate_full_peserta_bpjs(),tahun=tahun_pilih,list_kabkota=kabkota_pilih))}")
with col2:
    st.metric("Jumlah Penderita", f"{int(filter_penderita_penyakit(generate_full_penyakit(),tahun=tahun_pilih,list_kabkota=kabkota_pilih,penyakit=pilih_penderita))}")
with col3:
    st.metric("Jumlah Faskes", f"{int(filter_jumlah_unit_faskes_jenis(generate_faskes_jenis_summary(),tahun=tahun_pilih,list_kabkota=kabkota_pilih,jenis_faskes=pilih_jenis))}")

st.markdown("---")



col1, col2 = st.columns(2)
with col1:
    with st.container(border=True):
        list_kota = sorted(generate_full_peserta_bpjs()['bps_nama_kabupaten_kota'].unique())
        selected_kotas = st.multiselect("Pilih Kabupaten/Kota", options=list_kota, default=["KABUPATEN BOGOR"])
        df_agg = generate_trend_peserta(selected_kotas)
        st.plotly_chart(
            plot_trend_peserta(df_agg, selected_kotas),
            use_container_width=True
        )
        alerts = detect_significant_change_trend(df_agg)
        
        if alerts:
            with st.popover("🚨 Lihat perubahan signifikan"):
                st.markdown("\n".join([f"- {a}" for a in alerts]))
        else:
            st.success("Tidak ada perubahan signifikan untuk jumlah peserta di kabupaten ini")


        if st.button("🧠 Generate AI", key="ai trend peserta"):
            with st.spinner("Generate AI..."):
                # Simpan hasil ke session_state sekali saja
                st.session_state.pertumbuhan_peserta = run_insight_pipeline(
                    df_agg, insight_type="pertumbuhan_peserta_bpjs"
                )
                st.success("success")

        # Popover hanya muncul jika sudah ada insight di session_state
        if st.session_state.pertumbuhan_peserta:
            with st.popover("📌 Lihat Insight"):
                st.markdown(st.session_state.pertumbuhan_peserta)

with col2:
    with st.container(border=True):
        list_tahun = sorted(generate_full_peserta_bpjs()['tahun'].astype(int).unique())
        tahun = st.selectbox("Pilih Tahun", options=list_tahun)

        df = generate_geo_data_peserta(selected_tahun=tahun)
        st.plotly_chart(
            plot_geo_peserta(df_agg=df, selected_tahun=tahun),
            use_container_width=True
        )

        detect_spatial_anomaly(df=df,group_col="bps_nama_kabupaten_kota",jumlah_col="jumlah_ warga_terdaftar_bpjs",label=tahun)

        if st.button("🧠 Generate AI", key="ai penyebaran peserta"):
            with st.spinner("Generate AI..."):
                st.session_state.penyebaran_peserta = run_insight_pipeline(
                    df, insight_type="penyebaran_peserta_bpjs"
                )
                st.success("success")

        if st.session_state.penyebaran_peserta:
            with st.popover("📌 Lihat Insight"):
                st.markdown(st.session_state.penyebaran_peserta)



with st.container(border=True):
    tab1, tab2, tab3= st.tabs([ 
        "📊 Grafik Total Faskes berdasarkan jenis", 
        "🗺️ Penyebaran Jenis Faskes",
        "📈 Tren Jenis Faskes"
    ])
    with tab1:
        col1, col2 = st.columns(2)
        with col1:
            kota_option = st.selectbox("🏙️ Pilih Kab/Kota", generate_faskes_jenis_summary()['nama_kabupaten_kota'].unique())
        with col2:
            selected_tahun = st.selectbox("📆 Pilih Tahun", generate_faskes_jenis_summary()["tahun"].unique(),key="select box for jenis faskes grafik")
        df = generate_bar_faskes_jenis(selected_kota=kota_option,tahun=selected_tahun)
        st.plotly_chart(plot_bar_jumlah_jenis_faskes(df,selected_kota=kota_option,tahun=tahun),use_container_width=True)
        if st.button("🧠 Generate AI", key="ai sdistribusi jenis faskes"):
            with st.spinner("Generate AI..."):
                st.session_state.bar_jenis_faskes = run_insight_pipeline(
                    df, insight_type="jumlah_faskes_berdasarkan_jenis"
                )
                st.success("success")

        if st.session_state.bar_jenis_faskes:
            with st.popover("📌 Lihat Insight"):
                st.markdown(st.session_state.bar_jenis_faskes)
    with tab2:
        col1, col2 = st.columns(2)
        with col1:
            jenisfaskes_option = st.selectbox("🏙️ Pilih Jenis Faskes", generate_faskes_jenis_summary()['jenis_faskes'].unique())
        with col2:
            tahun_option = st.selectbox("📆 Pilih Tahun", generate_faskes_jenis_summary()["tahun"].unique(),key="select box tahun jenis faskes map")

        df = generate_geo_faskes_jenis(selected_jenis_faskes=jenisfaskes_option, selected_tahun=tahun_option)
        st.plotly_chart(
            plot_geo_jenis_faskes(df_agg=df,jenis_faskes_option=jenisfaskes_option,selected_tahun=tahun_option),
            use_container_width=True)
        
        detect_spatial_anomaly(df=df,group_col="nama_kabupaten_kota", jumlah_col="jumlah_faskes", label=jenisfaskes_option)
        
        if st.button("🧠 Generate AI", key="ai map jenis faskes"):
            with st.spinner("Generate AI..."):
                st.session_state.map_jenis_faskes = run_insight_pipeline(
                    df, insight_type="penyebaran_jenis_faskes"
                )
                st.success("success")

        if st.session_state.map_jenis_faskes:
            with st.popover("📌 Lihat Insight"):
                st.markdown(st.session_state.map_jenis_faskes)
        
    with tab3:
        kota_option = st.selectbox("🏙️ Pilih Kab/Kota", generate_faskes_jenis_summary()['nama_kabupaten_kota'].unique(), key="trend jenis faskes")
        df = generate_trend_faskes_jenis(selected_kota=kota_option)
        st.plotly_chart(plot_trend_jenis_faskes(df,kota_option),use_container_width=True)

        # Cek perubahan signifikan
        alerts = detect_significant_change_jenis_faskes(df,group_col="jenis_faskes",value_col="jumlah_faskes",time_col="tahun")
        if alerts:
            with st.popover("🚨 Lihat perubahan signifikan"):
                st.markdown("\n".join([f"- {a}" for a in alerts]))
        else:
            st.success("Tidak ada perubahan signifikan untuk jumlah faskes di kabupaten ini")


        if st.button("🧠 Generate AI", key="ai trend jenis faskes"):
            with st.spinner("Generate AI..."):
                st.session_state.trend_jenis_faskes = run_insight_pipeline(
                    df, insight_type="pertumbuhan_jenis_faskes"
                )
                st.success("success")

        if st.session_state.trend_jenis_faskes:
            with st.popover("📌 Lihat Insight"):
                st.markdown(st.session_state.trend_jenis_faskes)


st.markdown("---")

with st.container(border=True):
    tab1, tab2, tab3, tab4 = st.tabs([
        "📋 Tabel Penderita per Kab/Kota", 
        "📊 Grafik Total Penderita per Kab/Kota", 
        "🗺️ Peta Persebaran Penyakit",
        "📈 Trend Penyakit per Kab/Kota"
    ])

    with tab1:
        st.dataframe(generate_kabkot_penyakit_for_table().sort_values(by='tahun', ascending=True))

    with tab2:
        with st.container(border=True):
            st.plotly_chart(
                plot_jumlah_penderita_per_kabupaten(df=generate_kabkot_penyakit_for_bar()),
                use_container_width=True
            )

    with tab3:
        with st.container(border=True):
            col1, col2 = st.columns(2)
            with col1:
                penyakit_option = st.selectbox("🩺 Pilih Jenis Penyakit", generate_full_penyakit()['jenis_penderita'].unique())
            with col2:
                tahun = st.selectbox("📆 Pilih Tahun", generate_full_penyakit()["tahun"].unique(),key="tahun_penyakit")

            df = generate_geo_data_penyakit(selected_penyakit=[penyakit_option], selected_tahun=tahun)
            st.plotly_chart(
                plot_geo_penyakit(df_agg=df, penyakit_option=penyakit_option, selected_tahun=selected_tahun),
                use_container_width=True
            )

            detect_spatial_anomaly(df=df,group_col="nama_kabupaten_kota", jumlah_col="Total jumlah penderita", label=penyakit_option)



            if st.button("🧠 Generate AI", key="ai_penyebaran_penyakit"):
                with st.spinner("Generate AI..."):
                    st.session_state.penyebaran_penyakit = run_insight_pipeline(
                        df, insight_type="penyebaran_penyakit"
                    )
                    st.success("success")

            if st.session_state.penyebaran_penyakit:
                with st.popover("📌 Lihat Insight"):
                    st.markdown(st.session_state.penyebaran_penyakit)


    with tab4:
        with st.container(border=True):
            select_kabkot= st.selectbox("🏛️ Pilih Kabupaten Kota", generate_full_penyakit()["nama_kabupaten_kota"].unique(),key="select_box_trend_prenyakit_kabkot")
            df_agg = generate_trend_penyakit(select_kabkot)
            st.plotly_chart(
                plot_trend_penyakit(df_agg,select_kabkot),
                use_container_width=True
            )

            alerts = detect_significant_change_jenis_penyakit(df=df_agg,group_col="jenis_penderita",value_col="jumlah_penderita", time_col="tahun")
            if alerts:
                with st.popover("🚨 Lihat perubahan signifikan"):
                    st.markdown("\n".join([f"- {a}" for a in alerts]))
            else:
                st.success("Tidak ada perubahan signifikan untuk jenis penyakit di kabupaten ini")


            if st.button("🧠 Generate AI", key="ai_tren_penyakit"):
                with st.spinner("Generate AI..."):
                    st.session_state.pertumbuhan_penyakit = run_insight_pipeline(
                        df_agg, insight_type="pertumbuhan_penyakit"
                    )
                    st.success("success")

            if st.session_state.pertumbuhan_penyakit:
                with st.popover("📌 Lihat Insight"):
                    st.markdown(st.session_state.pertumbuhan_penyakit)



st.markdown("### 🔍 Insight Otomatis")
if st.button("🧠 Generate Summary", key="ai_summary"):
    with st.spinner("sedang menganalisis dan menyusun summary..."):
        hasil_summary = generate_llm_summary()
        st.session_state["final_summary"] = hasil_summary
        st.success("berhasil dibuat")

if st.session_state.get("final_summary"):
        with st.popover("📋 Laporan Final dari AI"):
            st.markdown(st.session_state["final_summary"])
from features.ai_insight.insight_conversation import handle_insight_conversation



# # Conversation
# st.markdown("### 🤖 Conversation Assitant")


# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []

# # Tampilkan tombol hapus kalau ada history
# if st.session_state.chat_history:
#     col1, col2 = st.columns([0.85, 0.15])
#     with col2:
#         if st.button("🗑️ Hapus Chat"):
#             st.session_state.chat_history = []
#             st.rerun()

# # Tampilkan histori chat
# for role, message in st.session_state.chat_history:
#     with st.chat_message(role):
#         st.markdown(message)

# # Input chat baru
# if prompt := st.chat_input("Tulis pertanyaanmu di sini..."):
#     # Simpan pertanyaan user
#     st.session_state.chat_history.append(("user", prompt))

#     with st.chat_message("user"):
#         st.markdown(prompt)

#     with st.chat_message("assistant"):
#         with st.spinner("🤖 Menganalisis dan menjawab..."):
#             answer = handle_insight_conversation(prompt)
#             st.markdown(answer)

#     # Simpan jawaban AI ke histori
#     st.session_state.chat_history.append(("assistant", answer))

# st.markdown("---")


# # AI Insight
# st.markdown("### 🤖 Insight Otomatis")
# st.info("Pada bulan terakhir terjadi peningkatan klaim sebesar 5.2% dibandingkan bulan sebelumnya. Disarankan untuk meninjau alokasi anggaran.")

st.markdown("---")
st.caption("© 2025 PT LANGIT. Prototype dashboard by LANGIT.")
