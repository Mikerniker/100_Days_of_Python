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
- Review: .value_counts(), .groupby(), .merge(), .sort_values() and .agg().
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

#### Matplotlib to Visualise Trends over Time

- Review functions: .figure(), the .title(), the .xticks(), and .yticks() to fine-tune the chart

#### [Chloropeth Map](https://plotly.com/python/choropleth-maps/)
- [Plotly color scales](https://plotly.com/python/builtin-colorscales/)
- [Plotly line chart](https://plotly.com/python/line-charts/)
- .cumsum() function (cumulutative sum)

- [Sunburst Charts](https://plotly.com/python/sunburst-charts/)
- [Seaborn Histogram](https://seaborn.pydata.org/generated/seaborn.histplot.html)
- [Seaborn .histplot() function](https://seaborn.pydata.org/generated/seaborn.histplot.html)
- [Seaborn .regplot ](https://seaborn.pydata.org/generated/seaborn.regplot.html?highlight=regplot#seaborn.regplot)
- [Seaborn .boxplot()](https://seaborn.pydata.org/generated/seaborn.boxplot.html?highlight=boxplot#seaborn.boxplot)
- [Seaborn .lmplot()](https://seaborn.pydata.org/generated/seaborn.lmplot.html?highlight=lmplot#seaborn.lmplot)
  - hue parameter
  - row parameter
  - lowess parameter

- To extract the year as a number from a datetime column, example: ```birth_years = df_data.birth_date.dt.year```
- [Panda .nlargest()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.nlargest.html)
- [Panda .nsmallest](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.nsmallest.html)