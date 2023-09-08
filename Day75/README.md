# Day 75 Google Trends Data: Resampling and Visualizing Time Series

## Overview

- Topics: Pandas and Matplotlib: Data Cleaning, Resampling Time Series Data, Converting to Datetime, Data Visualisation (Line Charts, Locators, DateFormatters, Line Style, and Markers)

### The challenge

Identify the Following with Pandas and Matplotlib:
1. How search volume for "Bitcoin" relates to the price of Bitcoin
2. How search volume for a hot stock like Telsa relates to that stock's price and
3. How searches for "Unemployment Benefits" vary with the actual unemployment rate in the United States


## Table of contents

- [Overview](#overview)
  - [The challenge](#the-challenge)
  - [Links](#links)
- [My process](#my-process)
  - [Built with](#built-with)
  - [Notes](#notes)


### Links

- Solution URL: [Google Trends Data](https://github.com/Mikerniker/100_Days_of_Python/tree/main/Day75)


### Pandas Notes
- ```.describe()```  - Generate descriptive statistics. Descriptive statistics include those that summarize the central tendency, dispersion and shape of a dataset’s distribution, excluding NaN values.


##### Data Cleaning - Resampling Time Series Data

- To verify missing values use ```.isna()``` method, wich returns a series of booleans
This can be chained with ```.values.any()``` to see if any value in the series is True.
Example: ```df_tesla.isna().values.any()```
- Missing values can be found by using .sum() to add up the number of occurrences of True in the series. and to find the row where the missing values occur, create a subset of the DataFrame using ```.isna()```. Use ```.dropna()``` to remove a missing value :
Example: 
```
df_btc_price.isna().values.sum()
df_btc_price[df_btc_price.CLOSE.isna()]
df_btc_price.dropna(inplace=True)
```

##### Converting Strings to DateTime Objects

- To convert string columns into a Datetime object use the Pandas ```.to_datetime()``` function. Example: 
```df_tesla.MONTH = pd.to_datetime(df_tesla.MONTH)```

##### Resampling Time Series Data
- To convert daily data into monthly data, to use the ```.resample()``` function, specify which column to use (e.g. the DATE column) and the kind of sample frequency (i.e., the "rule"). Example: For a monthly frequency, use 'M', 'Y' for yearly or 'T' for minute.
- After resampling, figure out how the data should be treated. Ex if you want the last available price of the month - the price at month-end:
```df_btc_monthly = df_btc_price.resample('M', on='DATE').last()```
OR if you need the average price over the course of the month:
```df_btc_monthly = df_btc_price.resample('M', on='DATE').mean()```

##### Data Visualisation - Tesla Line Charts in Matplotlib
- To create a line plot with two different y-axes we first have to get the current axis and make a copy of it using ```.twinx()```. Then we can configure each axis separately and call ```.plot()```.
- Use ```.figure()``` to increase the size and resolution of our chart.
- Call ```.show()``` to explicitly display the chart below the cell. The ```.show()``` method is important if you try to generate charts in PyCharm or elsewhere outside of an interactive notebook like Google Colab or Jupyter. It gives a very clean look to the notebook.
- ```.set_ylim()``` and ```.set_xlim()``` gives you precise control over the data you want to show on the chart. Either hard values or the ```.min()``` and ```.max()``` functions can be used.
- Fix the Matplotlib Warning (see ipynb) 

- Adding colours with HEX or colors Example:
  - ```x1.set_ylabel('TSLA Stock Price', color='#E6232E')``` # HEX 
  - ```ax2.set_ylabel('Search Trend', color='skyblue')``` # named colour

##### Using Locators and DateFormatters to generate Tick Marks on a Time Line
- ```import matplotlib.dates as mdates```
- objects: YearLocator(), MonthLocator(), DateFormatter()
Example ```years = mdates.YearLocator()```
- Format the ticks where the major and minor ticks should be using the Locators:
   - ```ax1.xaxis.set_major_locator(years)```

- Line Style and Markers Example:
```
ax1.plot(df_btc_monthly.index, df_btc_monthly.CLOSE, 
         color='#F08F2E', linewidth=3, linestyle='--')
ax2.plot(df_btc_monthly.index, df_btc_search.BTC_NEWS_SEARCH, 
         color='skyblue', linewidth=3, marker='o')
```
 
- To Add a Grid Example: ```ax1.grid(color='grey', linestyle='--')```
- Use [.grid()](https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.grid.html) to help visually identify seasonality in a time series.

# Resources
- [HEX codes](https://htmlcolorcodes.com/color-picker/)
- [Matplotlib Color Names](https://matplotlib.org/3.1.1/gallery/color/named_colors.html)
- [Matplotlib Markers](https://matplotlib.org/3.2.1/api/markers_api.html)
- [Matplotlib Linestyles](https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.plot.html)