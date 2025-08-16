import plotly.express as px
import json
import pandas as pd

with open("data/geojson/Jabar_By_Kab.geojson", "r", encoding="utf-8") as f:
    geojson = json.load(f)
import streamlit as st

@st.cache_data

def plot_geo_peserta(df_agg: pd.DataFrame,selected_tahun:list[int]):
    fig = px.choropleth_mapbox(
        df_agg,
        geojson=geojson,
        locations="bps_kode_kabupaten_kota",  # dari df
        featureidkey="properties.ID_KAB",  # dari geojson
        color="jumlah_ warga_terdaftar_bpjs",
        hover_name="bps_nama_kabupaten_kota",
        color_continuous_scale=px.colors.sequential.Tealgrn,
        # color_continuous_scale=["#8EEC57", "#4ACE21", "#058D0C"],
        mapbox_style="carto-positron",
        zoom=6,
        center={"lat": -6.9, "lon": 107.6},
        opacity=0.8,
        title=f"Penyebaran peserta BPJS di tahun {str(selected_tahun)}"
    )

    fig.update_layout(margin={"r":0,"t":40,"l":0,"b":0})

    fig.update_geos(fitbounds="locations", visible=False)
    return fig