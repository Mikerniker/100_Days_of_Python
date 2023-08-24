# Day 72 Data Exploration with Pandas

## Overview

- Topics: Pandas

### The challenge


## Table of contents

- [Overview](#overview)
  - [The challenge](#the-challenge)
  - [Links](#links)
- [My process](#my-process)
  - [Built with](#built-with)
  - [Notes](#notes)

### Links

- Solution URL: [Data Exploration with Pandas](https://github.com/Mikerniker/100_Days_of_Python/tree/main/Day72)

### Built with

### Notes

import pandas as pd
df = pd.read_csv('salaries_by_college_major.csv')



- ```df.head()``` Shows the first 5 rows of the dataframe

- ```df.shape```  To see the number of rows and columns
- NAN values are blank cells or cells that contain strings instead of numbers. 
- ```.isna() method``` To see if there are Nan values.
- ```df.tail()```  Checks the last couple of rows in the dataframe
-  ```.dropna() method``` Removes the row with the Nan
Example
```clean_df = df.dropna()
clean_df.tail()```

### References: