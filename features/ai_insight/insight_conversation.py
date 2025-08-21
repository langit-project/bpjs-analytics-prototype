import streamlit as st
from features.ai_insight.llm_model import ask_llm
from features.ai_insight.final_summary import generate_llm_summary_for_conversation

from features.ai_insight.rag_retriever import retrieve_from_rag


import os
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

# Memory untuk percakapan
memory = ConversationBufferMemory(
    memory_key="history",   # wajib: harus sama dengan nama di prompt
    input_key="input",      # wajib: input user
    return_messages=True
)
# LLM untuk percakapan
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.3,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)
context = generate_llm_summary_for_conversation()
# Prompt conversation
prompt = PromptTemplate(
    input_variables=["history", "input","context"],
    template="""

Anda adalah asisten data analyst profesional yang membantu pengguna memahami dan mengeksplorasi insight dari dashboard.

Peran Anda:
- Menjawab pertanyaan berdasarkan insight yang tersedia.
- Tidak menjawab pertanyaan yang tidak relevan dengan analisis data bisnis.
- Bersikap proaktif: berikan saran, tawarkan bantuan lebih lanjut, atau ajukan pertanyaan lanjutan jika diperlukan.
- Gunakan gaya bahasa profesional, sopan, dan komunikatif layaknya rekan analis manusia.

Konteks data:
{context}

Riwayat percakapan:
{history}

Pertanyaan pengguna:
{input}

Jawaban:
"""
)

# Conversation chain
conversation = LLMChain(
    llm=llm,
    memory=memory,
    prompt=prompt,
    verbose=True
)

# def handle_insight_conversation(user_input: str) -> str:
#     """
#     Percakapan dengan memory + context data.
#     """
#     response = conversation.predict(context=context, input=user_input)
#     return response


####################################################

# def handle_insight_conversation(user_input: str) -> str:
#     """
#     Percakapan dengan memory + context data + RAG.
#     """
#     # Ambil konteks dari RAG
#     rag_docs = retrieve_from_rag(user_input, top_k=3)
#     rag_text = " ".join([doc.page_content for doc in rag_docs])

#     # Gabungkan dengan aggregate context
#     full_context = f"{generate_llm_summary_for_conversation()}\n\nRAG Info:\n{rag_text}"

#     # Prediksi dengan LLM
#     response = conversation.predict(context=full_context, input=user_input)
#     return response

def handle_insight_conversation(user_input: str, verbose: bool = True) -> str:
    """
    Percakapan dengan memory + context data + RAG.
    Jika verbose=True, akan menampilkan info debug:
    - Dokumen RAG yang diambil
    - Full context yang dikirim ke LLM
    """
    # Ambil konteks dari RAG
    rag_docs = retrieve_from_rag(user_input, top_k=10)
    rag_text = " ".join([doc.page_content for doc in rag_docs])

    if verbose:
        print(f"[DEBUG] Retrieved {len(rag_docs)} docs from RAG:")
        for i, doc in enumerate(rag_docs):
            preview = doc.page_content[:200].replace("\n"," ")
            print(f"Doc {i+1}: {preview}...")

    # Gabungkan dengan aggregate context
    aggregate_context = generate_llm_summary_for_conversation()
    full_context = f"{aggregate_context}\n\nRAG Info:\n{rag_text}"

    if verbose:
        print("===== FULL CONTEXT SENT TO LLM =====")
        print(full_context[:1000] + ("..." if len(full_context)>1000 else ""))
        print("===================================")

    # Prediksi dengan LLM
    response = conversation.predict(context=full_context, input=user_input)

    if verbose:
        print("===== LLM RESPONSE PREVIEW =====")
        print(response[:500] + ("..." if len(response)>500 else ""))
        print("================================")

    return response