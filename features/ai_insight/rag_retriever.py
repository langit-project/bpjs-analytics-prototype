# from langchain_community.vectorstores import Chroma
# from langchain_community.embeddings import OllamaEmbeddings

# def load_bpjs_rag():
#     embedding_model = OllamaEmbeddings(model="nomic-embed-text")
#     return Chroma(
#         persist_directory="./chroma_db",
#         collection_name="bpjs_pdf_docs",
#         embedding_function=embedding_model
#     )

# def retrieve_from_rag(query, top_k=10):
#     vector_db = load_bpjs_rag()
#     docs = vector_db.similarity_search(query, k=top_k)
#     return docs



# ===========huggingface
# features/ai_insight/rag_retriever.py
# from langchain_community.vectorstores import Chroma
# from langchain_community.embeddings import HuggingFaceEmbeddings
# import streamlit as st


# def load_bpjs_rag():
#     embedding_model = HuggingFaceEmbeddings(
#         model_name="sentence-transformers/all-MiniLM-L6-v2"
#     )
#     return Chroma(
#         persist_directory="chroma_db_hf",   # samain sama waktu embedding
#         collection_name="bpjs_pdf_docs",
#         embedding_function=embedding_model
#     )

# def retrieve_from_rag(query, top_k=10):
#     # vector_db = load_bpjs_rag()
#     # docs = vector_db.similarity_search(query, k=top_k)
#     # return docs
#     # 🔥 Ambil retriever dari session_state kalau ada
#     if "vector_db" not in st.session_state:
#         st.session_state["vector_db"] = load_bpjs_rag()
#     vector_db = st.session_state["vector_db"]
#     docs = vector_db.similarity_search(query, k=top_k)
#     return docs



# =========versi 29/08

# features/ai_insight/rag_retriever.py
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
import streamlit as st

def load_bpjs_rag():
    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    return Chroma(
        persist_directory="chroma_db_hf",
        collection_name="bpjs_pdf_docs",
        embedding_function=embedding_model
    )

def retrieve_from_rag(query, top_k=10):
    if "vector_db" not in st.session_state:
        st.session_state["vector_db"] = load_bpjs_rag()
    docs = st.session_state["vector_db"].similarity_search(query, k=top_k)
    return docs
