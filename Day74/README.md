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

