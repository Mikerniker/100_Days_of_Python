import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import seaborn as sns

# from iso3166 import countries
from datetime import datetime, timedelta


pd.options.display.float_format = '{:,.2f}'.format

st.title("Mission Launches")

uploaded_file = "mission_launches.csv"

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("Preliminary Data Exploration")
    st.write("**What is the shape of `df_data`?**")
    st.write(df.shape)

    st.write("**How many rows and columns does it have?**")

    st.write("It has 4324 rows and 9 columns")

    st.write("**What are the column names?**")
    st.write(df.columns)

    st.write("**Are there any NaN values or duplicates?**")
    # st.write(df.isna())

    total_nans = df.isna().sum().sum()
    st.write(f"There are {total_nans} missing (NaN) values in the entire DataFrame")