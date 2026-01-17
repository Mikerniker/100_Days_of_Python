import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import seaborn as sns

# from iso3166 import countries
from datetime import datetime, timedelta


# CONFIGURATION ============================================================================
st.set_page_config(layout="wide")
pd.options.display.float_format = '{:,.2f}'.format


# CONSTANTS ============================================================================
COUNTRY_FIXES = {
    "Russia": "Russian Federation",
    "New Mexico": "United States",
    "Yellow Sea": "China",
    "Shahrud Missile Test Site": "Iran",
    "Pacific Missile Range Facility": "United States",
    "Barents Sea": "Russian Federation",
    "Gran Canaria": "United States"
}

st.title("Mission Launches")

uploaded_file = "mission_launches.csv"

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("Preliminary Data Exploration")

    with st.expander("See Preliminary Data"):

        st.write("**What is the shape of `df_data`?**")
        st.write(df.shape)

        st.write("**How many rows and columns does it have?**")

        st.write("It has 4324 rows and 9 columns")

        st.write("**What are the column names?**")
        st.write(", ".join(df.columns))

        st.write("**Are there any NaN values or duplicates?**")
        # st.write(df.isna())

        total_nans = df.isna().sum().sum()
        st.write(f"There are {total_nans} missing (NaN) values in the entire DataFrame")
    
    st.subheader("**Data Cleaning - Check for Missing Values and Duplicates**")
  
    with st.expander("What Data is Missing"):
        clean_df = df.dropna()
        #clean_df.columns  # to get column names
        df_new = clean_df.drop(columns=["Unnamed: 0.1", "Unnamed: 0"])

        st.write(f"Notes Use 'dropna' to remove missing values (ex. NaN, None, or NaT) and"
                 f" remove columns containing junk data. ")

        st.dataframe(df_new.head())
    
        code = '''clean_df = df.dropna()
clean_df.columns  #to get column names
df_new = clean_df.drop(columns=["Unnamed: 0.1", "Unnamed: 0"])
df_new.head()'''
        st.code(code, language="python")

    st.subheader("Descriptive Statistics")
    
    with st.expander("Data Overview"):
        st.write(df_new.describe())
        df_new["Price"] = pd.to_numeric(
            df_new["Price"].astype(str).str.replace(",", "", regex=False),
            errors="coerce"
        )
        st.write(df_new["Price"].describe())

    st.subheader("Number of Launches per Company")
    with st.expander("Chart for Number of Space Mission launches by Organisation."):
        launch_counts = (
            df.groupby("Organisation")
            .size()
            .sort_values()
        )
        st.bar_chart(launch_counts)

    st.subheader("Number of Active versus Retired Rockets ")
    with st.expander("How many rockets are active compared to those that are decommissioned?"):
        st.write("**Overall Rockets**")
        total_rockets = df["Rocket_Status"].value_counts().sort_index()

        st.write(total_rockets)
        st.bar_chart(total_rockets)
    
        st.write("**Rockets per organisation**")
        rockets_by_organization = df.groupby("Organisation")["Rocket_Status"].value_counts().unstack(fill_value=0)
        st.write(rockets_by_organization)
        st.bar_chart(rockets_by_organization)

    st.subheader("Distribution of Mission Status")
    with st.expander("How many missions were successful? How many missions failed?"):
        st.write("**Overall Mission Status**")
        mission_status = df["Mission_Status"].value_counts()

        st.write(mission_status)
        st.bar_chart(mission_status)

        st.write("**Mission Status per Organization**")
        mission_status_org = (
            df.groupby("Organisation")["Mission_Status"]
            .value_counts()
            .unstack(fill_value=0)
        )

        st.bar_chart(mission_status_org)
    
    

    st.subheader("**How Expensive are the Launches?**")
    with st.expander("Histogram and visualised distribution."):
        st.write("The price column is given in USD millions.")
        st.write(df_new["Price"].describe())
        price_data = df_new["Price"].dropna()

        # Create histogram
        plt.figure(figsize=(8, 4), dpi=200)
        plt.hist(price_data,  edgecolor="black", bins=50)
        plt.xlim(0, 300)
        plt.xlabel("Launch Price (USD Millions)")
        plt.ylabel("Number of Launches")
        plt.title("Distribution of Launch Prices")
        st.pyplot(plt)

        st.write(
            "The majority of launches cost below \\$300M. "
            "A small number of extremely expensive missions (up to \\$5B) "
            "skew the full distribution, so the x-axis is limited to better "
            "visualize typical launch costs."
        )


