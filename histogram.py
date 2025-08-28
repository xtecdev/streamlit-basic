import streamlit as st
import numpy as np
import db

data = db.load(10000)

st.header("Number of pickups by hour")
hist_values = np.histogram(data[db.DATE_COLUMN].dt.hour, bins=24, range=(0, 24))[0]
st.bar_chart(hist_values)