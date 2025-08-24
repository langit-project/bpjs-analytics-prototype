# features/ai_summary/final_summary.py
import json
import streamlit as st
from langchain_core.prompts import PromptTemplate
from features.ai_insight.llm_model import ask_llm
from core.generator.faskes_jenis.generator_for_summary_faskes_jenis import generate_faskes_jenis_summary
from core.generator.penyakit.generator_for_summary_penyakit import generate_penyakit_summary
from core.generator.peserta_bpjs.generator_for_summary_peserta_bpjs import generate_peserta_bpjs_summary
from features.ai_insight.summary_generator.generator import save_multiple_df_to_tabular_string,df_to_tabular_string,df_to_json
from features.ai_insight.prompt.prompt import make_ai_prompt_healthcare_summary_with_insight
from features.predictive.forecast_trend_jenis_faskes import forecast_trend_faskes_sarimax_ci_summary



def generate_llm_summary():
    # summary = {
    #     "summary kepemilikan faskes": generate_kepemilikan_faskes_summary(),
    #     "summary penderita penyakit": generate_penyakit_summary(),
    #     "summary peserta bpjs": generate_peserta_bpjs_summary()
    # }
    # # Filter hanya insight yang tersedia dan tidak kosong

    # summary = save_multiple_df_to_tabular_string(summary)

    summary_faskes = df_to_json(generate_faskes_jenis_summary())
    summary_penyakit = df_to_json(generate_penyakit_summary())
    summary_bpjs = df_to_json(generate_peserta_bpjs_summary())

    # print(f"🧾 Summary:\n{summary}")
    # return summary

    prompt = make_ai_prompt_healthcare_summary_with_insight(summary_faskes=summary_faskes, summary_penyakit=summary_penyakit,summary_bpjs=summary_bpjs)
    print(f"🧠 Prompt:\n{prompt}")

    result = ask_llm(prompt)
    print(f"📝 LLM Response:\n{result.content}")

    return result.content

def generate_llm_summary_for_conversation():
    df_summary_jenis_faskes = generate_faskes_jenis_summary()
    # ✅ Cek apakah sudah ada hasil forecast di session
    if "forecast_faskes" not in st.session_state:
        st.session_state["forecast_faskes"] = forecast_trend_faskes_sarimax_ci_summary(df_summary_jenis_faskes)
    
    df_forecast = st.session_state["forecast_faskes"]
    # pastikan kolom datetime (Timestamp) diubah ke string
    for col in df_forecast.select_dtypes(include=["datetime", "datetimetz"]).columns:
        df_forecast[col] = df_forecast[col].astype(str)

    summary = {
        "summary jenis faskes": df_summary_jenis_faskes.to_dict(orient="records"),
        "summary penderita penyakit": generate_penyakit_summary().to_dict(orient="records"),
        "summary peserta bpjs": generate_peserta_bpjs_summary().to_dict(orient="records"),
        "summary forecast jenis faskes": df_forecast.to_dict(orient="records")
    }

    return json.dumps(summary, ensure_ascii=False, indent=2)

