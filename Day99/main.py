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

    with col2:
        st.subheader("Average Spend per Launch by Organisation")

        avg_spend_per_launch = (
            df_new.groupby("Organisation")["Price"]
            .mean()
            .sort_values(ascending=False)
        )

        avg_spend_formatted = avg_spend_per_launch.apply(
            lambda x: f"${x:,.2f}M per launch"
        )

        st.write("All Organizations")
        st.dataframe(
            avg_spend_formatted.rename("Average Launch Cost")
        )

    # MONTHLY LAUNCH ANALYSIS ========================================================================
    col1, col2 = st.columns(2)

    with col1:
        # Monthly launches over time with rolling average
        launches_per_month = (
            df.dropna(subset=["Date"])
            .groupby("YearMonth")
            .size()
            .sort_index()
        )
        launches_per_month.index = launches_per_month.index.to_timestamp()

        # Calculate rolling average
        rolling_avg = launches_per_month.rolling(window=6).mean()

        # Find peak month
        peak_month = launches_per_month.idxmax()
        peak_value = launches_per_month.max()

        fig, ax = plt.subplots(figsize=(12, 6))
        ax.plot(
            launches_per_month.index,
            launches_per_month.values,
            label="Monthly Launches",
            alpha=0.6
        )
        ax.plot(
            rolling_avg.index,
            rolling_avg.values,
            label="6-Month Rolling Average",
            linewidth=3
        )

        ax.scatter(peak_month, peak_value, s=120, color='red', zorder=5)
        ax.set_title("Number of Space Launches Month-on-Month")
        ax.set_xlabel("Year")
        ax.set_ylabel("Number of Launches")
        ax.legend()
        ax.grid(alpha=0.3)
        st.pyplot(fig)
        plt.close()

        st.write(
            f"📈 **Based on the provided dataset, the highest number of launches occurred in "
            f"{peak_month.strftime('%B %Y')} with {peak_value} launches.**"
        )
        st.write("Missing Date values:", df["Date"].isna().sum())

    with col2:
        # Launches by calendar month (aggregated across all years)
        launches_by_month = (
            df.groupby(["Month", "Month_Name"])
            .size()
            .reset_index(name="Launch_Count")
            .sort_values("Month")
        )

        # Find most and least popular months
        most_popular = launches_by_month.loc[launches_by_month["Launch_Count"].idxmax()]
        least_popular = launches_by_month.loc[launches_by_month["Launch_Count"].idxmin()]

        fig, ax = plt.subplots(figsize=(10, 5))
        ax.bar(launches_by_month["Month_Name"], launches_by_month["Launch_Count"])
        ax.set_title("Launches by Calendar Month (All Years)")
        ax.set_xlabel("Month")
        ax.set_ylabel("Number of Launches")
        ax.tick_params(axis='x', rotation=45)
        ax.grid(axis="y", alpha=0.3)
        st.pyplot(fig)
        plt.close()

        st.write(
            f"**Most popular month for launches:** {most_popular['Month_Name']} "
            f"({most_popular['Launch_Count']} launches)"
        )

        st.write(
            f"**Least popular month for launches:** {least_popular['Month_Name']} "
            f"({least_popular['Launch_Count']} launches)"
        )

    # PRICE AND DOMINANCE OVER TIME# ========================================================================
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Average Launch Price Over Time")

        # Calculate average price per year
        df_price_clean = df_new.dropna(subset=["Date", "Price"])
        avg_price_per_year = (
            df_price_clean.groupby("Year")["Price"]
            .mean()
            .sort_index()
        )

        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(avg_price_per_year.index, avg_price_per_year.values, linewidth=2)
        ax.set_xlabel("Year")
        ax.set_ylabel("Average Launch Price (USD Millions)")
        ax.set_title("Average Price of Rocket Launches Over Time")
        ax.grid(alpha=0.3)
        st.pyplot(fig)
        plt.close()

    with col2:
        st.subheader("Launch Dominance Over Time (Top 10 Organisations)")

        # Find top 10 organisations by total launches
        top_10_orgs = (
            df.groupby("Organisation")
            .size()
            .sort_values(ascending=False)
            .head(10)
            .index
        )

        # Filter to top 10
        df_top10 = df[df["Organisation"].isin(top_10_orgs)]

        # Count launches per year per organisation
        launches_over_time = (
            df_top10.groupby(["Year", "Organisation"])
            .size()
            .reset_index(name="Launch_Count")
        )

        fig, ax = plt.subplots(figsize=(12, 6))
        for org in top_10_orgs:
            org_data = launches_over_time[launches_over_time["Organisation"] == org]
            ax.plot(org_data["Year"], org_data["Launch_Count"], label=org, linewidth=2)

        ax.set_xlabel("Year")
        ax.set_ylabel("Number of Launches")
        ax.set_title("Number of Launches Over Time by Top 10 Organisations")
        ax.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
        ax.grid(alpha=0.3)
        st.pyplot(fig)
        plt.close()

    # COLD WAR ANALYSIS - DATA PREPARATION ========================================================================
    st.header("The Cold War Era")
    container = st.container(border=True)

    # Create Cold War dataset (up to 1991)
    cold_war_df = df[df["Year"] <= COLD_WAR_END_YEAR].copy()

    # Assign 
    cold_war_df["Bloc"] = "Other"
    cold_war_df.loc[cold_war_df["Country"].isin(USA_COUNTRIES), "Bloc"] = "USA"
    cold_war_df.loc[cold_war_df["Country"].isin(USSR_COUNTRIES), "Bloc"] = "USSR"

    # Filter to only USA and USSR
    cold_war_blocs = cold_war_df[cold_war_df["Bloc"].isin(["USA", "USSR"])].copy()
