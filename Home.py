import streamlit as st
from utils.custom_style import apply_custom_style
import pickle
from pathlib import Path

import streamlit_authenticator as stauth


# st.set_page_config(page_title="Dashboard AI", layout='wide')
# import pickle
# from pathlib import Path

# file_path = Path(__file__).parent / "hashed_pw.pkl"
# with file_path.open("rb") as file:
#     hashed_passwords = pickle.load(file)  # list of hashed passwords


# # --- USER AUTHENTICATION
# credentials = {
#     "usernames": {
#         "admin1": {"name": "ADMIN 1", "password": hashed_passwords[0]},
#         "admin2": {"name": "ADMIN 2", "password": hashed_passwords[1]}
#     }
# }

# authenticator = stauth.Authenticate(
#     credentials=credentials,
#     cookie_name="dashboard_ai_cookie",
#     key="dashboard_ai_key",
#     cookie_expiry_days=30
# )
# authentication_status= authenticator.login(
#     location="main"
# )
# if authentication_status == False:
#     st.error("username/password incorrect")

# if authentication_status == None:
#     st.warning("Please enter your username and password")

# if authentication_status:





# # ============== LOGIN ==============
# USER_CREDENTIALS = {
#     "yogi": "12345",
#     "admin": "admin123"
# }

# if "logged_in" not in st.session_state:
#     st.session_state.logged_in = False
# if "username" not in st.session_state:
#     st.session_state.username = ""

# if not st.session_state.logged_in:
#     # 🔒 HIDE SIDEBAR saat belum login
#     hide_sidebar_style = """
#         <style>
#         [data-testid="stSidebar"] {visibility: hidden;}
#         </style>
#     """
#     st.markdown(hide_sidebar_style, unsafe_allow_html=True)


#     st.title("🔐 Login ke Dashboard")

#     username = st.text_input("Username")
#     password = st.text_input("Password", type="password")

#     if st.button("Login"):
#         if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
#             st.session_state.logged_in = True
#             st.session_state.username = username
#             st.rerun()
#         else:
#             st.error("Username atau password salah ❌")
# else:

import streamlit as st
from utils.custom_style import apply_custom_style
from utils.auth import get_authenticator



# Load style hanya sekali

# authenticator.logout("Logout","sidebar")
# Header utama
authenticator = get_authenticator()


# panggil login form
authenticator.login(location="main")

auth_status = st.session_state.get("authentication_status")
name = st.session_state.get("name")
username = st.session_state.get("username")


# kalau BELUM login -> sembunyikan sidebar
if not auth_status:
    st.markdown(
        """
        <style>
        [data-testid="stSidebar"] {display: none;}
        [data-testid="stSidebarNav"] {display: none;}
        </style>
        """,
        unsafe_allow_html=True,
    )


if auth_status:
    # Tampilkan tombol logout di sidebar
    apply_custom_style()
    authenticator.logout("Logout", "sidebar")
    st.sidebar.success(f"Selamat datang, {name} 👋")


    

    st.markdown("""
    <h1 style="text-align: center; font-size: 2.5em;">🚀 Selamat Datang di <span style="color:#0D9276;">InsightCare AI</span></h1>
    <p style="text-align: center; font-size: 1.1em; color: #555;">
    Pantau data, dapatkan insight AI, dan pantau prediksi.
    </p>
    """, unsafe_allow_html=True)

    st.write("---")

    # Penjelasan fitur
    col1, col2, col3, col4= st.columns(4)

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
    with col4:
        st.markdown("### 📘 Knowledge Management")
        st.write("""
        Kelola dokumen atau laporan pdfmu dengan sistem **Knowledge Management**.  
        Semua file yang diunggah akan di-*embed* dan bisa dijadikan sumber knowledge AI.
        """)

    st.write("---")

    # Guide penggunaan
    st.markdown("""
    ### 🧭 Panduan Singkat
    1. Pilih menu di sebelah kiri untuk berpindah halaman.
    2. Gunakan **Smart Dashboard** untuk melihat data dan insight awal.
    3. Gunakan **Forecasting** untuk memprediksi tren ke depan.
    4. Gunakan **Chat** untuk bertanya langsung ke AI.
    5. Gunakan **Knowledge Management** untuk mengunggah dokumen & membuat basis pengetahuan AI.

    💡 **Tips:**
    - Mulailah dari *Smart Dashboard* agar mendapatkan gambaran umum sebelum masuk ke analisis lebih detail.  
    - Upload dokumen penting ke *Knowledge Management* supaya AI bisa menjawab pertanyaan berdasarkan dokumen kamu.
    """)

elif auth_status is False:
    st.error("Username/password salah")

else:
    # auth_status is None
    st.info("Masukkan username & password untuk masuk.")