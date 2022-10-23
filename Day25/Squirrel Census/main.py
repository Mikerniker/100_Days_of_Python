import pandas

squirrel = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
squirrel_count = squirrel["Primary Fur Color"].value_counts()

data = pandas.DataFrame(squirrel_count)
print(data)

#convert to a csv file
data.to_csv("squirrel_count.csv")
