from .insight_registry import INSIGHT_REGISTRY
from .llm_model import ask_llm

from typing import Literal


def run_insight_pipeline(df, insight_type: Literal["pertumbuhan_peserta_bpjs", "penyebaran_peserta_bpjs","jumlah_faskes_berdasarkan_jenis", "pertumbuhan_jenis_faskes","penyebaran_jenis_faskes","pertumbuhan_penyakit","penyebaran_penyakit"]):
    config = INSIGHT_REGISTRY.get(insight_type)
    if not config:
        raise ValueError(f"Insight type '{insight_type}' belum didukung.")
    
    # print(f"📊 Memulai pipeline insight: {insight_type}")
    # print(f"📄 Dataframe: {df.head()}")

    summary = config["summary_func"](df)
    # print(f"🧾 Summary:\n{summary}")

    prompt = config["prompt_func"](summary)
    # print(f"🧠 Prompt:\n{prompt}")

    result = ask_llm(prompt)
    # print(f"📝 LLM Response:\n{result.content}")

    return result.content


# =========yang menggunakan RAG

# from .insight_registry import INSIGHT_REGISTRY
# from .llm_model import ask_llm
# from rag.retriever import retrieve_documents  # <- pastikan sudah ada
# from typing import Literal


# def run_insight_pipeline(
#     df, 
#     insight_type: Literal["sales", "new_customer", "describe_rfm", "segment_by_category", "habit_time_transaction","sales_forecast"]
# ):
#     config = INSIGHT_REGISTRY.get(insight_type)
#     if not config:
#         raise ValueError(f"Insight type '{insight_type}' belum didukung.")
    
#     print(f"📊 Memulai pipeline insight: {insight_type}")
#     # print(f"📄 Dataframe: {df.head()}")

#     summary = config["summary_func"](df)
#     print(f"🧾 Summary:\n{summary}")

#     # ✅ Tambahkan query map per insight
#     query_map = {
#         "sales": "strategi peningkatan penjualan",
#         "sales_forecast":"strategi analisis forecasting",
#         "new_customer": "strategi akuisisi pelanggan baru",
#         "describe_rfm": "strategi berdasarkan RFM dan segmentasi pelanggan",
#         "segment_by_category": "strategi marketing per kategori dan segmen",
#         "habit_time_transaction": "strategi kampanye waktu dan perilaku konsumen"
#     }

#     query = query_map.get(insight_type, insight_type)
#     rag_docs = retrieve_documents(query)
#     rag_text = "\n".join([doc.page_content for doc in rag_docs])
#     print(f"📚 Dokumen dari RAG (potongan):\n{rag_text[:300]}")

#     # Gabungkan summary + rag_text
#     combined_summary = summary
#     if rag_text.strip():
#         combined_summary += f"\n\n📚 Referensi Strategi:\n{rag_text}"

#     prompt = config["prompt_func"](combined_summary)
#     print(f"🧠 Prompt:\n{prompt}")

#     result = ask_llm(prompt)
#     print(f"📝 LLM Response:\n{result.content}")

#     return result.content
