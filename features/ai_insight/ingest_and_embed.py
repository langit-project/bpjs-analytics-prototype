from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings

# -------- Config --------
PDF_PATH = "data/pengelolaan dan pencegahan diabetes melitus tipe 2 indonesia.pdf"
CHROMA_DIR = "./chroma_db"
COLLECTION_NAME = "bpjs_pdf_docs" 
CHUNK_SIZE = 200     # kecil supaya RAM ringan
CHUNK_OVERLAP = 20
BATCH_SIZE = 10

# -------- Load PDF --------
loader = PyPDFLoader(PDF_PATH)
documents = loader.load()

# -------- Split teks menjadi chunks --------
splitter = RecursiveCharacterTextSplitter(
    chunk_size=CHUNK_SIZE,
    chunk_overlap=CHUNK_OVERLAP
)
docs = splitter.split_documents(documents)

# -------- Init vector DB --------
embedding_model = OllamaEmbeddings(model="nomic-embed-text")
vector_db = Chroma(
    persist_directory=CHROMA_DIR,
    collection_name=COLLECTION_NAME,
    embedding_function=embedding_model
)

# -------- Batch embedding --------
for i in range(0, len(docs), BATCH_SIZE):
    batch_docs = docs[i:i+BATCH_SIZE]
    vector_db.add_documents(batch_docs)
    vector_db.persist()
    print(f"[✅] Embedded batch {i}-{i+len(batch_docs)}")

print(f"[🎉] Selesai embedding {len(docs)} chunk PDF ke Chroma DB")
