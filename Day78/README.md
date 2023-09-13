# Day 78 Linear Regression and Data Visualization with Seaborn

## Overview

- Topics: Seaborn


### The challenge



## Table of contents

- [Overview](#overview)
  - [The challenge](#the-challenge)
  - [Links](#links)
- [My process](#my-process)
  - [Notes](#notes)

### Links

- Solution URL: [Linear Regression and Data Visualization with Seaborn](https://github.com/Mikerniker/100_Days_of_Python/tree/main/Day78)


###  Notes
Concepts reviewed
- .describe()
- .sort_values()


#### Filter on Multiple Conditions

- One approach use the .loc[] property combined with the bitwise and & operator. Example:
```international_releases = data.loc[(data.USD_Domestic_Gross == 0) & 
                                  (data.USD_Worldwide_Gross != 0)]```

- Other options is to use the Pandas ```.query()``` function: 
```international_releases = data.query('USD_Domestic_Gross == 0 and USD_Worldwide_Gross != 0')```
- pandas Timestamp = ```scrape_date = pd.Timestamp('2018-5-1')```
- To drop a subset of data example: ```data_clean = data.drop(future_releases.index)```
- To calculate the percentage examples with loc or query:
```money_losing = data_clean.loc[data_clean.USD_Production_Budget > data_clean.USD_Worldwide_Gross]
len(money_losing)/len(data_clean)```
or
```money_losing = data_clean.query('USD_Production_Budget > USD_Worldwide_Gross')
money_losing.shape[0]/data_clean.shape[0]```

#### Seaborn Data Visualisation: Bubble Charts

- To import Seaborn:  ```import seaborn as sns```

##### Seaborn Scatter Plots

- To create a simple .scatterplot():
```
sns.scatterplot(data=data_clean,
                x='USD_Production_Budget', 
                y='USD_Worldwide_Gross')
```

##### From Scatter Plot to Bubble Chart

- Seaborn has hue and size parameters that make it easy to create a bubble chart. These parameters colour the data and change their size according to one of the columns in the DataFrame.

# increase the size of figure:
```plt.figure(figsize=(8,4), dpi=200)```

# style chart, configure the Axes object that is returned from sns.scatterplot().
# To set the styling on a single chart (as opposed to all the charts in the entire notebook) Use Python's with keyword. 
```
with sns.axes_style('darkgrid'):
  ax = sns.scatterplot(data=data_clean,
                       x='USD_Production_Budget', 
                       y='USD_Worldwide_Gross',
                       hue='USD_Worldwide_Gross',
                       size='USD_Worldwide_Gross')


ax.set(ylim=(0, 3000000000),
       xlim=(0, 450000000),
       ylabel='Revenue in $ billions',
       xlabel='Budget in $100 millions',)
 
plt.show()
```

- Seaborn has different built-in themes to style chart very quickly, examples: 'whitegrid', 'dark', 'darkgrid', or 'ticks'. 

#### Floor Division: Converting Years to Decades

- To create a DatetimeIndex, call the constructor and provide the Release_date column as an argument to initialise the DatetimeIndex object. Then extract all the years from the DatetimeIndex, example

```dt_index = pd.DatetimeIndex(data_clean.Release_Date)
years = dt_index.year```

- To convert the years to decades, use floor division (aka integer division) vs regular division, the result is rounded down.

- To conver to decade: Use the floor division by 10 and then multiplication by 10 to convert the release year to the release decade:
```
decades = years//10*10
data_clean['Decade'] = decades
```

#### Plotting Linear Regressions with Seaborn