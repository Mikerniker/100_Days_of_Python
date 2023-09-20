# Day 80 T-Tests & Distributions: Analyzing a Hospital Data Set

## Overview

- Topics: Seaborn , Matplotlib, Plotly


### The challenge

- Analyze a dataset on the number of births and maternal deaths throughout the 1840s.

## Table of contents

- [Overview](#overview)
  - [The challenge](#the-challenge)
  - [Links](#links)
- [Notes](#notes)

### Links

- Solution URL: [T-Tests & Distributions](https://github.com/Mikerniker/100_Days_of_Python/tree/main/Day80)


###  Notes
- Review of Matplotlib (mdates, .twinx(), .grid(), color, linewidth, linestyle parameters, .plot(), plt.legend()) 
- [Matplotlib add a Legend](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.legend.html)

- Review of Plotly (line charts), Box plots, calculating a Rolling Average
- [NumPy's .where() function](https://numpy.org/doc/stable/reference/generated/numpy.where.html)
- [Plotly Histogram](https://plotly.com/python/histograms/)
  - color parameter
  - histnorm
  - marginal parameter
- [Kernel Density Estimate (KDE) kdeplot()](https://seaborn.pydata.org/generated/seaborn.kdeplot.html)
  - shade parameter
  - clip parameter
- T-Test to Show Statistical Significance
  - If the p-value is less than 1% then there's 99% certainty
  - import stats from scipy: ```import scipy.stats as stats```
  - Use the .ttest_ind() function to calculate a t-statistic and p-value
