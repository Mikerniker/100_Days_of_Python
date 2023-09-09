# Day 76 Analyze Android App Store (with Plotly)

## Overview

- Topics: Pandas (Data Cleaning: Removing NaN Values, Finding and Removing Duplicates, Dropping Unused Columns, Removing NaN Values, Converting Data to Numeric Types, Working with Nested Column Data) and  Plotly ( Pie, Donut, Bar Charts, Box Plots, Scatter Plots, Colour Scales)


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


#### Data Cleaning: Removing NaN Values and Duplicates

- To get a random sample of n rows use ```.sample()```

#### Dropping Unused Columns and Removing NaN Values

- To remove the unwanted columns, provide a list of the column names to the .drop() method. Setting axis=1 specifies that we want to drop certain columns.
- Example: ```df_apps.drop(['Last_Updated', 'Android_Ver'], axis=1, inplace=True)```
- To find and remove the rows with the NaN values, create a subset of the DataFrame based on where .isna() evaluates to True. Example:  ```nan_rows = df_apps[df_apps.Rating.isna()]```
- To drop the NaN values use .dropna():
```
df_apps_clean = df_apps.dropna()
df_apps_clean.shape
```

#### Finding and Removing Duplicates
- Use ```.drop_duplicates()``` to remove any duplicates.
- Example: 
```
duplicated_rows = df_apps_clean[df_apps_clean.duplicated()]
print(duplicated_rows.shape)
duplicated_rows.head()
```
- To check for individual items, ex check for an individual app like ‘Instagram’ by looking up all the entries with that name in the App column: ```df_apps_clean[df_apps_clean.App == 'Instagram']```
- Provide the column names/subset that should be used in the comparison to identify duplicates. For example:
```
df_apps_clean = df_apps_clean.drop_duplicates(subset=["App", "Type", "Price"])
df_apps_clean[df_apps_clean.App == 'Instagram']
```

- Review to find highest values, use .sort_values with ascending set to False; You can also specify the number of rows you want to see in head, Example: ```df_apps_clean.sort_values('Reviews', ascending=False).head(50)```
- Count the number of occurrences of a column with ```.value_counts()```, example:
```ratings = df_apps_clean.Content_Rating.value_counts()```



#### Ploty Notes
- To import Plotly: ```import plotly.express as px```

##### Pie Charts
- To create a pie chart call ```px.pie()``` and then ```.show()``` the resulting figure. 
- Plotly refers to all their figures, be they line charts, bar charts, or pie charts as graph_objects.
- Example:
```
fig = px.pie(labels=ratings.index, values=ratings.values)
fig.show()
```

###### To Customize Pie Chart:
- If you’d like to configure other aspects of the chart, that you can’t see in the list of parameters, you can call a method called ```.update_traces()```. 
- In plotly lingo, “traces” refer to graphical marks on a figure, like a collection of attributes. 
```
fig = px.pie(labels=ratings.index,
values=ratings.values,
title="Content Rating",
names=ratings.index,
)
fig.update_traces(textposition='outside', textinfo='percent+label')
 
fig.show()
```

###### Donut Chart
- To create a donut chart, we can simply add a value for the hole argument:
```
fig = px.pie(labels=ratings.index,
values=ratings.values,
title="Content Rating",
names=ratings.index,
hole=0.6, #added
)
fig.update_traces(textposition='inside', textfont_size=15, textinfo='percent')
 
fig.show()
```

#### Data Cleaning & Converting Data to Numeric Types
- To check the data types you can either use ```.describe()``` on the column or ```.info()``` on the DataFrame. Example:
```
df_apps_clean.Installs.describe()
df_apps_clean.info()
```
- Python can't recognize data as numbers if there are comma (,) characters.
- To remove the comma (,) character - or any character - from a DataFrame use the string’s ```.replace()``` method. Then you can convert data to a number using ```.to_numeric()```.

```
df_apps_clean.Installs = df_apps_clean.Installs.astype(str).str.replace(',', "")
df_apps_clean.Installs = pd.to_numeric(df_apps_clean.Installs)
df_apps_clean[['App', 'Installs']].groupby('Installs').count()
```

- To remove rows of unnecessary data, example remove prices over $250:
```
df_apps_clean = df_apps_clean[df_apps_clean['Price'] < 250]
df_apps_clean.sort_values('Price', ascending=False).head(5)
```
- To multiply and create a new column:
```
df_apps_clean['Revenue_Estimate'] = df_apps_clean.Installs.mul(df_apps_clean.Price)
df_apps_clean.sort_values('Revenue_Estimate', ascending=False)[:10]
```

##### Plotly Bar Charts & Scatter Plots
- Use nunique to find unique categories ```df_apps_clean.Category.nunique()```
- To calculate the number of apps per category use ```.value_counts()```
- ```top10_category = df_apps_clean.Category.value_counts()[:10]```

