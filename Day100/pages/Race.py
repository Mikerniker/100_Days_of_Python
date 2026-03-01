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