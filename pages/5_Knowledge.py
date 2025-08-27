# pages/Knowledge_Management.py
import streamlit as st
import pandas as pd
import os, shutil
from features.ai_insight.ingest_and_embed import embed_pdf, delete_doc, list_docs
from utils.custom_style import apply_custom_style


apply_custom_style()

st.title("📘 Knowledge Management")

UPLOAD_DIR = "./uploaded_pdfs"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

# ===== Upload PDF =====
uploaded_file = st.file_uploader("Upload PDF untuk dijadikan knowledge", type=["pdf"])

if uploaded_file is not None:
    file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
    with open(file_path, "wb") as f:
        shutil.copyfileobj(uploaded_file, f)

    if st.button("🚀 Proses & Simpan ke Knowledge Base"):
        with st.spinner("Embedding & simpan ke Chroma..."):
            result = embed_pdf(file_path)
        st.success(
            f"✅ {result['file_name']} berhasil di-embed "
            f"({result['chunks']} chunks) | DocID: {result['doc_id']}"
        )

st.divider()

# ===== Daftar Knowledge =====
st.subheader("📂 Knowledge Base Saat Ini")

docs = list_docs()
if docs:
    df = pd.DataFrame(docs)
    st.dataframe(df, use_container_width=True)

   # tombol hapus langsung per baris (versi dengan border)
for doc in docs:
    with st.container():
        st.markdown(
            """
            <div style="
                border: 1px solid #ddd;
                border-radius: 10px;
                padding: 10px;
                margin-bottom: 10px;
                background-color: #f9f9f9;">
            """,
            unsafe_allow_html=True
        )

        col1, col2, col3 = st.columns([3, 3, 1])
        with col1:
            st.write(f"📄 **{doc['file_name']}**")
        with col2:
            st.write(f"🆔 `{doc['doc_id']}`")
        with col3:
            if st.button("🗑️ Hapus", key=doc["doc_id"]):
                delete_doc(doc["doc_id"])
                st.success(f"Knowledge {doc['file_name']} berhasil dihapus")
                st.experimental_rerun()

        st.markdown("</div>", unsafe_allow_html=True)


