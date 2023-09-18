# Day 79 Analyzing the Nobel Prize with Plotly, Matplotlib, and Seaborn

## Overview

- Topics: Seaborn , Matplotlib, Plotly


### The challenge

- Analyze a dataset on the past winners of the Nobel Prize to uncover patterns among the past Nobel laureates and glean other insights on the Nobel prize and the world in general.

## Table of contents

- [Overview](#overview)
  - [The challenge](#the-challenge)
  - [Links](#links)
- [Notes](#notes)

### Links

- Solution URL: [Analyzing the Nobel Prize with Plotly, Matplotlib, and Seaborn](https://github.com/Mikerniker/100_Days_of_Python/tree/main/Day79)


###  Notes

- To updated a package in Google Colab: ```%pip install --upgrade plotly```
- To filter a subset if the data:
```
col_subset = ['year','category', 'laureate_type',
              'birth_date','full_name', 'organization_name']
df_data.loc[df_data.birth_date.isna()][col_subset]
```
- A column can be split and sliced to get certain items or perform operations on items of that column
- Review: Plotly (donut chart, bar chart)
- To filter a column based on an item then sort according to another column:
```df_data[df_data.sex == 'Female'].sort_values('year', ascending=True)[:3]``` 
- ```.groupby()``` and ```.agg()``` and ```.count()``` can be combined
- Review .color the parameter in the ```.bar()``` function
