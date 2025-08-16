import plotly.express as px
import json
import pandas as pd

with open("data/geojson/Jabar_By_Kab.geojson", "r", encoding="utf-8") as f:
    geojson = json.load(f)
import streamlit as st

@st.cache_data

def plot_geo_penyakit(df_agg: pd.DataFrame, penyakit_option: str,selected_tahun:int):
    fig = px.choropleth_mapbox(
        df_agg,
        geojson=geojson,
        locations="kode_kabupaten_kota",  # dari df
        featureidkey="properties.ID_KAB",  # dari geojson
        color="Total jumlah penderita",
        hover_name="nama_kabupaten_kota",
        color_continuous_scale=px.colors.sequential.OrRd,
        mapbox_style="carto-positron",
        zoom=7,
        center={"lat": -6.9, "lon": 107.6},
        opacity=0.6,
        title=f"Penyebaran Jumlah Penderita {penyakit_option} di tahun {selected_tahun}"
    )

    fig.update_layout(margin={"r":0,"t":40,"l":0,"b":0})
    return fig