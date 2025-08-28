import streamlit as st
import db

st.header("Map of all pickups")

data = db.load(10000)

hour_to_filter = st.slider("hour", 0, 23, 17)  # min: 0h, max: 23h, default: 17h
filtered_data = data[data[db.DATE_COLUMN].dt.hour == hour_to_filter]
st.text(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)