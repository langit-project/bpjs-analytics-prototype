# utils/auth_guard.py
import streamlit as st

def require_login():
    auth_status = st.session_state.get("authentication_status")
    name = st.session_state.get("name")

    if not auth_status:
        # sembunyikan sidebar
        st.markdown(
            """
            <style>
            [data-testid="stSidebar"] {display: none;}
            [data-testid="stSidebarNav"] {display: none;}
            </style>
            """,
            unsafe_allow_html=True,
        )
        st.warning("⚠️ Silakan login dulu di halaman utama.")
        st.stop()  # hentikan eksekusi page ini

    return name
