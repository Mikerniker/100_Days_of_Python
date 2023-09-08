# Day 76 Analyze Android App Store (with Plotly)

## Overview

- Topics: 

### The challenge

- Analyze/Compare apps in the Google Play Store to answer the following: 
  - How competitive different app categories (e.g., Games, Lifestyle, Weather) are
  - Which app category offers compelling opportunities based on its popularity
  - How many downloads you would give up by making your app paid vs. free
  - How much you can reasonably charge for a paid app
  - Which paid apps have had the highest revenue
  - How many paid apps will recoup their development costs based on their sales revenue


## Table of contents

- [Overview](#overview)
  - [The challenge](#the-challenge)
  - [Links](#links)
- [My process](#my-process)
  - [Built with](#built-with)
  - [Notes](#notes)

### Links

- Solution URL: [Analyze Android App Store (with Plotly)](https://github.com/Mikerniker/100_Days_of_Python/tree/main/Day76)


### Notes

#### Panda Notes

#### Plotly Notes
- Use ```.update_traces()```  to configure other aspects of the chart that you can’t see in the list of parameters.
- “traces” (in plotly lingo) refer to graphical marks on a figure, like collections of attributes.


References
- [ .pie() documentation](https://plotly.com/python-api-reference/generated/plotly.express.pie.html)
- [.stack()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.stack.html)
-[Box Plots](https://plotly.com/python/box-plots/)