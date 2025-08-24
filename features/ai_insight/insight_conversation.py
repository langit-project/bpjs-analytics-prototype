# import streamlit as st
# from features.ai_insight.llm_model import ask_llm
# from features.ai_insight.final_summary import generate_llm_summary_for_conversation

# from features.ai_insight.rag_retriever import retrieve_from_rag


# import os
# from langchain.memory import ConversationBufferMemory
# from langchain.chains import LLMChain
# from langchain.prompts import PromptTemplate
# from langchain_google_genai import ChatGoogleGenerativeAI



# import os
# import json
# import matplotlib.pyplot as plt
# import pandas as pd
# import plotly.express as px



# # Fungsi untuk membuat plot dari data JSON menggunakan Plotly
# def create_plot_from_json(plot_json: str):
#     """
#     Membuat plot dari data yang disediakan LLM dalam format JSON.
#     Mengembalikan objek figure Plotly.
#     """
#     try:
#         data = json.loads(plot_json)
#         df = pd.DataFrame(data["data"])
        
#         fig = None
#         chart_type = data.get("type", "line").lower()
        
#         # Buat grafik Plotly berdasarkan tipe
#         if chart_type == "bar":
#             fig = px.bar(df, x=data["x_axis"], y=data["y_axis"],
#                          title=data.get("title", "Plot Data"),
#                          labels={data["x_axis"]: data.get("x_axis_label", data["x_axis"]),
#                                  data["y_axis"]: data.get("y_axis_label", data["y_axis"])})
#         elif chart_type == "pie":
#             fig = px.pie(df, values=data["y_axis"], names=data["x_axis"],
#                          title=data.get("title", "Plot Data"))
#         else:  # Default ke line chart
#             fig = px.line(df, x=data["x_axis"], y=data["y_axis"],
#                           title=data.get("title", "Plot Data"),
#                           labels={data["x_axis"]: data.get("x_axis_label", data["x_axis"]),
#                                   data["y_axis"]: data.get("y_axis_label", data["y_axis"])})

#         # Atur tata letak tambahan
#         if fig:
#             fig.update_layout(xaxis_title=data.get("x_axis_label", data["x_axis"]),
#                               yaxis_title=data.get("y_axis_label", data["y_axis"]))
            
#         return fig
#     except Exception as e:
#         print(f"Error creating plot: {e}")
#         return None


# # Memory untuk percakapan
# memory = ConversationBufferMemory(
#     memory_key="history",   # wajib: harus sama dengan nama di prompt
#     input_key="input",      # wajib: input user
#     return_messages=True
# )
# # LLM untuk percakapan
# llm = ChatGoogleGenerativeAI(
#     model="gemini-2.0-flash",
#     temperature=0.3,
#     google_api_key=os.getenv("GOOGLE_API_KEY")
# )
# context = generate_llm_summary_for_conversation()




# # # Prompt conversation
# # prompt = PromptTemplate(
# #     input_variables=["history", "input","context"],
# #     template="""

# # Anda adalah asisten data analyst profesional yang membantu pengguna memahami dan mengeksplorasi insight dari dashboard.

# # Peran Anda:
# # - Menjawab pertanyaan berdasarkan insight yang tersedia.
# # - Tidak menjawab pertanyaan yang tidak relevan dengan analisis data bisnis.
# # - Bersikap proaktif: berikan saran, tawarkan bantuan lebih lanjut, atau ajukan pertanyaan lanjutan jika diperlukan.
# # - Gunakan gaya bahasa profesional, sopan, dan komunikatif layaknya rekan analis manusia.
# # - Anda harus bisa membuat plot gambar juga dari data yang ada 
# # - anda juga seorang statistik profesional dengan pengalaman 10 tahun harus bisa memprediksi dengan berbagai metode statistik ataupun machine learning jika disuruh memprediksi



# # Konteks data:
# # {context}

# # Riwayat percakapan:
# # {history}

# # Pertanyaan pengguna:
# # {input}

# # Jawaban:
# # """
# # )


