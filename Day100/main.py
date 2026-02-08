import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns


# CONFIGURATION ============================================================================
st.set_page_config(
    page_title="Deaths By Police",
    page_icon="🚓",
    layout="wide",
)
pd.options.display.float_format = '{:,.2f}'.format

import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# This might be helpful:
from collections import Counter


# CONFIGURATION ============================================================================
st.set_page_config(
    page_title="Deaths By Police",
    page_icon="🚓",
    layout="wide",
)
pd.options.display.float_format = '{:,.2f}'.format


# HEADER SECTION ============================================================================

st.markdown("<h1 style='text-align: center;'>Deaths by Police in the United States</h1>", unsafe_allow_html=True)


# LOAD DATA  ============================================================================
df_hh_income = pd.read_csv('Median_Household_Income_2015.csv', encoding="windows-1252")
df_pct_poverty = pd.read_csv('Pct_People_Below_Poverty_Level.csv', encoding="windows-1252")
df_pct_completed_hs = pd.read_csv('Pct_Over_25_Completed_High_School.csv', encoding="windows-1252")
df_share_race_city = pd.read_csv('Share_of_Race_By_City.csv', encoding="windows-1252")
df_fatalities = pd.read_csv('Deaths_by_Police_US.csv', encoding="windows-1252")


all_data = [df_hh_income, df_pct_poverty, df_pct_completed_hs,
            df_share_race_city, df_fatalities]


dataframes = {
    "Household Income": df_hh_income,
    "Poverty Rate": df_pct_poverty,
    "High School Completion": df_pct_completed_hs,
    "Race by City": df_share_race_city,
    "Police Fatalities": df_fatalities,
}

# PRELIMINARY DATA EXPLORATION ========================================================================
# *What is the shape of the DataFrames?
# *How many rows and columns do they have?
# *What are the column names?
# *Are there any NaN values or duplicates?


container = st.container(border=True)

col1, col2 = container.columns(2, border=True)

with col1:
    st.image("./assets/police_1.png", caption="police man with baton")

with col2:

    st.write("**What is the shape of df_data?**")

    with st.expander("How many rows and columns does it have?"):
        for name, df in dataframes.items():
            st.write(f"**{name}**: This has {df.shape[0]} rows and {df.shape[1]} columns")