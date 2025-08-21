import streamlit as st

def apply_custom_style():
    st.markdown("""
        <style>
        body {
            background-color: #F8FCFB;
        }

        .header-container {
            display: flex;
            align-items: center;
            gap: 20px;
            background: linear-gradient(90deg, #0D9276, #106EBE);
            padding: 15px 25px;
            border-radius: 12px;
            color: white;
            margin-bottom: 25px;
        }
                
        .block-container {
            max-width: 1400px;
            margin: auto;
        }
                
        h1 {
            font-size: 3em !important;
            margin: 0 !important;
        }

        /* Sidebar style */
        [data-testid="stSidebar"] {
            /* background: linear-gradient(to bottom, #0D9276, #106EBE); */
            /* color: white; */
            width: 180px !important;
        }
        
        div[data-testid="stSidebar"] + section.main {
            margin-left: 180px !important;
        }
        
        .stButton > button {
            background-color: #0D9276; /* Hijau BPJS */
            color: white;
            border: none;
            padding: 0.5em 1em;
            font-weight: bold;
            border-radius: 8px;
            transition: background-color 0.3s ease;
            margin-top: 8px;
            margin-bottom: 8px;
            width: 100%;
        }

        .stButton > button:hover {
            background-color: #0b7d66; /* Warna saat hover */
            color: white;
        }
                

        /* Atur container metric */
        [data-testid="stMetric"] {
            background-color: #E6F4F1;
            padding: 6px 10px;
            border-radius: 8px;
            text-align: center;
            min-width: 120px;
        }
        /* Perkecil font label */
        [data-testid="stMetric"] > label {
            font-size: 12px;
        }
        /* Perkecil font value */
        [data-testid="stMetric"] > div > div {
            font-size: 18px;
            font-weight: bold;
        }
        /* Perkecil delta persentase */
        [data-testid="stMetricDelta"] {
            font-size: 4px;
        }
        </style>
    """, unsafe_allow_html=True)