# Day 78 Linear Regression and Data Visualization with Seaborn

## Overview

- Topics: Seaborn (Regression a scatter plot, Bubble charts), Matplotlib, Pandas, Linear regression with scikit-learn, convert data with floor division.


### The challenge

- Analyze the given cost revenue dataset to assess whether higher film budgets lead to more revenue in the box office? (i.e., should a movie studio spend more on a film to make more?) using Seaborn, Matplotlib, Pandas, and Sklearn.


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
```
international_releases = data.loc[(data.USD_Domestic_Gross == 0) & 
                                  (data.USD_Worldwide_Gross != 0)]
```

- Other options is to use the Pandas ```.query()``` function: 
```international_releases = data.query('USD_Domestic_Gross == 0 and USD_Worldwide_Gross != 0')```
- pandas Timestamp = ```scrape_date = pd.Timestamp('2018-5-1')```
- To drop a subset of data example: ```data_clean = data.drop(future_releases.index)```
- To calculate the percentage examples with loc or query:
```
money_losing = data_clean.loc[data_clean.USD_Production_Budget > data_clean.USD_Worldwide_Gross]
len(money_losing)/len(data_clean)
```

or
```
money_losing = data_clean.query('USD_Production_Budget > USD_Worldwide_Gross')
money_losing.shape[0]/data_clean.shape[0]
```

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

- To increase the size of figure:
```plt.figure(figsize=(8,4), dpi=200)```

- To style chart, configure the Axes object that is returned from sns.scatterplot().
- To set the styling on a single chart (as opposed to all the charts in the entire notebook) Use Python's with keyword. 
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

- To create a DatetimeIndex, call the constructor and provide the Release_date column as an argument to initialise the DatetimeIndex object. Then extract all the years from the DatetimeIndex, example:

```
dt_index = pd.DatetimeIndex(data_clean.Release_Date)
years = dt_index.year
```
- To convert the years to decades, use floor division (aka integer division) vs regular division, the result is rounded down.
- To conver to decade: Use the floor division by 10 and then multiplication by 10 to convert the release year to the release decade:
```
decades = years//10*10
data_clean['Decade'] = decades
```

#### Plotting Linear Regressions with Seaborn

- Linear regression with Seaborn, use ```.regplot()``` function to create a scatter plot and draw a linear regression line together with the confidence interval.

```
sns.regplot(data=old_films, 
            x='USD_Production_Budget',
            y='USD_Worldwide_Gross')
```

- To style the chart , use Matplotlib layer and supply keyword arguments as dictionaries. Can also add limits, labels, and general style. Example:

```
plt.figure(figsize=(8,4), dpi=200)
with sns.axes_style('darkgrid'):
  ax = sns.regplot(data=new_films,
                   x='USD_Production_Budget',
                   y='USD_Worldwide_Gross',
                   color='#2f4b7c',
                   scatter_kws = {'alpha': 0.3},
                   line_kws = {'color': '#ff7c43'})
  
  ax.set(ylim=(0, 3000000000),
         xlim=(0, 450000000),
         ylabel='Revenue in $ billions',
         xlabel='Budget in $100 millions') 
```

#### Scikit-learn to Run Regression
- Univariate regression. This is a regression with a single explanatory variable (movie BUDGET). Explanatory variables are also referred to as ```features``` in machine learning terminology.

- The regression line (for the exercise) has the following structure:

```REVENUE = y-axis intercept + slope(budget)```
- y-intercept ("theta zero") 
-  slope ("theta one"). 

- To import scikit-learn: ```from sklearn.linear_model import LinearRegression```
- To run run a LinearRegression. First, create a LinearRegression object: ```regression = LinearRegression()```
- Specify features (capital X ) and targets (lower case y) (i.e., response variable). 
```
# Explanatory Variable(s) or Feature(s)
X = pd.DataFrame(new_films, columns=['USD_Production_Budget'])
# Response Variable or Target
y = pd.DataFrame(new_films, columns=['USD_Worldwide_Gross']) 
```
- Find the best-fit line
```regression.fit(X, y)```
- Theta zero
```regression.intercept_```
- Theta one
```regression.coef_```

#### R-Squared: Goodness of Fit
- One measure of figuring out how well our model fits our data is by looking at a metric called r-squared. 
- R-squared
```regression.score(X, y)```

- Make a prediction example: 
```
revenue_estimate = regression.intercept_[0] + regression.coef_[0,0]*budget
revenue_estimate = round(revenue_estimate, -6)
print(f'The estimated revenue for a $350 film is around ${revenue_estimate:.10}.')
```
- (The colon : and dot . in a print statement helps control the number of digits you'd like to show up in the output)	
