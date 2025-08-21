from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings

def load_bpjs_rag():
    embedding_model = OllamaEmbeddings(model="nomic-embed-text")
    return Chroma(
        persist_directory="./chroma_db",
        collection_name="bpjs_pdf_docs",
        embedding_function=embedding_model
    )

def retrieve_from_rag(query, top_k=10):
    vector_db = load_bpjs_rag()
    docs = vector_db.similarity_search(query, k=top_k)
    return docs