# # Prompt conversation
# # Penting: Tambahkan instruksi untuk menghasilkan JSON
# prompt = PromptTemplate(
#     input_variables=["history", "input", "context"],
#     template="""

# Anda adalah asisten data analyst profesional yang membantu pengguna memahami dan mengeksplorasi insight dari dashboard.

# Peran Anda:
# - Menjawab pertanyaan berdasarkan insight yang tersedia.
# - Tidak menjawab pertanyaan yang tidak relevan dengan analisis data bisnis.
# - Bersikap proaktif: berikan saran, tawarkan bantuan lebih lanjut, atau ajukan pertanyaan lanjutan jika diperlukan.
# - Gunakan gaya bahasa profesional, sopan, dan komunikatif layaknya rekan analis manusia.

# - Jika pengguna meminta plot atau grafik, berikan respons dalam format JSON string yang diawali dan diakhiri dengan tag `<PLOT>`.
# - Format JSON harus memiliki struktur: {{"title": "Judul Plot", "x_axis": "nama_kolom_x", "y_axis": "nama_kolom_y", "x_axis_label": "Label X", "y_axis_label": "Label Y", "data": [{{'Tahun': 2020, 'Nilai': 30}}, {{'Tahun': 2021, 'Nilai': 35}}]}}. Pastikan data yang Anda berikan valid dan sesuai dengan konteks.
# - Jika permintaan tidak terkait plot, berikan respons teks biasa.
# - anda juga seorang statistik profesional dengan pengalaman 10 tahun harus bisa memprediksi dengan berbagai metode statistik ataupun machine learning jika disuruh memprediksi.

# Konteks data:
# {context}

# Riwayat percakapan:
# {history}

# Pertanyaan pengguna:
# {input}

# Jawaban:
# """
# )

# # Conversation chain
# conversation = LLMChain(
#     llm=llm,
#     memory=memory,
#     prompt=prompt,
#     verbose=True
# )


# # def handle_insight_conversation(user_input: str, verbose: bool = True) -> str:
# #     """
# #     Percakapan dengan memory + context data + RAG.
# #     Jika verbose=True, akan menampilkan info debug:
# #     - Dokumen RAG yang diambil
# #     - Full context yang dikirim ke LLM
# #     """
# #     # Ambil konteks dari RAG
# #     rag_docs = retrieve_from_rag(user_input, top_k=10)
# #     rag_text = " ".join([doc.page_content for doc in rag_docs])

# #     if verbose:
# #         print(f"[DEBUG] Retrieved {len(rag_docs)} docs from RAG:")
# #         for i, doc in enumerate(rag_docs):
# #             preview = doc.page_content[:200].replace("\n"," ")
# #             print(f"Doc {i+1}: {preview}...")

# #     # Gabungkan dengan aggregate context
# #     aggregate_context = generate_llm_summary_for_conversation()
# #     full_context = f"{aggregate_context}\n\nRAG Info:\n{rag_text}"

# #     if verbose:
# #         print("===== FULL CONTEXT SENT TO LLM =====")
# #         print(full_context[:1000] + ("..." if len(full_context)>1000 else ""))
# #         print("===================================")

# #     # Prediksi dengan LLM
# #     response = conversation.predict(context=full_context, input=user_input)

# #     if verbose:
# #         print("===== LLM RESPONSE PREVIEW =====")
# #         print(response[:500] + ("..." if len(response)>500 else ""))
# #         print("================================")

# #     return response


# def handle_insight_conversation(user_input: str, verbose: bool = True):
#     """
#     Percakapan dengan memory + context data + RAG.
#     Mengembalikan dictionary dengan tipe konten ('text' atau 'plot') dan kontennya.
#     """
#     # Ambil konteks dari RAG
#     # ... (kode RAG Anda tetap sama)
#     rag_docs = retrieve_from_rag(user_input, top_k=10)
#     rag_text = " ".join([doc.page_content for doc in rag_docs])
#     aggregate_context = generate_llm_summary_for_conversation()
#     full_context = f"{aggregate_context}\n\nRAG Info:\n{rag_text}"

