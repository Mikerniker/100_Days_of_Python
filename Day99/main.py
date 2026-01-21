import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import seaborn as sns

# from iso3166 import countries
from datetime import datetime, timedelta


# CONFIGURATION ============================================================================
st.set_page_config(
    page_title="Space Race",
    page_icon="🚀",
    layout="wide",
)
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


USSR_COUNTRIES = ["Russian Federation", "Kazakhstan"]
USA_COUNTRIES = ["United States", "USA"]
FAILURE_STATUSES = ["Failure", "Partial Failure", "Prelaunch Failure"]
COLD_WAR_END_YEAR = 1991

COLOR_MAP_BLOCS = {"USA": "#3F9AAE", "USSR": "#F96E5B"}
COLOR_MAP_MISSIONS = {
    "Success": "#6AECE1",
    "Failure": "#F96E5B",
    "Partial Failure": "#FFE2AF",
    "Prelaunch Failure": "#FF986A"
}

# LOAD DATA
# ============================================================================
# Banner Section
st.image("spacerace2.png", caption="Rocket Ships", width="stretch")

st.markdown("<h1 style='text-align: center;'>The Space Race 1957-2020</h1>", unsafe_allow_html=True)


uploaded_file = "mission_launches.csv"

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # PRELIMINARY DATA EXPLORATION ========================================================================
    
    col1, col2 = st.columns(2)

    with col1:
        st.header("Preliminary Data Exploration")
        with st.expander("See Preliminary Data"):

            st.write("**What is the shape of df_data?**")
            st.write(df.shape)

            st.write("**How many rows and columns does it have?**")
            st.write(f"It has {df.shape[0]} rows and {df.shape[1]} columns")

            st.write("**What are the column names?**")
            st.write(", ".join(df.columns))

            st.write("**Are there any NaN values or duplicates?**")
            total_nans = df.isna().sum().sum()
            st.write(f"There are {total_nans} missing (NaN) values in the entire DataFrame")

            total_dupes = df.duplicated().sum()
            st.write(f"There are {total_dupes} duplicate rows")

  # DATA CLEANING ========================================================================

    # st.subheader("Data Cleaning - Check for Missing Values and Duplicates")
    with col2:
        st.header("Data Cleaning")
        with st.expander("What Data is Missing"):
            st.write("**Check for Missing Values and Duplicates**")
            # Remove rows with missing values
            clean_df = df.dropna()
            # Remove junk columns
            df_new = clean_df.drop(columns=["Unnamed: 0.1", "Unnamed: 0"])

            st.write(
                "Notes: Use 'dropna' to remove missing values (ex. NaN, None, or NaT) and "
                "remove columns containing junk data."
            )
            st.dataframe(df_new.head())

            code = '''clean_df = df.dropna()
    df_new = clean_df.drop(columns=["Unnamed: 0.1", "Unnamed: 0"])
    df_new.head()'''
            st.code(code, language="python")


 # DATA PREPARATION========================================================================

    # Convert dates 
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce", utc=True)
    df["Year"] = df["Date"].dt.year
    df["Month"] = df["Date"].dt.month
    df["Month_Name"] = df["Date"].dt.month_name()
    df["YearMonth"] = df["Date"].dt.to_period("M")

    # Extract and fix country names 
    df["Country"] = df["Location"].str.split(",").str[-1].str.strip()
    df["Country"] = df["Country"].replace(COUNTRY_FIXES)

    # Convert dates and clean price for df_new
    df_new["Date"] = pd.to_datetime(df_new["Date"], errors="coerce", utc=True)
    df_new["Year"] = df_new["Date"].dt.year
    df_new["Price"] = pd.to_numeric(
        df_new["Price"].astype(str).str.replace(",", "", regex=False),
        errors="coerce"
    )

 # DESCRIPTIVE STATISTICS ========================================================================

    col1, col2 = st.columns(2)

    with col1:
        st.header("Descriptive Statistics")
        with st.expander("Data Overview"):

            st.write("**Data Overview**")
            st.write(df_new.describe())


        # LAUNCH PRICE DISTRIBUTION
        # ========================================================================
    with col2:
        st.header("How Expensive are the Launches?")

        with st.expander("Histogram and visualised distribution"):
            st.write("The price column is given in USD millions.")
            st.write(df_new["Price"].describe())


            price_data = df_new["Price"].dropna()

            # Create histogram
            fig, ax = plt.subplots(figsize=(8, 4), dpi=200)
            ax.hist(price_data, edgecolor="black", bins=50)
            ax.set_xlim(0, 300)
            ax.set_xlabel("Launch Price (USD Millions)")
            ax.set_ylabel("Number of Launches")
            ax.set_title("Distribution of Launch Prices")
            st.pyplot(fig)
            plt.close()

            st.write(
                "The majority of launches cost below \\$300M. "
                "A small number of extremely expensive missions (up to \\$5B) "
                "skew the full distribution, so the x-axis is limited to better "
                "visualize typical launch costs."
            )

   # ACTIVE VS RETIRED ROCKETS ========================================================================
    
    st.header("Number of Active versus Retired Rockets")
    st.write("How many rockets are active compared to those that are decommissioned?")

    # Optional outer container
    container = st.container(border=True)

    with container:
        col1, col2, col3 = st.columns(3, border=True)

        # -------- LEFT COLUMN: Overall Rockets --------
        with col1:
            st.image("rocketships.png", caption="Rocket", width=300)

        # -------- RIGHT COLUMN: Total Rockets --------
        with col2:
            st.subheader("Total Rockets")

            total_rockets = (
                df["Rocket_Status"]
                .value_counts()
                .sort_index()
            )

            st.dataframe(total_rockets, use_container_width=True)

        with col3:
            st.subheader("Total Rockets (Bar Chart)")
            st.bar_chart(total_rockets)


        # ===================== ROW 2: Rockets per Org  =====================
        # CONTINUE GITHUB HERE
        col4, col5 = st.columns([1, 3], border=True)
        with col4:
            # tile_right = st.container(border=True)
            st.subheader("Rockets per Organisation")

            rockets_by_organization = (
                df
                .groupby("Organisation")["Rocket_Status"]
                .value_counts()
                .unstack(fill_value=0)
            )

            st.dataframe(rockets_by_organization.head(), use_container_width=True)

        with col5:
            st.subheader("Rockets per Organisation (Bar Chart)")
            st.bar_chart(rockets_by_organization)

    # NUMBER OF LAUNCHES PER ORG
    # ========================================================================
        container.subheader("Number of Launches per Organization")
        st.write("**Chart for Number of Space Mission launches by Organisation**")

        launch_counts = df.groupby("Organisation").size().sort_values()
        st.bar_chart(launch_counts)

    # MISSION STATUS DISTRIBUTION
    # ========================================================================
    st.subheader("Distribution of Mission Status")

    container = st.container(border=True)

    with container:
        col1, col2 = st.columns(2, border=True)

        # -------- LEFT COLUMN: Overall Rockets --------
        with col1:
            st.subheader("Overall Mission Status")

            mission_status = df["Mission_Status"].value_counts()
            st.dataframe(mission_status)

        # -------- RIGHT COLUMN: Rockets per Organisation --------
        with col2:
            st.subheader("Overall Mission Status")

            st.bar_chart(mission_status)

        # NEXT CONTAINER ROW
        container.write("**Mission Status per Organization**")
        mission_status_org = (
            df.groupby("Organisation")["Mission_Status"]
            .value_counts()
            .unstack(fill_value=0)
        )
        container.bar_chart(mission_status_org)

   # CHOROPLETH MAPS
    # ========================================================================
    st.header("Choropleth Maps")

    col1, col2 = st.columns(2)

    with col1:
        # Count launches per country
        launches_by_country = (
            df.groupby("Country")
            .size()
            .reset_index(name="Launch_Count")
        )

        # Create choropleth map
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
        # Filter failed missions
        failed_df = df[df["Mission_Status"].isin(FAILURE_STATUSES)]

        # Count failures by country
        failures_by_country = (
            failed_df.groupby("Country")
            .size()
            .reset_index(name="Failure_Count")
        )

        # Create choropleth map
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

    # SUNBURST CHART AND LINE CHART
    # ========================================================================
    col1, col2 = st.columns(2)

    with col1:
        st.header("Sunburst Chart")

        # Create sunburst data
        sunburst_df = (
            df.groupby(["Country", "Organisation", "Mission_Status"])
            .size()
            .reset_index(name="Count")
        )

        fig = px.sunburst(
            sunburst_df,
            path=["Country", "Organisation", "Mission_Status"],
            values="Count",
            color="Mission_Status",
            title="Mission Outcomes by Country and Organisation",
            color_discrete_map=COLOR_MAP_MISSIONS
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.header("Line Chart")

        # Chart launches per year
        launches_per_year = df.groupby("Year").size()

        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(launches_per_year.index, launches_per_year.values, linewidth=2)
        ax.set_xlabel("Year")
        ax.set_ylabel("Number of Launches")
        ax.set_title("Number of Space Launches per Year")
        st.pyplot(fig)
        plt.close()

    # SPENDING ANALYSIS ========================================================================
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Total Money Spent per Organisation")

        total_spend = (
            df_new.groupby("Organisation")["Price"]
            .sum()
            .sort_values(ascending=False)
        )
        total_formatted = total_spend.apply(lambda x: f"${x:,.2f}M")

        st.write("Top Ten")
        st.dataframe(
            total_formatted.head(10).rename("Total Spend (USD Millions)")
        )





#         total_nans = df.isna().sum().sum()
#         st.write(f"There are {total_nans} missing (NaN) values in the entire DataFrame")
    
#     st.subheader("**Data Cleaning - Check for Missing Values and Duplicates**")
  
#     with st.expander("What Data is Missing"):
#         clean_df = df.dropna()
#         #clean_df.columns  # to get column names
#         df_new = clean_df.drop(columns=["Unnamed: 0.1", "Unnamed: 0"])

#         st.write(f"Notes Use 'dropna' to remove missing values (ex. NaN, None, or NaT) and"
#                  f" remove columns containing junk data. ")

#         st.dataframe(df_new.head())
    
#         code = '''clean_df = df.dropna()
# clean_df.columns  #to get column names
# df_new = clean_df.drop(columns=["Unnamed: 0.1", "Unnamed: 0"])
# df_new.head()'''
#         st.code(code, language="python")

#     st.subheader("Descriptive Statistics")
    
#     with st.expander("Data Overview"):
#         st.write(df_new.describe())
#         df_new["Price"] = pd.to_numeric(
#             df_new["Price"].astype(str).str.replace(",", "", regex=False),
#             errors="coerce"
#         )
#         st.write(df_new["Price"].describe())

#     st.subheader("Number of Launches per Company")
#     with st.expander("Chart for Number of Space Mission launches by Organisation."):
#         launch_counts = (
#             df.groupby("Organisation")
#             .size()
#             .sort_values()
#         )
#         st.bar_chart(launch_counts)

#     st.subheader("Number of Active versus Retired Rockets ")
#     with st.expander("How many rockets are active compared to those that are decommissioned?"):
#         st.write("**Overall Rockets**")
#         total_rockets = df["Rocket_Status"].value_counts().sort_index()

#         st.write(total_rockets)
#         st.bar_chart(total_rockets)
    
#         st.write("**Rockets per organisation**")
#         rockets_by_organization = df.groupby("Organisation")["Rocket_Status"].value_counts().unstack(fill_value=0)
#         st.write(rockets_by_organization)
#         st.bar_chart(rockets_by_organization)

#     st.subheader("Distribution of Mission Status")
#     with st.expander("How many missions were successful? How many missions failed?"):
#         st.write("**Overall Mission Status**")
#         mission_status = df["Mission_Status"].value_counts()

#         st.write(mission_status)
#         st.bar_chart(mission_status)

#         st.write("**Mission Status per Organization**")
#         mission_status_org = (
#             df.groupby("Organisation")["Mission_Status"]
#             .value_counts()
#             .unstack(fill_value=0)
#         )

#         st.bar_chart(mission_status_org)
    
    

#     st.subheader("**How Expensive are the Launches?**")
#     with st.expander("Histogram and visualised distribution."):
#         st.write("The price column is given in USD millions.")
#         st.write(df_new["Price"].describe())
#         price_data = df_new["Price"].dropna()

#         # Create histogram
#         plt.figure(figsize=(8, 4), dpi=200)
#         plt.hist(price_data,  edgecolor="black", bins=50)
#         plt.xlim(0, 300)
#         plt.xlabel("Launch Price (USD Millions)")
#         plt.ylabel("Number of Launches")
#         plt.title("Distribution of Launch Prices")
#         st.pyplot(plt)

#         st.write(
#             "The majority of launches cost below \\$300M. "
#             "A small number of extremely expensive missions (up to \\$5B) "
#             "skew the full distribution, so the x-axis is limited to better "
#             "visualize typical launch costs."
#         )


# col1, col2 = st.columns(2)
# st.header("Choropleth Maps")

# with col1:   
#     # Extract the country from Location
#     df["Country"] = (
#         df_new["Location"]
#         .str.split(",")
#         .str[-1]
#         .str.strip()
#     )

#     # Fix Country Names
#     country_fixes = {
#         "Russia": "Russian Federation",
#         "New Mexico": "United States",
#         "Yellow Sea": "China",
#         "Shahrud Missile Test Site": "Iran",
#         "Pacific Missile Range Facility": "United States",
#         "Barents Sea": "Russian Federation",
#         "Gran Canaria": "United States"
#     }
#     df["Country"] = df["Country"].replace(country_fixes)
    
#     # Count launches per country
#     launches_by_country = (
#         df
#         .groupby("Country")
#         .size()
#         .reset_index(name="Launch_Count")
#     )

#         # Create Choropleth Map
#     fig = px.choropleth(
#         launches_by_country,
#         locations="Country",
#         locationmode="country names",
#         color="Launch_Count",
#         hover_name="Country",
#         color_continuous_scale="blugrn",
#         title="Number of Launches by Country"
#     )
    
#     fig.update_layout(
#         geo=dict(showframe=False, showcoastlines=True),
#         coloraxis_colorbar=dict(title="Launches")
#     )

#     st.plotly_chart(fig, use_container_width=True)


# with col2:
#    #Failed Launches by country
#     failed_df = df[
#         df["Mission_Status"].isin([
#             "Failure",
#             "Partial Failure",
#             "Prelaunch Failure"
#         ])
#     ]

#     # Count Failures by Country
#     failures_by_country = (
#         failed_df
#         .groupby("Country")
#         .size()
#         .reset_index(name="Failure_Count")
#     )

#     fig = px.choropleth(
#     failures_by_country,
#     locations="Country",
#     locationmode="country names",
#     color="Failure_Count",
#     hover_name="Country",
#     color_continuous_scale="matter",
#     title="Number of Failed Launches by Country"
#     )

#     fig.update_layout(
#     geo=dict(showframe=False, showcoastlines=True),
#     coloraxis_colorbar=dict(title="Failed Launches")
# )
#     st.plotly_chart(fig, use_container_width=True)
#     st.write("This choropleth includes Failure, Partial Failure, and Prelaunch Failure")

# ## Create a Plotly Sunburst Chart of the countries, organisations, and mission status.

# col1, col2 = st.columns(2)

# with col1:
#     sunburst_df = (
#         df
#         .groupby(["Country", "Organisation", "Mission_Status"])
#         .size()
#         .reset_index(name="Count")
#     )

#     fig = px.sunburst(
#         sunburst_df,
#         path=["Country", "Organisation", "Mission_Status"],
#         values="Count",
#         color="Mission_Status",
#         title="Mission Outcomes by Country and Organisation",
#         color_discrete_map={
#             "Success": "#6AECE1",
#             "Failure": "#F96E5B",
#             "Partial Failure": "#FFE2AF",
#             "Prelaunch Failure": "#FF986A"
#         }
#     )
#     st.header("Sunburst Chart")
#     st.plotly_chart(fig, use_container_width=True)

    
# with col2:
#     # Chart the Number of Launches per Year
#     df["Date"] = pd.to_datetime(df["Date"], errors="coerce", utc=True)
   
#     df["Year"] = df["Date"].dt.year

#     launches_per_year = (
#         df
#         .groupby("Year")
#         .size()
#     )

#         plt.figure(figsize=(10, 5))

#     plt.plot(
#         launches_per_year.index,
#         launches_per_year.values,
#         linewidth=2
#     )

#     plt.xlabel("Year")
#     plt.ylabel("Number of Launches")
#     plt.title("Number of Space Launches per Year")
#     st.header("Line Chart")
#     st.pyplot(plt)


# col1, col2 = st.columns(2)

# with col1:
#         ## Analyse the Total Amount of Money Spent by Organisation on Space Missions
#     st.subheader("Total Money Spent per Organisation")

#     total_spend = (
#         df_new
#         .groupby('Organisation')['Price']
#         .sum()
#         .sort_values(ascending=False)
#     )
#     total_formatted = total_spend.apply(lambda x: f"${x:,.2f}M")
    
#     st.write("Top Ten")
#     st.dataframe(
#         total_formatted.head(10).rename("Total Spend (USD Millions)")
#     )

# with col2:
#     #Average Spend per Launch by Organisation
#     avg_spend_per_launch = (
#         df_new
#         .groupby("Organisation")["Price"]
#         .mean()
#         .sort_values(ascending=False)
#     )
#     avg_spend_formatted = avg_spend_per_launch.apply(
#         lambda x: f"${x:,.2f}M per launch"
#     )
#     st.subheader("Average Spend per Launch by Organisation")
#     st.write("All Organizations")

#     st.dataframe(
#         avg_spend_formatted.rename("Average Launch Cost")
#     )
