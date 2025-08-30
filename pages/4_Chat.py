# pages/02_chat.py

import streamlit as st
from utils.custom_style import apply_custom_style
from features.ai_insight.insight_conversation import handle_insight_conversation
# from features.ai_insight.rag_retriever import load_bpjs_rag   # 🔥 tambahkan import ini

import plotly.express as px

# auth_guard
from utils.auth_guard import require_login
name = require_login()

# Jangan panggil st.set_page_config di halaman ini
apply_custom_style()

st.title("🤖 Chat")
st.caption("Ngobrol dengan asisten AI kamu. Tanyakan tentang data, insight, atau apapun 🚀")
st.markdown("---")

# Inisialisasi session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Fungsi tambah pesan
def add_message(role, content, type="text"):
    st.session_state.chat_history.append({"role": role, "content": content, "type": type})
    with st.chat_message(role):
        if type == "text":
            st.markdown(content)
        elif type == "plot":
            st.plotly_chart(content)

# Suggestion list
suggestions = [
    "analisis Peserta BPJS setiap Kabupaten/kota",
    "analisis Penderita Dabetes setiap Kabupaten/Kota",
    "analisis Jumlah Faskes setiap Kabupaten/Kota",
]


   

# === Jika belum ada chat, tampilkan halaman welcome ===
if len(st.session_state.chat_history) == 0:
    st.markdown(
        """
        <div style="text-align: center; padding: 50px 20px; color: #555;">
            <div style="font-size: 40px; margin-bottom: 20px;">💬</div>
            <h3>Mulai percakapan</h3>
            <p>Tidak ada chat yang tampil. Tanyakan apa pun terkait klaim, prediksi, atau data kesehatan Anda, 
            atau gunakan salah satu saran di bawah.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    # Suggestion card (horizontal)
    cols = st.columns(len(suggestions))
    for i, s in enumerate(suggestions):
        if cols[i].button(s):
            add_message("user", s, "text")
            with st.chat_message("assistant"):
                with st.spinner("🤖 Menganalisis dan menjawab..."):
                    response_data = handle_insight_conversation(s)
                    add_message("assistant", response_data["content"], response_data["type"])
            st.rerun()

else:
    # Tombol hapus history
    col1, col2 = st.columns([0.85, 0.15])
    with col2:
        if st.button("🗑️ Hapus Chat"):
            st.session_state.chat_history = []
            st.rerun()

    # Tampilkan history
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            if message["type"] == "text":
                st.markdown(message["content"])
            elif message["type"] == "plot":
                st.plotly_chart(message["content"])

# Input manual (chat_input tetap di bawah)
if prompt := st.chat_input("Tulis pertanyaanmu di sini..."):
    add_message("user", prompt, "text")
    with st.chat_message("assistant"):
        with st.spinner("🤖 Menganalisis dan menjawab..."):
            response_data = handle_insight_conversation(prompt)
            add_message("assistant", response_data["content"], response_data["type"])
    st.rerun()
