# Day 78 Linear Regression and Data Visualization with Seaborn

## Overview

- Topics: Numpy


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
 
plt.show()```

- To set the styling on a single chart (as opposed to all the charts in the entire notebook) Use Python's with keyword. 

plt.figure(figsize=(8,4), dpi=200)
 
# To set the styling on a single chart (as opposed to all the charts in the entire notebook) Use Python's with keyword. 
with sns.axes_style('darkgrid'):
  ax = sns.scatterplot(data=data_clean,
                       x='USD_Production_Budget', 
                       y='USD_Worldwide_Gross',
                       hue='USD_Worldwide_Gross',
                       size='USD_Worldwide_Gross')
 
  ax.set(ylim=(0, 3000000000),
        xlim=(0, 450000000),
        ylabel='Revenue in $ billions',
        xlabel='Budget in $100 millions')

In addition to 'darkgrid', Seaborn has a number of built-in themes. so you can style your chart very quickly. Try out 'whitegrid', 'dark',  or 'ticks' for example.

Challenge
Now that you've seen how to create a beautiful bubble chart in Seaborn, it's time to create your own. Can you write the code to replicate this chart? Notice how we are actually representing THREE dimensions in this chart: the budget, the release date, and the worldwide revenue. This is what makes bubble charts so awesomely informative.

Solution: Movie Budgets over Time

Alright, I hope that was fairly straightforward. All you needed to do is change a few arguments:

plt.figure(figsize=(8,4), dpi=200)
 
with sns.axes_style("darkgrid"):
    ax = sns.scatterplot(data=data_clean, 
                    x='Release_Date', 
                    y='USD_Production_Budget',
                    hue='USD_Worldwide_Gross',
                    size='USD_Worldwide_Gross',)
 
    ax.set(ylim=(0, 450000000),
           xlim=(data_clean.Release_Date.min(), data_clean.Release_Date.max()),
           xlabel='Year',
           ylabel='Budget in $100 millions')
 
Analysis

What do we see here? What is this chart telling us? Well, first off, movie budgets have just exploded in the last 40 years or so. Up until the 1970s, the film industry appears to have been in an entirely different era. Budgets started growing fast from the 1980s onwards and continued to grow through the 2000s. Also, the industry has grown massively, producing many more films than before. The number of data points is so dense from 2000 onwards that they are overlapping.


611. Floor Division: A Trick to Convert Years to Decades

Floor Division: A Trick to Convert Years to Decades
In our bubble charts, we've seen how massively the industry has changed over time, especially from the 1970s onwards. This makes me think it makes sense to separate our films out by decade. Here's what I'm after:


Challenge
Can you create a column in data_clean that has the decade of the movie release. For example, a film released in 1992 or 1999 should have 1990 in the Decade column.

Here is one approach that you can follow:

- Create a DatetimeIndex object from the Release_Date column.
- Grab all the years from the DatetimeIndex object using the .year property.
- Use floor division // to convert the year data to the decades of the films.
- Add the decades as a Decade column to the data_clean DataFrame.

Solution: Using Floor Division to Convert Years to Decades

To create a DatetimeIndex, we just call the constructor and provide our release date column as an argument to initialise the DatetimeIndex object. Then we can extract all the years from the DatetimeIndex.

dt_index = pd.DatetimeIndex(data_clean.Release_Date)
years = dt_index.year

Now, all we need to do is convert the years to decades. For that, we will use floor division (aka integer division). The difference to regular division is that the result is effectively rounded down.

5.0 / 2
# output: 2.5
5.0 // 2
# output: 2.0
In our case, we will use the floor division by 10 and then multiplication by 10 to convert the release year to the release decade:

# How to conver the year 1999 to the 90s decade
1999 //10
>> 199
199*10
>>1990

We can do this for all the years and then add the decades back as a column.

decades = years//10*10
data_clean['Decade'] = decades


Challenge
- Create two new DataFrames: old_films and new_films
-old_films should include all the films before 1970 (up to and including 1969)
- new_films should include all the films from 1970 onwards
- How many of our films were released prior to 1970?
- What was the most expensive film made prior to 1970?

Solution: Separate the films made before and after 1970

Now that we have our Decades column we can use it to create subsets of our data.

old_films = data_clean[data_clean.Decade <= 1960]
new_films = data_clean[data_clean.Decade > 1960]
The cut-off for our calculation is 1960 in the Decade column because this will still include 1969. When we inspect our old_films DataFrame we see that it only includes 153 films. As we saw in the bubble chart, the bulk of films in the dataset have been released in the last 30 years.

old_films.describe()
old_films.sort_values('USD_Production_Budget', ascending=False).head()

The most expensive film prior to 1970 was Cleopatra, with a production budget of $42 million. That's some serious 1960s money, and judging by the trailer, a lot of it went into extravagant costumes, set design, and plenty of extras. Impressive.


##### Plotting Linear Regressions with Seaborn