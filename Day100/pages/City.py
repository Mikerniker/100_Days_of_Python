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

state_counts = (
    df_fatalities['state']
    .value_counts()
    .reset_index()
)

state_counts.columns = ['state', 'killings']

top_10_states = state_counts.head(10)

st.write("The most dangerous states (by total police killings):")
st.dataframe(top_10_states)

fig = px.choropleth(
    state_counts,
    locations='state',
    locationmode='USA-states',
    color='killings',
    hover_name='state',
    color_continuous_scale='sunsetdark',
    title='Police Killings by U.S. State'
)

fig.update_layout(
    geo=dict(
        scope='usa',
        showlakes=True,
        lakecolor='rgb(255, 255, 255)'
    ),
    coloraxis_colorbar=dict(
        title='Number of Killings'
    )
)

st.plotly_chart(fig, use_container_width=True)

st.write("**Which states are the most dangerous? Compare your map with your previous chart. "
         "Are these the same states with high degrees of poverty?**")

st.write("States with the most police killings tend to be large, populous states."
         " Arizona, Oklahoma, and Georgia also appear among the "
         "top 10 states with high poverty rates. Several top 10 cities with the most police"
         " killings are within the top most dangerous states. While poverty may play a role, "
         "other factors appear to influence higher police killings.")

# Number of Police Killings Over Time
st.subheader("Number of Police Killings Over Time")

df_fatalities['date'] = pd.to_datetime(df_fatalities['date'], errors='coerce')

df_time = df_fatalities.dropna(subset=['date']).copy()

df_time['YearMonth'] = df_time['date'].dt.to_period('M')

killings_per_month = (
    df_time
    .groupby('YearMonth')
    .size()
    .sort_index()
)

killings_per_month.index = killings_per_month.index.to_timestamp()


fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(
    killings_per_month.index,
    killings_per_month.values,
    label="Monthly Police Killings",
    alpha=0.7
)

ax.set_title("Number of Police Killings Over Time (Monthly)")
ax.set_xlabel("Year")
ax.set_ylabel("Number of Killings")
ax.legend()
ax.grid(alpha=0.3)

st.pyplot(fig)
plt.close()