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
