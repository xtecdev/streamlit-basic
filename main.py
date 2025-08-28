import streamlit as st

st.set_page_config(
   page_title="Uber | xtec.dev",
   page_icon="X",
   layout="wide",
   initial_sidebar_state="expanded",
)


home = st.Page("home.py", title="Home", icon="🏠")
histogram = st.Page("histogram.py", title="Histogram", icon="📊")
map = st.Page("map.py", title="Map", icon="🗺️")

# Set up navigation
pg = st.navigation([home, histogram, map])

# Run the selected page
pg.run()
