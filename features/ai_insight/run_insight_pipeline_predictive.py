# features/ai_insight/summary_generator/run_insight_multiple_data.py
from features.ai_insight.summary_generator.generator import df_to_json
from features.ai_insight.prompt.prompt import make_prompt_ai_predictive_faskes_vs_penyakit
from features.ai_insight.llm_model import ask_llm
from features.ai_insight.rag_retriever import retrieve_from_rag


def run_insight_multiple_data(df1, df2, user_query="Analisis faskes vs penyakit"):
    # Convert DF ke JSON
    df1_json = df_to_json(df=df1)
    df2_json = df_to_json(df=df2)

    # Gabungkan jadi context
    context = {
        "forecast faskes": df1_json,
        "forecast penyakit": df2_json,
    }

    # Ambil referensi dari RAG (misalnya WHO ratio, dokumen medis, dll.)
    rag_docs = retrieve_from_rag(user_query, top_k=5)
    rag_context = "\n\n".join([doc.page_content for doc in rag_docs])

    # Buat prompt final
    prompt = make_prompt_ai_predictive_faskes_vs_penyakit(context, rag_context)

    result = ask_llm(prompt)
    
    # Panggil LLM
    return result.content