#     # Prediksi dengan LLM
#     response = conversation.predict(context=full_context, input=user_input)

#     # Cek apakah respons mengandung data plot
#     plot_start = response.find('<PLOT>')
#     plot_end = response.find('</PLOT>')

#     if plot_start != -1 and plot_end != -1:
#         plot_json = response[plot_start + len('<PLOT>'):plot_end].strip()
#         plot_figure = create_plot_from_json(plot_json)
        
#         if plot_figure:
#             # Mengembalikan dictionary dengan tipe 'plot' dan objek figure
#             return {"type": "plot", "content": plot_figure}
#         else:
#             # Jika gagal membuat plot, kembalikan respons teks LLM
#             return {"type": "text", "content": "Maaf, saya tidak dapat membuat plot dari data yang ada. " + response}
#     else:
#         # Jika tidak ada tag <PLOT>, kembalikan respons teks
#         return {"type": "text", "content": response}
















# ======================= VERSI BERHASIL MENGGUNAKALAN MATPLOTLIB




# import streamlit as st
# from features.ai_insight.llm_model import ask_llm
# from features.ai_insight.final_summary import generate_llm_summary_for_conversation
# from features.ai_insight.rag_retriever import retrieve_from_rag

# import os
# import json
# import matplotlib.pyplot as plt
# import pandas as pd
# from langchain.memory import ConversationBufferMemory
# from langchain.chains import LLMChain
# from langchain.prompts import PromptTemplate
# from langchain_google_genai import ChatGoogleGenerativeAI

# # Fungsi untuk membuat plot dari data JSON
# def create_plot_from_json(plot_json: str):
#     """
#     Membuat plot dari data yang disediakan LLM dalam format JSON.
#     Mengembalikan objek figure Matplotlib.
#     """
#     try:
#         data = json.loads(plot_json)
#         df = pd.DataFrame(data["data"])
        
#         # Buat figure dan axes
#         fig, ax = plt.subplots()
        
#         chart_type = data.get("type", "line").lower()
        
#         # Buat grafik berdasarkan tipe
#         if chart_type == "bar":
#             ax.bar(df[data["x_axis"]], df[data["y_axis"]])
#         elif chart_type == "pie":
#             # Pie chart tidak menggunakan x_axis dan y_axis seperti bar/line
#             ax.pie(df[data["y_axis"]], labels=df[data["x_axis"]], autopct='%1.1f%%', startangle=90)
#             ax.axis('equal') # Pastikan pie chart berbentuk lingkaran
#         else: # Default ke line chart
#             ax.plot(df[data["x_axis"]], df[data["y_axis"]])
            
#         ax.set_title(data.get("title", "Plot Data"))
#         ax.set_xlabel(data.get("x_axis_label", data["x_axis"]))
#         ax.set_ylabel(data.get("y_axis_label", data["y_axis"]))
        
#         return fig
#     except Exception as e:
#         print(f"Error creating plot: {e}")
#         return None

# # Memory untuk percakapan
# memory = ConversationBufferMemory(
#     memory_key="history",
#     input_key="input",
#     return_messages=True
# )
# # LLM untuk percakapan
# llm = ChatGoogleGenerativeAI(
#     model="gemini-2.0-flash",
#     temperature=0.3,
#     google_api_key=os.getenv("GOOGLE_API_KEY")
# )
# context = generate_llm_summary_for_conversation()

# # Prompt conversation
# # Penting: Tambahkan instruksi untuk menghasilkan JSON
# prompt = PromptTemplate(
#     input_variables=["history", "input", "context"],
#     template="""

# Anda adalah asisten data analyst profesional yang membantu pengguna memahami dan mengeksplorasi insight dari dashboard.

