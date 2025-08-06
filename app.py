# Streamlit dashboard entry point

import streamlit as st
st.title("Project Coco: Cruise Suite Tracker")
import streamlit as st
import pandas as pd

st.title("Project Coco: Cruise Suite Tracker")

# Sample DataFrame — replace with real data or scraper output
data = pd.DataFrame({
    'Ship': ['Harmony of the Seas', 'Symphony of the Seas', 'Wonder of the Seas'],
    'Sailing Date': ['2025-09-15', '2025-10-01', '2025-10-20'],
    'Suite': ['Royal Loft', 'Owner’s Suite', 'AquaTheater Suite'],
    'Price (USD)': [15000, 12000, 13500]
})

# Filters
ship_filter = st.selectbox("Select Ship", options=data['Ship'].unique())
date_filter = st.date_input("Sailing After", value=pd.to_datetime('2025-08-01'))

# Filtered results
filtered = data[
    (data['Ship'] == ship_filter) &
    (pd.to_datetime(data['Sailing Date']) >= pd.to_datetime(date_filter))
]

st.subheader("Available Suites")
st.dataframe(filtered)
