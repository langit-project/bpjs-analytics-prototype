# from langchain.document_loaders import PyPDFLoader
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain_community.vectorstores import Chroma
# from langchain_community.embeddings import OllamaEmbeddings

# # -------- Config --------
# PDF_PATH = "data/pengelolaan dan pencegahan diabetes melitus tipe 2 indonesia.pdf"
# CHROMA_DIR = "./chroma_db" 
# COLLECTION_NAME = "bpjs_pdf_docs" 
# CHUNK_SIZE = 200     # kecil supaya RAM ringan
# CHUNK_OVERLAP = 20 
# BATCH_SIZE = 10


# # -------- Load PDF --------
# loader = PyPDFLoader(PDF_PATH)
# documents = loader.load()


# # -------- Split teks menjadi chunks --------
# splitter = RecursiveCharacterTextSplitter(
#     chunk_size=CHUNK_SIZE,
#     chunk_overlap=CHUNK_OVERLAP
# )
# docs = splitter.split_documents(documents)


# # -------- Init vector DB --------
# embedding_model = OllamaEmbeddings(model="nomic-embed-text")
# vector_db = Chroma(
#     persist_directory=CHROMA_DIR,
#     collection_name=COLLECTION_NAME,
#     embedding_function=embedding_model
# )

# # -------- Batch embedding --------
# for i in range(0, len(docs), BATCH_SIZE):
#     batch_docs = docs[i:i+BATCH_SIZE]
#     vector_db.add_documents(batch_docs)
#     vector_db.persist()
#     print(f"[✅] Embedded batch {i}-{i+len(batch_docs)}")

# print(f"[🎉] Selesai embedding {len(docs)} chunk PDF ke Chroma DB")




# ============== use huggingface=========

# from langchain.document_loaders import PyPDFLoader

# #  ingest_and_embed.py
# from langchain_community.document_loaders import PyPDFLoader
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain_community.vectorstores import Chroma
# from langchain_community.embeddings import HuggingFaceEmbeddings

# # -------- Config --------
# # PDF_PATH = "data/pengelolaan dan pencegahan diabetes melitus tipe 2 indonesia.pdf"
# PDF_PATH = r"C:\Users\ASUS\Desktop\prototype_dashboard_v1\data\Buku Pedoman Hipertensi 2024.pdf"

# CHROMA_DIR = "./chroma_db_hf"   # folder baru untuk HuggingFace
# COLLECTION_NAME = "bpjs_pdf_docs"
# CHUNK_SIZE = 200     # kecil supaya RAM ringan
# CHUNK_OVERLAP = 20
# BATCH_SIZE = 10

# # -------- Load PDF --------
# loader = PyPDFLoader(PDF_PATH)
# documents = loader.load()

# # -------- Split teks menjadi chunks --------
# splitter = RecursiveCharacterTextSplitter(
#     chunk_size=CHUNK_SIZE,
#     chunk_overlap=CHUNK_OVERLAP
# )
# docs = splitter.split_documents(documents)

# # -------- Init vector DB --------
# embedding_model = HuggingFaceEmbeddings(
#     model_name="sentence-transformers/all-MiniLM-L6-v2"  # ringan & bagus untuk prototipe
# )
# vector_db = Chroma(
#     persist_directory=CHROMA_DIR,
#     collection_name=COLLECTION_NAME,
#     embedding_function=embedding_model
# )

# # -------- Batch embedding --------
# for i in range(0, len(docs), BATCH_SIZE):
#     batch_docs = docs[i:i+BATCH_SIZE]
#     vector_db.add_documents(batch_docs)
#     vector_db.persist()
#     print(f"[✅] Embedded batch {i}-{i+len(batch_docs)}")

# print(f"[🎉] Selesai embedding {len(docs)} chunk PDF ke Chroma DB (HuggingFace)")


# features/ingest/ingest_and_embed.py
# features/ai_insight/ingest_and_embed.py
import os
import uuid
from datetime import datetime
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

