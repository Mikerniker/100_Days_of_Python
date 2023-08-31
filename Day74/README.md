# Day 74 Analyze Lego Data Set (Aggregate and Merge Data with Pandas)

## Overview

- Topics: Matplotlib, Pandas, Python,  

### The challenge



## Table of contents

- [Overview](#overview)
  - [The challenge](#the-challenge)
  - [Links](#links)
- [My process](#my-process)
  - [Built with](#built-with)
  - [Notes](#notes)

### Links

- Solution URL: [Analyze Lego Data Set](https://github.com/Mikerniker/100_Days_of_Python/tree/main/Day74)


### Notes

#### Markdown Notes

- The Double-asterisk ** symbol will make text bold.
- Adding images to markdown is possible with HTML. For example: ```<img src="https://i.imgur.com/49FNOHj.jpg">```

#### Panda Notes

- ```.sort_values()``` Sorts in ascending order by default. For example: ```sets.sort_values('year').head()```
- ```sets[sets['year'] == 1949]``` Example of filtering DataFrame on a condition. Retrieving the rows where the year column has the value 1949: sets['year'] == 1949.
- Set the ascending argument to False when we sorting if we want to find the largest number, example: 
```sets.sort_values('num_parts', ascending=False).head()```

#### Matplotlib Notes

- To import matplotlib:
```
import pandas as pd
import matplotlib.pyplot as plt
```




Can exclude data with slicing, example: ```plt.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2])```
- Pandas .agg() function

When you need to summarize data, the .groupby() function comes in handy. However, if you want to run even more operations based on a particular DataFrame column, the .agg() method comes in.
Example: Calculate the number of different themes by calendar year. This means grouping the data by year and then counting the number of unique theme_ids for that year, so chain the .groupby() and the .agg() functions together: ```themes_by_year = sets.groupby('year').agg({'theme_id': pd.Series.nunique})```
- The .agg() method takes a dictionary as an argument. In this dictionary, specify which operation to apply to each column. In the example, calculate the number of unique entries in the theme_id column by the .nunique() method.
```
themes_by_year = sets.groupby('year').agg({'theme_id': pd.Series.nunique})
themes_by_year.rename(columns = {'theme_id':'nr_themes'}, inplace = True)
themes_by_year.head()
themes_by_year.tail()
```



