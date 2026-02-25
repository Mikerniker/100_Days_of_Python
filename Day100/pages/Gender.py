import streamlit as st
import pandas as pd
import plotly.express as px

df_fatalities = pd.read_csv('Deaths_by_Police_US.csv', encoding="windows-1252")
