import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns


df_fatalities = pd.read_csv('Deaths_by_Police_US.csv', encoding="windows-1252")

race_map = {
    'W': 'White',
    'B': 'Black',
    'A': 'Asian',
    'H': 'Hispanic',
    'N': 'Native American',
    'O': 'Other'
}
# In Which Cities Do the Most Police Killings Take Place?
# Create a chart ranking the top 10 cities with the most police killings.
# Which cities are the most dangerous?


city_counts = (
    df_fatalities['city']
    .value_counts()
    .head(10)
)

st.subheader("Top 10 Cities with the Most Police Killings")
st.bar_chart(city_counts, horizontal=True, sort=False)


top_10_city_names = city_counts.index

top_cities_df = df_fatalities[df_fatalities['city'].isin(top_10_city_names)]

race_dist = (
    top_cities_df
    .groupby(['city', 'race'])
    .size()
    .unstack(fill_value=0)
)

race_dist = race_dist.loc[top_10_city_names]

race_dist = race_dist.rename(columns=race_map)

race_share = race_dist.div(race_dist.sum(axis=1), axis=0) * 100

st.subheader("Rate of Police Killings by Race in the Top 10 Cities")

st.bar_chart(
    race_share,
    stack=True,   # ensure it shows percentages rather than raw counts
    sort=False
)

# Create a Choropleth Map of Police Killings by US State
# Which states are the most dangerous? Compare your map with your previous chart.
# Are these the same states with high degrees of poverty?
st.subheader("Choropleth Map of Police Killings by US State")
