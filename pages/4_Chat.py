# # pages/02_Conversation.py
# import streamlit as st
# from utils.custom_style import apply_custom_style   # opsional: biar gaya konsisten
# from features.ai_insight.insight_conversation import handle_insight_conversation

# # Jangan panggil st.set_page_config di halaman ini (panggil hanya sekali di app.py)
# apply_custom_style() 

# st.title("🤖 Chat")

# # inisialisasi session state (shared antar halaman)
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []

# # Tombol hapus history
# if st.session_state.chat_history:
#     col1, col2 = st.columns([0.85, 0.15])
#     with col2:
#         if st.button("🗑️ Hapus Chat"):
#             st.session_state.chat_history = []
#             st.rerun()  # gunakan st.rerun() (Streamlit versi baru)

# # Tampilkan history
# for role, message in st.session_state.chat_history:
#     # st.chat_message tersedia di Streamlit versi yang mendukung chat UI
#     try:
#         with st.chat_message(role):
#             st.markdown(message)
#     except Exception:
#         # fallback jika chat_message tidak tersedia
#         st.markdown(f"**{role}**: {message}")

# st.markdown("---")

# # Input baru (chat)
# try:
#     prompt = st.chat_input("Tulis pertanyaanmu di sini...")
# except Exception:
#     # fallback kalau chat_input belum ada: gunakan text_input + tombol
#     prompt = st.text_input("Tulis pertanyaanmu di sini...")
#     send_clicked = st.button("Kirim")
#     if not prompt:
#         send_clicked = False

# if prompt:
#     # jika menggunakan fallback text_input, pastikan send_clicked True (di atas)
#     if "send_clicked" in locals() and not send_clicked:
#         # jangan respon sebelum klik
#         pass
#     else:
#         # simpan user
#         st.session_state.chat_history.append(("user", prompt))
#         with st.chat_message("user"):
#             st.markdown(prompt)

#         # proses jawaban
#         with st.chat_message("assistant"):
#             with st.spinner("🤖 Menganalisis dan menjawab..."):
#                 answer = handle_insight_conversation(prompt)
#                 st.markdown(answer)

#         st.session_state.chat_history.append(("assistant", answer))
#         # optional: langsung rerun agar input kosong lagi
#         st.rerun()








# # ================== VERSI MATPLOTLIB===============================
# import streamlit as st
# from utils.custom_style import apply_custom_style
# from features.ai_insight.insight_conversation import handle_insight_conversation
# import matplotlib.pyplot as plt

# # Jangan panggil st.set_page_config di halaman ini
# apply_custom_style()

# st.title("🤖 Chat")

# # inisialisasi session state (shared antar halaman)
# # Menggunakan struktur dictionary untuk membedakan tipe pesan
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []

# # Tombol hapus history
# if st.session_state.chat_history:
#     col1, col2 = st.columns([0.85, 0.15])
#     with col2:
#         if st.button("🗑️ Hapus Chat"):
#             st.session_state.chat_history = []
#             st.rerun()

# # Tampilkan history
# for message in st.session_state.chat_history:
#     try:
#         with st.chat_message(message["role"]):
#             # Cek tipe pesan dan tampilkan
#             if message["type"] == "text":
#                 st.markdown(message["content"])
#             elif message["type"] == "plot":
#                 st.pyplot(message["content"])
#     except Exception as e:
#         # fallback jika chat_message tidak tersedia atau ada error
#         st.markdown(f"**{message['role']}**: {message['content']}")
#         st.error(f"Error rendering plot: {e}")

# st.markdown("---")

# # Input baru (chat)
# prompt = st.chat_input("Tulis pertanyaanmu di sini...")

# if prompt:
#     # simpan prompt user
#     st.session_state.chat_history.append({"role": "user", "content": prompt, "type": "text"})
#     with st.chat_message("user"):
#         st.markdown(prompt)

#     # proses jawaban
#     with st.chat_message("assistant"):
#         with st.spinner("🤖 Menganalisis dan menjawab..."):
#             # Panggil fungsi yang sudah diubah
#             response_data = handle_insight_conversation(prompt)

#             # Tampilkan konten berdasarkan tipenya
#             if response_data["type"] == "text":
#                 st.markdown(response_data["content"])
#             elif response_data["type"] == "plot":
#                 # Tampilkan teks pengantar sebelum plot
#                 st.markdown("Berikut adalah plot yang saya buat:")
#                 st.pyplot(response_data["content"])

#         # Simpan respons ke history
#         st.session_state.chat_history.append({"role": "assistant", "content": response_data["content"], "type": response_data["type"]})
#     st.rerun()

__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import streamlit as st
from utils.custom_style import apply_custom_style
from features.ai_insight.insight_conversation import handle_insight_conversation
import matplotlib.pyplot as plt
import plotly.express as px

# Jangan panggil st.set_page_config di halaman ini
apply_custom_style()

st.title("🤖 Chat")

# inisialisasi session state (shared antar halaman)
# Menggunakan struktur dictionary untuk membedakan tipe pesan
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Tombol hapus history
if st.session_state.chat_history:
    col1, col2 = st.columns([0.85, 0.15])
    with col2:
        if st.button("🗑️ Hapus Chat"):
            st.session_state.chat_history = []
            st.rerun()

# Tampilkan history
for message in st.session_state.chat_history:
    try:
        with st.chat_message(message["role"]):
            # Cek tipe pesan dan tampilkan
            if message["type"] == "text":
                st.markdown(message["content"])
            elif message["type"] == "plot":
                # Menggunakan st.plotly_chart untuk menampilkan objek Plotly
                st.plotly_chart(message["content"])
    except Exception as e:
        # fallback jika chat_message tidak tersedia atau ada error
        st.markdown(f"**{message['role']}**: {message['content']}")
        st.error(f"Error rendering plot: {e}")

st.markdown("---")

# Input baru (chat)
prompt = st.chat_input("Tulis pertanyaanmu di sini...")

if prompt:
    # simpan prompt user
    st.session_state.chat_history.append({"role": "user", "content": prompt, "type": "text"})
    with st.chat_message("user"):
        st.markdown(prompt)

    # proses jawaban
    with st.chat_message("assistant"):
        with st.spinner("🤖 Menganalisis dan menjawab..."):
            # Panggil fungsi yang sudah diubah
            response_data = handle_insight_conversation(prompt)

            # Tampilkan konten berdasarkan tipenya
            if response_data["type"] == "text":
                st.markdown(response_data["content"])
            elif response_data["type"] == "plot":
                # Tampilkan teks pengantar sebelum plot
                st.markdown("Berikut adalah plot yang saya buat:")
                # Menggunakan st.plotly_chart
                st.plotly_chart(response_data["content"])

        # Simpan respons ke history
        st.session_state.chat_history.append({"role": "assistant", "content": response_data["content"], "type": response_data["type"]})
    st.rerun()
