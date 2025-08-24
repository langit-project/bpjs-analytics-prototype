from features.ai_insight.prompt import prompt
from features.ai_insight.summary_generator import generator



INSIGHT_REGISTRY = {
    "pertumbuhan_peserta_bpjs": {
        "summary_func": generator.df_to_json,
        "prompt_func": prompt.make_ai_prompt_for_trend_pertumbuhan_peserta_bpjs_v2
    },
    "penyebaran_peserta_bpjs": {
        "summary_func": generator.df_to_json,
        "prompt_func": prompt.make_ai_prompt_for_penyebaran_peserta_bpjs
    },
    "jumlah_faskes_berdasarkan_jenis": {
        "summary_func": generator.df_to_json,
        "prompt_func": prompt.make_ai_prompt_faskes_jenis_bar
    },
    "penyebaran_jenis_faskes": {
        "summary_func": generator.df_to_json,
        "prompt_func": prompt.make_ai_prompt_penyebaran_faskes_jenis
    },
    "pertumbuhan_jenis_faskes": {
        "summary_func": generator.df_to_json,
        "prompt_func": prompt.make_ai_prompt_tren_faskes_jenis
    },
    "pertumbuhan_penyakit": {
        "summary_func": generator.df_to_json,
        "prompt_func": prompt.make_ai_prompt_trend_penyakit
    },
    
    "penyebaran_penyakit": {
        "summary_func": generator.df_to_json,
        "prompt_func": prompt.make_ai_prompt_peta_persebaran_penyakit
    },
    "forecast_faskes_vs_penyakit": {
        "summary_func": generator.df_to_json,
        "prompt_func": prompt.make_ai_prompt_peta_persebaran_penyakit
    },
    
    
    # kamu bisa tambahkan "new_customer", "habit_time", dst nanti
}