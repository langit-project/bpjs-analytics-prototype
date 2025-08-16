# pages/02_Conversation.py
import streamlit as st
from utils.custom_style import apply_custom_style   # opsional: biar gaya konsisten
from features.ai_insight.insight_conversation import handle_insight_conversation

# Jangan panggil st.set_page_config di halaman ini (panggil hanya sekali di app.py)
apply_custom_style() 

st.title("🤖 Conversation Assistant")

# inisialisasi session state (shared antar halaman)
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Tombol hapus history
if st.session_state.chat_history:
    col1, col2 = st.columns([0.85, 0.15])
    with col2:
        if st.button("🗑️ Hapus Chat"):
            st.session_state.chat_history = []
            st.rerun()  # gunakan st.rerun() (Streamlit versi baru)

# Tampilkan history
for role, message in st.session_state.chat_history:
    # st.chat_message tersedia di Streamlit versi yang mendukung chat UI
    try:
        with st.chat_message(role):
            st.markdown(message)
    except Exception:
        # fallback jika chat_message tidak tersedia
        st.markdown(f"**{role}**: {message}")

st.markdown("---")

# Input baru (chat)
try:
    prompt = st.chat_input("Tulis pertanyaanmu di sini...")
except Exception:
    # fallback kalau chat_input belum ada: gunakan text_input + tombol
    prompt = st.text_input("Tulis pertanyaanmu di sini...")
    send_clicked = st.button("Kirim")
    if not prompt:
        send_clicked = False

if prompt:
    # jika menggunakan fallback text_input, pastikan send_clicked True (di atas)
    if "send_clicked" in locals() and not send_clicked:
        # jangan respon sebelum klik
        pass
    else:
        # simpan user
        st.session_state.chat_history.append(("user", prompt))
        with st.chat_message("user"):
            st.markdown(prompt)

        # proses jawaban
        with st.chat_message("assistant"):
            with st.spinner("🤖 Menganalisis dan menjawab..."):
                answer = handle_insight_conversation(prompt)
                st.markdown(answer)

        st.session_state.chat_history.append(("assistant", answer))
        # optional: langsung rerun agar input kosong lagi
        st.rerun()
