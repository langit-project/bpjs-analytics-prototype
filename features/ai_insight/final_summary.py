# features/ai_summary/final_summary.py
import json

from langchain_core.prompts import PromptTemplate
from features.ai_insight.llm_model import ask_llm
from core.generator.faskes_jenis.generator_for_summary_faskes_jenis import generate_faskes_jenis_summary
from core.generator.penyakit.generator_for_summary_penyakit import generate_penyakit_summary
from core.generator.peserta_bpjs.generator_for_summary_peserta_bpjs import generate_peserta_bpjs_summary
from features.ai_insight.summary_generator.generator import save_multiple_df_to_tabular_string,df_to_tabular_string,df_to_json
from features.ai_insight.prompt.prompt import make_ai_prompt_healthcare_summary_with_insight

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
    summary = {
        "summary jenis faskes": generate_faskes_jenis_summary().to_dict(orient="records"),
        "summary penderita penyakit": generate_penyakit_summary().to_dict(orient="records"),
        "summary peserta bpjs": generate_peserta_bpjs_summary().to_dict(orient="records")
    }
    # Filter hanya insight yang tersedia dan tidak kosong

    return json.dumps(summary, ensure_ascii=False, indent=2)
