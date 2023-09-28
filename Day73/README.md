# Day 73 Data Visualization with Matplotlib

## Overview

- Topics: Matplotlib, Pandas, Python  

### The challenge

- Get raw data and create some charts using Pandas and Matplotlib.
- Analyze the the popularity of different programming languages over the years.

![matplotlib](https://github.com/Mikerniker/100_Days_of_Python/assets/63586831/eabc2da0-d7a9-47ed-b3b7-4d5b42f146c4)


## Table of contents

- [Overview](#overview)
  - [The challenge](#the-challenge)
  - [Links](#links)
- [My process](#my-process)
  - [Built with](#built-with)
  - [Notes](#notes)

### Links

- Solution URL: [Data Visualization with Matplotlib](https://github.com/Mikerniker/100_Days_of_Python/tree/main/Day73)


### Notes

### To import pandas and matplotlib

```
import pandas as pd
import matplotlib.pyplot as plt
```

- ```.count()``` To count the number of entries in each column, this tells the number of non-NaN values in each column.
- Use ```.groupby()``` to explore the entries per column.
- Use ```to_datetime()``` to convert strings to Datetime objects for easier plotting.
- Use ```.pivot()``` to reshape DataFrame by converting categories to columns.
- Use ```.count()``` and ```isna().values.any()``` to look for NaN values in DataFrame
- Use ```.fillna()``` to replace NaN values.
- Use ```.plot()``` to create (multiple) line charts, can also be used with a for-loop.
- Charts can be styled by changing the size, the labels, and the upper and lower bounds of the axis. Example:
```   
plt.figure(figsize=(16,10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)
```
- Use ```.legend()``` example: ```plt.legend(fontsize=16)``` to tell lines apart by colour
- Use ```.rolling().mean()``` to smooth out the time-series observations and better identify trends over time.
