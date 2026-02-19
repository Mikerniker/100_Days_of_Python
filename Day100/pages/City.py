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
