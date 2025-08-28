import streamlit as st

home = st.Page("home.py", title="Home", icon="🏠")
histogram = st.Page("histogram.py", title="Histogram", icon="📊")
map = st.Page("map.py", title="Map", icon="🗺️")

# Set up navigation
pg = st.navigation([home, histogram, map])

# Run the selected page
pg.run()
