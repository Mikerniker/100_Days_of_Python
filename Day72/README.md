# Day 72 Data Exploration with Pandas

## Overview

- Topics: Pandas, Python, Beautiful Soup (Web Scraping)

### The challenge

Challenge 1\
With the given data find the following:
1. What college major has the highest mid-career salary? How much do graduates with this major earn? 
2. Which college major has the lowest starting salary and how much do graduates earn after university?
3. Which college major has the lowest mid-career salary and how much can people expect to earn with this degree?

Challenge 2
1. Use the .sort_values() method to find the degrees with the highest potential. Find the top 5 degrees with the highest values in the 90th percentile. 
2. Find the degrees with the greatest spread in salaries. Which majors have the largest difference between high and low earners after graduation?

Mini-Challenge 3:\
Use web scraping to scrape more updated data in Payscale. 
(My Extra Credit solution: main.py and Salaries2023.ipynb) 



![pandasrev](https://github.com/Mikerniker/100_Days_of_Python/assets/63586831/01f1b27d-afd1-45ca-8272-03823a57b93d)

## Table of contents

- [Overview](#overview)
  - [The challenge](#the-challenge)
  - [Links](#links)
- [My process](#my-process)
  - [Built with](#built-with)
  - [Notes](#notes)

### Links

- Solution URL: [Data Exploration with Pandas](https://github.com/Mikerniker/100_Days_of_Python/tree/main/Day72)


### Notes

#### Import and open a CSV file with Pandas
- import pandas as pd
- df = pd.read_csv('salaries_by_college_major.csv') #example to read panda csv file

##### To explore Panda DataFrame (find number of rows, columns, and column names):
- .head()
  - ```df.head()``` Shows the first 5 rows of the dataframe
- .tail()
  - ```df.tail()```  Checks the last couple of rows in the dataframe
- .shape 
  - ```df.shape```  To see the number of rows and columns
- .columns

##### Clean DataFrame
- Look for NaN (not a number) values with .findna() 
- ```.isna() method``` To see if there are Nan values.
- NAN values are blank cells or cells that contain strings instead of numbers. 
- Consider using .dropna() to clean up DataFrame
-  ```.dropna() method``` Removes the row with the Nan
Example:
```
clean_df = df.dropna()
clean_df.tail()
```

##### To access entire columns of a DataFrame
- Use the square bracket notation: 
- ```df['column name']``` or
- ```df[['column name 1', 'column name 2', 'column name 3']]```

##### To access individual cells in a DataFrame
- Chain square brackets, example:
- ```df['column name'][index]``` or 
- ```df['column name'].loc[index]```

##### To find the largest and smallest values (and their positions)
- Use the following methods 
- ```.max()```
- ```.min()```
- ```.idxmax()```
- ```.idxmin()```

##### Sort DataFrame
- Use ```.sort_values()``` 

##### Add new columns
- Use ```.insert()```

##### To create an Excel Style Pivot Table by grouping entries that belong to a particular category
- Use the .groupby() method

### References:
- [.sort_values](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html)
References Used for mini-challenge:
- [Beautiful Soup getting Tags](https://www.geeksforgeeks.org/find-the-text-of-the-given-tag-using-beautifulsoup/)
- [Beautiful Soup Extracting Tables](https://www.pluralsight.com/guides/extracting-data-html-beautifulsoup)
- [Scrape Multiple Pages with BS](https://proxyway.com/knowledge-base/how-to-scrape-multiple-pages-using-beautifulsoup)
- [Lists and Dicts to CSV](https://blog.enterprisedna.co/how-to-write-a-list-to-csv-in-python/)

## Additional Notes for Extra Credit
8/29/2023
Initially had a hard time figuring out why I kept getting a value error for the scraped salaries2023 data set whenever I tried using ```.astype()``` Slowly realized I had to remove the following symbols 
```$",``` (quotation marks AND comma) but ended up doing it at different points in time, so the code is longer than necessary: 
```
clean_early_career = df['Early Career Pay'].str.replace('$', '')
df.insert(1, 'Early Career New', clean_early_career)
df['Early Career New'].str.replace('"', '')
df['Early Career New'] = df['Early Career New'].str.replace(',', '').astype(float)
df.head()
```

Some references used:
- [Pandas String to Float](https://sparkbyexamples.com/pandas/pandas-convert-string-to-float-type-dataframe/)
- [Pandas ValueError Could not Conver str to Float](https://bobbyhadz.com/blog/python-valueerror-could-not-convert-string-to-float)
- [Delete a column with Pandas](https://www.educative.io/answers/how-to-delete-a-column-in-pandas)