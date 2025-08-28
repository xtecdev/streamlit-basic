import streamlit as st
import db

st.header("Uber pickups in NYC")

data_load_state = st.text('Loading data...')
data = db.load(10000)
data_load_state.text('Loading data... Done!')

if st.checkbox("Show raw data"):
    st.subheader("Raw data")
    st.write(data)
























