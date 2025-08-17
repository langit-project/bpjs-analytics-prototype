import streamlit as st
from utils.custom_style import apply_custom_style
from st_pages import Page, Section, show_pages, add_page_title  # <- tambahkan ini

st.set_page_config(page_title="Dashboard AI", layout='wide')

# Load style hanya sekali
apply_custom_style()

add_page_title()

# Sidebar logo
st.sidebar.image("assets/bpjs_logo.png", width=150)
st.sidebar.markdown("---")

st.markdown("""
<style>
[data-testid="stSidebar"] {
    background: linear-gradient(to bottom, #0D9276, #106EBE);
    color: white;
}
</style>
""", unsafe_allow_html=True)

show_pages(
    [
        Section("Main Pages", "🏠"),
        Page("app.py", "Home", "🏡", in_section=True),  # optional: masukkan app.py
        Page("pages/dashboard.py", "Dashboard", "📊", in_section=True),
        Page("pages/forecasting.py", "Forecasting", "📈", in_section=True),
        Page("pages/page_conversation.py", "Conversation", "💬", in_section=True)
    ]
)


# Header utama
st.markdown("""
<h1 style="text-align: center; font-size: 2.5em;">🚀 Selamat Datang di <span style="color:#0D9276;">Dashboard AI</span></h1>
<p style="text-align: center; font-size: 1.1em; color: #555;">
Pantau data, dapatkan insight AI, dan pantau prediksi.
</p>
""", unsafe_allow_html=True)

st.write("---")

# Penjelasan fitur
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 📊 Dashboard")
    st.write("""
    Lihat visualisasi data yang interaktif  
    untuk memantau tren, performa serta generate insight berbasis AI.
    """)

with col2:
    st.markdown("### 📈 Forecasting")
    st.write("""
    Prediksi tren masa depan menggunakan  
    model statistik dan machine learning.
    """)

with col3:
    st.markdown("### 💬 Page Conversation")
    st.write("""
    Diskusikan data dengan AI untuk  
    mendapatkan insight secara langsung.
    """)

st.write("---")

# Guide penggunaan
st.markdown("""
### 🧭 Panduan Singkat
1. Pilih menu di sebelah kiri untuk berpindah halaman.
2. Gunakan **Dashboard** untuk melihat data dan insight awal.
3. Gunakan **Forecasting** untuk memprediksi tren ke depan.
4. Gunakan **Page Conversation** untuk bertanya langsung ke AI.

💡 **Tips:** Mulailah dari *Dashboard* agar mendapatkan gambaran umum sebelum masuk ke analisis lebih detail.
""")
