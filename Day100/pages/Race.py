import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

df_fatalities = pd.read_csv('Deaths_by_Police_US.csv', encoding="windows-1252")
df_share_race_city = pd.read_csv('Share_of_Race_By_City.csv', encoding="windows-1252")

race_fatalities = df_fatalities['race'].value_counts()

race_map = {
    'W': 'White',
    'B': 'Black',
    'A': 'Asian',
    'H': 'Hispanic',
    'N': 'Native American',
    'O': 'Other'
}

race_fatalities.index = race_fatalities.index.map(race_map)

# TO DO
# Create a Bar Chart with Subsections Showing the Racial Makeup of Each US State
# Visualise the share of the white, black, hispanic, asian and native american
# population in each US State using a bar chart with sub sections.

race_label_map = {
    'share_white': 'White',
    'share_black': 'Black',
    'share_native_american': 'Native American',
    'share_asian': 'Asian',
    'share_hispanic': 'Hispanic'
}

st.subheader("Racial Makeup of Each US State")

race_cols = ['share_white', 'share_black', 'share_native_american', 'share_asian', 'share_hispanic']

for col in race_cols:
    df_share_race_city[col] = pd.to_numeric(df_share_race_city[col], errors='coerce')

state_race = (
    df_share_race_city
    .groupby('Geographic area', as_index=False)[race_cols]
    .mean()
)

state_race_renamed = state_race.rename(columns=race_label_map)

fig, ax = plt.subplots(figsize=(14, 7))
state_race_renamed.set_index('Geographic area')[
    list(race_label_map.values())
].plot(
    kind='bar',
    stacked=True,
    ax=ax,
    colormap='tab20'
)


ax.set_title('Racial Makeup by US State', fontsize=16)
ax.set_xlabel('State')
ax.set_ylabel('Percentage (%)')
ax.legend(title='Demographics', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.xticks(rotation=90)
plt.tight_layout()

st.pyplot(fig)  