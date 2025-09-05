import altair as alt
import numpy as np
import pandas as pd
import polars as pl
import streamlit as st

st.set_page_config(
    page_title="Uber | xtec.dev",
    page_icon="𝚾",
    layout="wide",
    initial_sidebar_state="expanded",
)

DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')


@st.cache_data
def load_data(n_rows):
    return pl.read_csv(DATA_URL, n_rows=n_rows, try_parse_dates=True)


st.header("Uber pickups in NYC")

df = load_data(10000)

if st.checkbox("Show raw data"):
    st.subheader("Raw data")
    st.write(df)

hist_tab, map_tab = st.tabs(["Histogram", "Map"])

with hist_tab:
    st.subheader("Number of pickups by hour")
    df = df.with_columns(pl.col("Date/Time").dt.hour().alias("hour"))
    st.altair_chart(alt.Chart(df).mark_bar().encode(
        x="hour",
        y="count()"
    ))

with map_tab:
    st.subheader("Map of all pickups")
    hour_to_filter = st.slider("hour", 0, 23, 17)  # min: 0h, max: 23h, default: 17h
    df = df.filter(pl.col("Date/Time").dt.hour() == hour_to_filter)
    st.text(f'Map of all pickups at {hour_to_filter}:00')

    df = df.rename({"Lat": "latitude", "Lon": "longitude"})
    st.map(df)
