import streamlit as st
import pandas as pd
import plotly.express as px

df_fatalities = pd.read_csv('Deaths_by_Police_US.csv', encoding="windows-1252")

# TO DO
# Create a Chart Comparing the Total Number of Deaths of Men and Women
# Use `df_fatalities` to illustrate how many more men are killed compared to women.

col1, col2 = st.columns(2)
with col1:
    gender_fatalities = df_fatalities['gender'].value_counts()

    gender_map = {
        'M': 'Men',
        'F': 'Women',
    }