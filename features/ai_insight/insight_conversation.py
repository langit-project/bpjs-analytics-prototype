from features.ai_insight.llm_model import ask_llm
from features.ai_insight.final_summary import generate_llm_summary_for_conversation



def handle_insight_conversation(user_input: str) -> str:
    """
    Fungsi untuk menjawab pertanyaan user berdasarkan semua insight yang sudah dihasilkan.
    """

    context = generate_llm_summary_for_conversation()
    prompt = f"""
Anda adalah asisten data analyst profesional yang membantu pengguna memahami dan mengeksplorasi insight dari dashboard.

Peran Anda:
- Menjawab pertanyaan berdasarkan insight yang tersedia.
- Tidak menjawab pertanyaan yang tidak relevan dengan analisis data bisnis.
- Bersikap proaktif: berikan saran, tawarkan bantuan lebih lanjut, atau ajukan pertanyaan lanjutan jika diperlukan.
- Gunakan gaya bahasa profesional, sopan, dan komunikatif layaknya rekan analis manusia.

# Insight Tersedia:
{context}

# Pertanyaan Pengguna:
{user_input}

# Balasan:
"""

    response = ask_llm(prompt)
    return response.content

# def handle_insight_conversation(user_input: str, all_insight_context: str) -> str:
#     """
#     Fungsi untuk menjawab pertanyaan user berdasarkan semua insight yang sudah dihasilkan.
#     """
#     prompt = f"""
# Anda adalah asisten data analyst profesional yang membantu pengguna memahami dan mengeksplorasi insight dari dashboard.

# Peran Anda:
# - Menjawab pertanyaan berdasarkan insight/ data yang tersedia.
# - Tidak menjawab pertanyaan yang tidak relevan dengan analisis data bisnis.
# - Bersikap proaktif: berikan saran, tawarkan bantuan lebih lanjut, atau ajukan pertanyaan lanjutan jika diperlukan.
# - Gunakan gaya bahasa profesional, sopan, dan komunikatif layaknya rekan analis manusia.

# # Insight Tersedia:
# {all_insight_context}

# # Pertanyaan Pengguna:
# {user_input}

# # Balasan:
# """

#     response = ask_llm(prompt)
#     return response.content
