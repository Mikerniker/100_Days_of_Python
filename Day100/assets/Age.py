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

st.title("How Old Were the People Killed?")
# How Old Were the People Killed?
# Work out what percentage of people killed were under 25 years old.
# Create a histogram and KDE plot that shows the distribution of ages of the people killed by police.
# Create a seperate KDE plot for each race. Is there a difference between the distributions?
# Ensure age is numeric

container = st.container(border=True)
container.subheader("What percentage of people killed were under 25 years old?")
df_fatalities['age'] = pd.to_numeric(df_fatalities['age'], errors='coerce')

total_people = df_fatalities['age'].notna().sum()
under_25_count = (df_fatalities['age'] < 25).sum()
percent_under_25 = round((under_25_count / total_people) * 100, 1)

container.write(f"Total people with known age: {total_people}")
container.write(f"People under 25: {under_25_count}")
container.write(f"**{percent_under_25}% of people killed were under 25 years old**")

# -----------------------------------------------
# Create a Box Plot Showing the Age and Manner of Death
# Break out the data by gender using `df_fatalities`. Is there a difference between
# men and women in the manner of death?
df_fatalities['gender_label'] = df_fatalities['gender'].map({
    'M': 'Men',
    'F': 'Women'
})


fig = px.box(
    df_fatalities,
    x='manner_of_death',
    y='age',
    color='gender_label',
    points='all',
    title='Age Distribution by Manner of Death and Gender'
)

fig.update_layout(
    xaxis_title='Manner of Death',
    yaxis_title='Age',
)

st.plotly_chart(fig, use_container_width=True)
st.write("Men account for the majority of deaths across all manners, "
         "with wider age distributions. Women are also less likely "
         "to be both shot and tasered.")