import streamlit as st
import pandas as pd

st.title("Project Coco: Cruise Suite Tracker")

# Sample DataFrame — replace with real scraped data
data = pd.DataFrame({
    'Departure Port': ['Miami', 'Fort Lauderdale', 'Orlando’, 'Tampa', ‘Galveston’, ‘Baltimore’, ‘New Orleans’, ‘San Juan’, ‘Ravenna’, ‘Rome’, ‘Barcelona’, ‘Los Angeles’, ‘Hong Kong’, ‘Singapore’, ‘Athens’, ‘Colon’, ‘Boston’, ‘Cape Liberty’, ‘Seattle’, ‘Southampton’, ‘Sydney’, ‘Venice’, ‘Oahu’, ‘Tokyo’, San Diego’, ‘Lisbon’, ‘Cartagena’,  ],
    'Ship': ['Harmony of the Seas', 'Symphony of the Seas', 'Wonder of the Seas', ‘Quantum of the Seas’, ‘Allure of the Seas’, ‘Freedom of the Seas’, ‘Oasis of the Seas’, ‘Odyssey of the Seas’, ‘Anthem of the Seas’, ‘Jewel of the Seas’, ‘Liberty of the Seas’, ‘Independence of the Seas’, ‘Ovation of the Seas’, ‘Icon of the Seas’, ‘Mariner of the Seas’, ‘Spectrum of the Seas’, ‘Utopia of the Seas’, ‘Brilliance of the Seas’, ‘Serenade of the Seas’, ‘Legend of the Seas’, ‘Star of the Seas’, ‘Explorer of the Seas’, ‘Grandeur of the Seas’, ‘Navigator of the Seas’, Adventure of the Seas’, ‘Enchantment of the Seas’, ‘Radiance of the Seas’, ‘Voyager of the Seas’, Rhapsody of the Seas’],
    'Sailing Date': ['2025-09-15', '2025-10-01', '2025-10-20', '2025-11-01'],
    'Suite': ['Junior Suite', 'Owner’s Suite', 'Junior Suite', 'Royal Loft'],
    'Price (USD)': [4800, 12000, 4500, 15000]
})

# Convert date column to datetime
data['Sailing Date'] = pd.to_datetime(data['Sailing Date'])

# Sidebar Filters
st.sidebar.header("🧭 Filter Options")

port_filter = st.sidebar.selectbox("Select Departure Port", options=sorted(data['Departure Port'].unique()))
ship_filter = st.sidebar.selectbox("Select Ship", options=sorted(data['Ship'].unique()))
suite_filter = st.sidebar.selectbox("Select Cabin Type", options=sorted(data['Suite'].unique()))
date_filter = st.sidebar.date_input("Sailing After", value=pd.to_datetime('2025-08-01'))

# Apply filters
filtered = data[
    (data['Departure Port'] == port_filter) &
    (data['Ship'] == ship_filter) &
    (data['Suite'] == suite_filter) &
    (data['Sailing Date'] >= pd.to_datetime(date_filter))
]

# Display results
st.subheader("🎟️ Available Suites")
st.dataframe(filtered, use_container_width=True)

# Show lowest price in this filtered set
if not filtered.empty:
    lowest = filtered.loc[filtered['Price (USD)'].idxmin()]
    st.success(f"💰 Lowest Price: **${lowest['Price (USD)']}** for {lowest['Suite']} on **{lowest['Ship']}**, departing **{lowest['Sailing Date'].date()}** from {lowest['Departure Port']}")
else:
    st.warning("🚫 No matching cruises found. Try different filters.")