# -------- Config --------
CHROMA_DIR = "./chroma_db_hf"
COLLECTION_NAME = "bpjs_pdf_docs"

# Init embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Init vector DB
vector_db = Chroma(
    persist_directory=CHROMA_DIR,
    collection_name=COLLECTION_NAME,
    embedding_function=embedding_model
)

# -------- Fungsi --------
# def embed_pdf(file_path: str):
#     """Load PDF, chunk, embed, simpan ke Chroma"""
#     loader = PyPDFLoader(file_path)
#     documents = loader.load()

#     splitter = RecursiveCharacterTextSplitter(
#         chunk_size=500,
#         chunk_overlap=100
#     )
#     docs = splitter.split_documents(documents)

#     # buat ID unik untuk file
#     doc_id = str(uuid.uuid4())
#     uploaded_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#     for d in docs:
#         d.metadata["doc_id"] = doc_id
#         d.metadata["source"] = os.path.basename(file_path)
#         d.metadata["uploaded_at"] = uploaded_at

#     vector_db.add_documents(docs)
#     vector_db.persist()

#     return {
#         "doc_id": doc_id,
#         "file_name": os.path.basename(file_path),
#         "chunks": len(docs),
#         "uploaded_at": uploaded_at
#     }

# features/ingest/ingest_and_embed.py
# import os
# import uuid
# from datetime import datetime
# from langchain_community.text_splitter import RecursiveCharacterTextSplitter
# from langchain_community.vectorstores import Chroma
# from langchain_community.embeddings import HuggingFaceEmbeddings


# -------- Fungsi --------
def embed_pdf(file_path: str):
    """Load PDF (auto detect loader), chunk, embed, simpan ke Chroma"""
    documents = []

    try:
        # 1. Coba pakai PyMuPDFLoader (paling stabil & cepat)
        from langchain_community.document_loaders import PyMuPDFLoader
        loader = PyMuPDFLoader(file_path)
        documents = loader.load()
        print(f"[INFO] Dibaca dengan PyMuPDFLoader: {len(documents)} halaman")
    except Exception as e1:
        print(f"[WARN] PyMuPDFLoader gagal: {e1}")
        try:
            # 2. Fallback ke PyPDFLoader
            from langchain_community.document_loaders import PyPDFLoader
            loader = PyPDFLoader(file_path)
            documents = loader.load()
            print(f"[INFO] Dibaca dengan PyPDFLoader: {len(documents)} halaman")
        except Exception as e2:
            raise RuntimeError(f"Gagal membaca PDF {file_path}: {e2}")

    # 3. Split dokumen jadi chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    docs = splitter.split_documents(documents)

    # 4. Tambahkan metadata unik
    doc_id = str(uuid.uuid4())
    uploaded_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for d in docs:
        d.metadata["doc_id"] = doc_id
        d.metadata["source"] = os.path.basename(file_path)
        d.metadata["uploaded_at"] = uploaded_at

    # 5. Masukkan ke Vector DB
    vector_db.add_documents(docs)
    vector_db.persist()

    return {
        "doc_id": doc_id,
        "file_name": os.path.basename(file_path),
        "chunks": len(docs),
        "uploaded_at": uploaded_at
    }

def delete_doc(doc_id: str):
    """Hapus knowledge berdasarkan doc_id"""
    vector_db.delete(where={"doc_id": doc_id})
    vector_db.persist()
    return True


def list_docs():
    """Ambil daftar knowledge unik"""
    all_docs = vector_db.get(include=["metadatas"])
    metadatas = all_docs["metadatas"]

    unique_docs = {}
    for m in metadatas:
        doc_id = m.get("doc_id")
        if doc_id and doc_id not in unique_docs:
            unique_docs[doc_id] = {
                "doc_id": doc_id,
                "file_name": m.get("source"),
                "uploaded_at": m.get("uploaded_at"),
            }
    return list(unique_docs.values())