col1, col2 = st.columns(2)
st.header("Choropleth Maps")

with col1:   
    # Extract the country from Location
    df["Country"] = (
        df_new["Location"]
        .str.split(",")
        .str[-1]
        .str.strip()
    )

    # Fix Country Names
    country_fixes = {
        "Russia": "Russian Federation",
        "New Mexico": "United States",
        "Yellow Sea": "China",
        "Shahrud Missile Test Site": "Iran",
        "Pacific Missile Range Facility": "United States",
        "Barents Sea": "Russian Federation",
        "Gran Canaria": "United States"
    }
    df["Country"] = df["Country"].replace(country_fixes)
    
    # Count launches per country
    launches_by_country = (
        df
        .groupby("Country")
        .size()
        .reset_index(name="Launch_Count")
    )

        # Create Choropleth Map
    fig = px.choropleth(
        launches_by_country,
        locations="Country",
        locationmode="country names",
        color="Launch_Count",
        hover_name="Country",
        color_continuous_scale="blugrn",
        title="Number of Launches by Country"
    )
    
    fig.update_layout(
        geo=dict(showframe=False, showcoastlines=True),
        coloraxis_colorbar=dict(title="Launches")
    )

    st.plotly_chart(fig, use_container_width=True)


with col2:
   #Failed Launches by country
    failed_df = df[
        df["Mission_Status"].isin([
            "Failure",
            "Partial Failure",
            "Prelaunch Failure"
        ])
    ]

    # Count Failures by Country
    failures_by_country = (
        failed_df
        .groupby("Country")
        .size()
        .reset_index(name="Failure_Count")
    )

    fig = px.choropleth(
    failures_by_country,
    locations="Country",
    locationmode="country names",
    color="Failure_Count",
    hover_name="Country",
    color_continuous_scale="matter",
    title="Number of Failed Launches by Country"
    )

    fig.update_layout(
    geo=dict(showframe=False, showcoastlines=True),
    coloraxis_colorbar=dict(title="Failed Launches")
)
    st.plotly_chart(fig, use_container_width=True)
    st.write("This choropleth includes Failure, Partial Failure, and Prelaunch Failure")

## Create a Plotly Sunburst Chart of the countries, organisations, and mission status.

col1, col2 = st.columns(2)

with col1:
    sunburst_df = (
        df
        .groupby(["Country", "Organisation", "Mission_Status"])
        .size()
        .reset_index(name="Count")
    )

    fig = px.sunburst(
        sunburst_df,
        path=["Country", "Organisation", "Mission_Status"],
        values="Count",
        color="Mission_Status",
        title="Mission Outcomes by Country and Organisation",
        color_discrete_map={
            "Success": "#6AECE1",
            "Failure": "#F96E5B",
            "Partial Failure": "#FFE2AF",
            "Prelaunch Failure": "#FF986A"
        }
    )
    st.header("Sunburst Chart")
    st.plotly_chart(fig, use_container_width=True)

    
with col2:
    # Chart the Number of Launches per Year
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce", utc=True)
   
    df["Year"] = df["Date"].dt.year

    launches_per_year = (
        df
        .groupby("Year")
        .size()
    )

        plt.figure(figsize=(10, 5))

    plt.plot(
        launches_per_year.index,
        launches_per_year.values,
        linewidth=2
    )

    plt.xlabel("Year")
    plt.ylabel("Number of Launches")
    plt.title("Number of Space Launches per Year")
    st.header("Line Chart")
    st.pyplot(plt)


col1, col2 = st.columns(2)

with col1:
        ## Analyse the Total Amount of Money Spent by Organisation on Space Missions
    st.subheader("Total Money Spent per Organisation")

    total_spend = (
        df_new
        .groupby('Organisation')['Price']
        .sum()
        .sort_values(ascending=False)
    )
    total_formatted = total_spend.apply(lambda x: f"${x:,.2f}M")
    
    st.write("Top Ten")
    st.dataframe(
        total_formatted.head(10).rename("Total Spend (USD Millions)")
    )

with col2:
    #Average Spend per Launch by Organisation
    avg_spend_per_launch = (
        df_new
        .groupby("Organisation")["Price"]
        .mean()
        .sort_values(ascending=False)
    )
    avg_spend_formatted = avg_spend_per_launch.apply(
        lambda x: f"${x:,.2f}M per launch"
    )
    st.subheader("Average Spend per Launch by Organisation")
    st.write("All Organizations")

    st.dataframe(
        avg_spend_formatted.rename("Average Launch Cost")
    )