# Peran Anda:
# - Menjawab pertanyaan berdasarkan insight yang tersedia.
# - Tidak menjawab pertanyaan yang tidak relevan dengan analisis data bisnis.
# - Bersikap proaktif: berikan saran, tawarkan bantuan lebih lanjut, atau ajukan pertanyaan lanjutan jika diperlukan.
# - Gunakan gaya bahasa profesional, sopan, dan komunikatif layaknya rekan analis manusia.

# - Jika pengguna meminta plot atau grafik, berikan respons dalam format JSON string yang diawali dan diakhiri dengan tag `<PLOT>`.
# - Format JSON harus memiliki struktur: {{"type": "bar/line/pie", "title": "Judul Plot", "x_axis": "nama_kolom_x", "y_axis": "nama_kolom_y", "x_axis_label": "Label X", "y_axis_label": "Label Y", "data": [{{'Tahun': 2020, 'Nilai': 30}}, {{'Tahun': 2021, 'Nilai': 35}}]}}. Pastikan data yang Anda berikan valid dan sesuai dengan konteks.
# - Jika permintaan tidak terkait plot, berikan respons teks biasa.
# - anda juga seorang statistik profesional dengan pengalaman 10 tahun harus bisa memprediksi dengan berbagai metode statistik ataupun machine learning jika disuruh memprediksi.

# Konteks data:
# {context}

# Riwayat percakapan:
# {history}

# Pertanyaan pengguna:
# {input}

# Jawaban:
# """
# )

# # Conversation chain
# conversation = LLMChain(
#     llm=llm,
#     memory=memory,
#     prompt=prompt,
#     verbose=True
# )

# def handle_insight_conversation(user_input: str, verbose: bool = True):
#     """
#     Percakapan dengan memory + context data + RAG.
#     Mengembalikan dictionary dengan tipe konten ('text' atau 'plot') dan kontennya.
#     """
#     # Ambil konteks dari RAG
#     # ... (kode RAG Anda tetap sama)
#     rag_docs = retrieve_from_rag(user_input, top_k=10)
#     rag_text = " ".join([doc.page_content for doc in rag_docs])
#     aggregate_context = generate_llm_summary_for_conversation()
#     full_context = f"{aggregate_context}\n\nRAG Info:\n{rag_text}"

#     # Prediksi dengan LLM
#     response = conversation.predict(context=full_context, input=user_input)

#     # Cek apakah respons mengandung data plot
#     plot_start = response.find('<PLOT>')
#     plot_end = response.find('</PLOT>')

#     if plot_start != -1 and plot_end != -1:
#         plot_json = response[plot_start + len('<PLOT>'):plot_end].strip()
#         plot_figure = create_plot_from_json(plot_json)
        
#         if plot_figure:
#             # Mengembalikan dictionary dengan tipe 'plot' dan objek figure
#             return {"type": "plot", "content": plot_figure}
#         else:
#             # Jika gagal membuat plot, kembalikan respons teks LLM
#             return {"type": "text", "content": "Maaf, saya tidak dapat membuat plot dari data yang ada. " + response}
#     else:
#         # Jika tidak ada tag <PLOT>, kembalikan respons teks
#         return {"type": "text", "content": response}




import streamlit as st
from features.ai_insight.llm_model import ask_llm
from features.ai_insight.final_summary import generate_llm_summary_for_conversation
from features.ai_insight.rag_retriever import retrieve_from_rag

import os
import json
import matplotlib.pyplot as plt
import pandas as pd
# Import library Plotly
import plotly.express as px
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

