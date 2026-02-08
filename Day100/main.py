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

    with st.expander("**What are the column names?**"):
        # st.write("**What are the column names?**")
        for name, df in dataframes.items():
            with st.expander(f"{name} columns & preview"):
                st.write(list(df.columns))
                st.dataframe(df.head())

    ## Data Cleaning - Check for Missing Values and Duplicates
    # Consider how to deal with the NaN values. Perhaps substituting 0 is appropriate.
    with st.expander("**Data Cleaning**"):
        for i in range(len(all_data)):
            all_data[i] = all_data[i].fillna(0)

        st.write("**Are there any NaN values or duplicates?**")
        for df in all_data:
            total_nans = df.isna().sum().sum()
            st.write(f"There are {total_nans} missing (NaN) values in the entire DataFrame")

            total_dupes = df.duplicated().sum()
            st.write(f"There are {total_dupes} duplicate rows")

st.markdown("<h2 style='text-align: center;'>Poverty, Education, and Mental Health</h2>", unsafe_allow_html=True)


# Chart the Poverty Rate in each US State
# Create a bar chart that ranks the poverty rate from highest to
# lowest by US state. Which state has the highest poverty rate?
# Which state has the lowest poverty rate?  Bar Plot
  # PRICE AND DOMINANCE OVER TIME
    # ========================================================================
col1, col2 = st.columns(2)

with col1:
    st.subheader("Chart the Poverty Rate in each US State")
    # st.write(f"Chart the Poverty Rate in each US State")

    df_pct_poverty["poverty_rate"] = (
        df_pct_poverty["poverty_rate"]
        .replace("-", np.nan)
        .astype(float)
    )

    poverty_by_state = (
        df_pct_poverty
        .groupby("Geographic Area", as_index=False)
        .agg({"poverty_rate": "mean"})
        .sort_values(by="poverty_rate", ascending=False)
    )