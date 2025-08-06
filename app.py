import streamlit as st
import pandas as pd

st.set_page_config(page_title="Project Coco", layout="wide")
st.title("🛳️ Project Coco: Cruise Suite Tracker")

# Cleaned & balanced sample dataset
data = pd.DataFrame({
    'Departure Port': [
        'Miami', 'Fort Lauderdale', 'Orlando', 'Tampa',
        'Galveston', 'Baltimore', 'New Orleans'
    ],
    'Ship': [
        'Harmony of the Seas', 'Symphony of the Seas', 'Wonder of the Seas',
        'Allure of the Seas', 'Oasis of the Seas', 'Icon of the Seas', 'Utopia of the Seas'
    ],
    'Sailing Date': [
        '2025-09-15', '2025-10-01', '2025-10-20',
        '2025-11-01', '2025-12-01', '2026-01-01', '2026-02-01'
    ],
    'Suite': [
        'Junior Suite', "Owner's Suite", 'Grand Suite',
        'Royal Suite', 'AquaTheater Suite', 'Sky Loft Suite', 'Royal Loft Suite'
    ],
    'Price (USD)': [
        1200, 2400, 3600, 4800, 5200, 12000, 15000
    ]
})

# Convert date column to datetime
data['Sailing Date'] = pd.to_datetime(data['Sailing Date'])

# --- Sidebar Filters ---
st.sidebar.header("🧭 Filter Options")

port_filter = st.sidebar.selectbox("Departure Port", sorted(data['Departure Port'].unique()))
ship_filter = st.sidebar.selectbox("Ship", sorted(data['Ship'].unique()))
suite_filter = st.sidebar.selectbox("Cabin Type", sorted(data['Suite'].unique()))
date_filter = st.sidebar.date_input("Sailing After", value=pd.to_datetime('2025-08-01'))

# --- Filtered Dataset ---
filtered = data[
    (data['Departure Port'] == port_filter) &
    (data['Ship'] == ship_filter) &
    (data['Suite'] == suite_filter) &
    (data['Sailing Date'] >= pd.to_datetime(date_filter))
]

# --- Display Filtered Results ---
st.subheader("📋 Matching Cruise Suites")
if not filtered.empty:
    st.dataframe(filtered, use_container_width=True)

    # --- Show Lowest Price ---
    lowest = filtered.loc[filtered['Price (USD)'].idxmin()]
    st.success(
        f"💰 **Lowest Price:** ${lowest['Price (USD)']} — {lowest['Suite']} on "
        f"**{lowest['Ship']}**, sailing **{lowest['Sailing Date'].date()}** from **{lowest['Departure Port']}**"
    )
else:
    st.warning("🚫 No cruise matches found. Try changing your filters.")