# Fungsi untuk membuat plot dari data JSON menggunakan Plotly
def create_plot_from_json(plot_json: str):
    """
    Membuat plot dari data yang disediakan LLM dalam format JSON.
    Mengembalikan objek figure Plotly.
    """
    try:
        data = json.loads(plot_json)
        # LLM hanya menghasilkan satu seri, jadi kita buat DataFrame langsung dari data
        df = pd.DataFrame(data["data"])
        
        fig = None
        chart_type = data.get("type", "line").lower()
        
        # Buat grafik Plotly berdasarkan tipe
        if chart_type == "bar":
            fig = px.bar(df, x=data["x_axis"], y=data["y_axis"],
                         title=data.get("title", "Plot Data"),
                         labels={data["x_axis"]: data.get("x_axis_label", data["x_axis"]),
                                 data["y_axis"]: data.get("y_axis_label", data["y_axis"])})
        elif chart_type == "pie":
            fig = px.pie(df, values=data["y_axis"], names=data["x_axis"],
                         title=data.get("title", "Plot Data"))
        else:  # Default ke line chart
            fig = px.line(df, x=data["x_axis"], y=data["y_axis"],
                          title=data.get("title", "Plot Data"),
                          labels={data["x_axis"]: data.get("x_axis_label", data["x_axis"]),
                                  data["y_axis"]: data.get("y_axis_label", data["y_axis"])})
        
        return fig
    except Exception as e:
        print(f"Error creating plot: {e}")
        return None

# Memory untuk percakapan
memory = ConversationBufferMemory(
    memory_key="history",
    input_key="input",
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
# Penting: Tambahkan instruksi untuk menghasilkan JSON
prompt = PromptTemplate(
    input_variables=["history", "input", "context"],
    template="""

Anda adalah asisten data analyst profesional yang membantu pengguna memahami dan mengeksplorasi insight dari dashboard.

Peran Anda:
- Menjawab pertanyaan berdasarkan insight yang tersedia.
- Tidak menjawab pertanyaan yang tidak relevan dengan analisis data bisnis.
- Bersikap proaktif: berikan saran, tawarkan bantuan lebih lanjut, atau ajukan pertanyaan lanjutan jika diperlukan.
- Gunakan gaya bahasa profesional, sopan, dan komunikatif layaknya rekan analis manusia.

- Jika pengguna meminta plot atau grafik, berikan respons dalam format JSON string yang diawali dan diakhiri dengan tag `<PLOT>`.
- Format JSON harus memiliki struktur: {{"type": "bar/line/pie", "title": "Judul Plot", "x_axis": "nama_kolom_x", "y_axis": "nama_kolom_y", "x_axis_label": "Label X", "y_axis_label": "Label Y", "data": [{{'Tahun': 2020, 'Nilai': 30}}, {{'Tahun': 2021, 'Nilai': 35}}]}}. Pastikan data yang Anda berikan valid dan sesuai dengan konteks.
- Jika permintaan tidak terkait plot, berikan respons teks biasa.
- anda juga seorang statistik profesional dengan pengalaman 10 tahun harus bisa memprediksi dengan berbagai metode statistik ataupun machine learning jika disuruh memprediksi.

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

def handle_insight_conversation(user_input: str, verbose: bool = True):
    """
    Percakapan dengan memory + context data + RAG.
    Mengembalikan dictionary dengan tipe konten ('text' atau 'plot') dan kontennya.
    """
    # Ambil konteks dari RAG
    # ... (kode RAG Anda tetap sama)
    rag_docs = retrieve_from_rag(user_input, top_k=10)
    rag_text = " ".join([doc.page_content for doc in rag_docs])
    aggregate_context = generate_llm_summary_for_conversation()
    full_context = f"{aggregate_context}\n\nRAG Info:\n{rag_text}"

    # Prediksi dengan LLM
    response = conversation.predict(context=full_context, input=user_input)

    # Cek apakah respons mengandung data plot
    plot_start = response.find('<PLOT>')
    plot_end = response.find('</PLOT>')

    if plot_start != -1 and plot_end != -1:
        plot_json = response[plot_start + len('<PLOT>'):plot_end].strip()
        plot_figure = create_plot_from_json(plot_json)
        
        if plot_figure:
            # Mengembalikan dictionary dengan tipe 'plot' dan objek figure
            return {"type": "plot", "content": plot_figure}
        else:
            # Jika gagal membuat plot, kembalikan respons teks LLM
            return {"type": "text", "content": "Maaf, saya tidak dapat membuat plot dari data yang ada. " + response}
    else:
        # Jika tidak ada tag <PLOT>, kembalikan respons teks
        return {"type": "text", "content": response}
