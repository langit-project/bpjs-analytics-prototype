import streamlit as st
from utils.custom_style import apply_custom_style

st.set_page_config(page_title="Dashboard AI", layout='wide')
# ============== LOGIN ==============
USER_CREDENTIALS = {
    "yogi": "12345",
    "admin": "admin123"
}

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""

if not st.session_state.logged_in:
    # 🔒 HIDE SIDEBAR saat belum login
    hide_sidebar_style = """
        <style>
        [data-testid="stSidebar"] {visibility: hidden;}
        </style>
    """
    st.markdown(hide_sidebar_style, unsafe_allow_html=True)


    st.title("🔐 Login ke Dashboard")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.rerun()
        else:
            st.error("Username atau password salah ❌")
else:

# Load style hanya sekali
    apply_custom_style()

    # Header utama
    st.markdown("""
    <h1 style="text-align: center; font-size: 2.5em;">🚀 Selamat Datang di <span style="color:#0D9276;">Smart Dasboard</span></h1>
    <p style="text-align: center; font-size: 1.1em; color: #555;">
    Pantau data, dapatkan insight AI, dan pantau prediksi.
    </p>
    """, unsafe_allow_html=True)

    st.write("---")

    # Penjelasan fitur
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### 📊 Smart Dashboard")
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
        st.markdown("### 💬 Chat")
        st.write("""
        Diskusikan data dengan AI untuk  
        mendapatkan insight secara langsung.
        """)

    st.write("---")

    # Guide penggunaan
    st.markdown("""
    ### 🧭 Panduan Singkat
    1. Pilih menu di sebelah kiri untuk berpindah halaman.
    2. Gunakan **Smart Dashboard** untuk melihat data dan insight awal.
    3. Gunakan **Forecasting** untuk memprediksi tren ke depan.
    4. Gunakan **Chat** untuk bertanya langsung ke AI.

    💡 **Tips:** Mulailah dari *Smart Dashboard* agar mendapatkan gambaran umum sebelum masuk ke analisis lebih detail.
    """)