###### Bar Chart
- To visualise this data in a bar chart we can use the plotly express (our px) bar() function:
```
bar = px.bar(x = top10_category.index, # index = category name
             y = top10_category.values)
 
bar.show()
```
- To group all our apps by category and sum the number of installations:
```
category_installs = df_apps_clean.groupby('Category').agg({'Installs': pd.Series.sum})
category_installs.sort_values('Installs', ascending=True, inplace=True)
Then we can create a horizontal bar chart, simply by adding the orientation parameter:

h_bar = px.bar(x = category_installs.Installs,
               y = category_installs.index,
               orientation='h')
 
h_bar.show()
````
- To add a custom title and axis labels:
```
h_bar = px.bar(x = category_installs.Installs,
               y = category_installs.index,
               orientation='h',
               title='Category Popularity')
 
h_bar.update_layout(xaxis_title='Number of Downloads', yaxis_title='Category')
h_bar.show()
```

###### Create a scatter plot with Plotly

- To work out the number of apps in each category:
```cat_number = df_apps_clean.groupby('Category').agg({'App': pd.Series.count})````
- To combine two DataFrames use ```.merge()``` 
```
cat_merged_df = pd.merge(cat_number, category_installs, on='Category', how="inner")
print(f'The dimensions of the DataFrame are: {cat_merged_df.shape}')
cat_merged_df.sort_values('Installs', ascending=False)
```
- To create the chart: 
```
scatter = px.scatter(cat_merged_df, # data
                    x='App', # column name
                    y='Installs',
                    title='Category Concentration',
                    size='App',
                    hover_name=cat_merged_df.index,
                    color='Installs')
 
scatter.update_layout(xaxis_title="Number of Apps (Lower=More Concentrated)",
                      yaxis_title="Installs",
                      yaxis=dict(type='log'))
 
scatter.show()
```

#### Extracting Nested Column Data using .stack()

###### Working with Nested Column Data

- Use ```.value_counts()```  to look at the values that just have a single entry. (There we see that the semi-colon (;) separates the genre names.)
```df_apps_clean.Genres.value_counts().sort_values(ascending=True)[:5]```
- To separate the genre names use string’s ```.split()``` method. After separating genre names based on the semi-colon,  add them all into a single column with ```.stack()``` and then use ```.value_counts()```.

- Split the strings on the semi-colon and then .stack them.
```
stack = df_apps_clean.Genres.str.split(';', expand=True).stack()
print(f'We now have a single column with shape: {stack.shape}')
num_genres = stack.value_counts()
print(f'Number of genres: {len(num_genres)}')
```

###### Working with Colour Scales in Plotly

- Set the colour scale use the color_continuous_scale parameter.
- To make the colour axis disappear use coloraxis_showscale.
```
bar = px.bar(x = num_genres.index[:15], # index = category name
             y = num_genres.values[:15], # count
             title='Top Genres',
             hover_name=num_genres.index[:15],
             color=num_genres.values[:15],
             color_continuous_scale='Agsunset')
 
bar.update_layout(xaxis_title='Genre', yaxis_title='Number of Apps', coloraxis_showscale=False)
 
bar.show()
```

###### Grouped Bar Charts and Box Plots with Plotly
- To group our data first by Category and then by Type, add up the number of apps per each type. Using as_index=False pushes all the data into columns rather than end up with Categories as the index.
```
df_free_vs_paid = df_apps_clean.groupby(["Category", "Type"], as_index=False).agg({'App': pd.Series.count})
df_free_vs_paid.head()
```
- To use color and barmode parameters for the .bar() method. To get a particular order, pass a dictionary to the axis parameter in .update_layout().
```
g_bar = px.bar(df_free_vs_paid,
               x='Category',
               y='App',
               title='Free vs Paid Apps by Category',
               color='Type',
               barmode='group')
 
g_bar.update_layout(xaxis_title='Category',
                    yaxis_title='Number of Apps',
                    xaxis={'categoryorder':'total descending'},
                    yaxis=dict(type='log'))
 
g_bar.show()
```

###### Box Plots
- Box plots can show descriptive statistics in a graph - things like the median value, the maximum value, the minimum value, and some quartiles. 
- Example box plot:
```box = px.box(df_apps_clean,
             y='Installs',
             x='Type',
             color='Type',
             notched=True,
             points='all',
             title='How Many Downloads are Paid Apps Giving Up?')
 
box.update_layout(yaxis=dict(type='log'))
 
box.show()
```
```
df_paid_apps = df_apps_clean[df_apps_clean['Type'] == 'Paid']
box = px.box(df_paid_apps, 
             x='Category', 
             y='Revenue_Estimate',
             title='How Much Can Paid Apps Earn?')
 
box.update_layout(xaxis_title='Category',
                  yaxis_title='Paid App Ballpark Revenue',
                  xaxis={'categoryorder':'min ascending'},
                  yaxis=dict(type='log'))
 
 
box.show()
```
- Can use {categoryorder':'max descending'} to sort the categories.
- To get the median use .median, example ```df_paid_apps.Price.median()```
```
box = px.box(df_paid_apps,
             x='Category',
             y="Price",
             title='Price per Category')
 
box.update_layout(xaxis_title='Category',
                  yaxis_title='Paid App Price',
                  xaxis={'categoryorder':'max descending'},
                  yaxis=dict(type='log'))
 
box.show()
```


References
- [ .pie() documentation](https://plotly.com/python-api-reference/generated/plotly.express.pie.html)
- [.stack()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.stack.html)
-[Box Plots](https://plotly.com/python/box-plots/)