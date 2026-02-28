import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

df_fatalities = pd.read_csv('Deaths_by_Police_US.csv', encoding="windows-1252")
df_share_race_city = pd.read_csv('Share_of_Race_By_City.csv', encoding="windows-1252")