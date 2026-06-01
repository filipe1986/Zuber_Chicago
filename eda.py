'''
Step 4. Exploratory data analysis (Python)

In addition to the data retrieved in the previous tasks, you received a second file. You now have these two CSVs:
The file /datasets/project_sql_result_01.csv contains the following data:

trips_amount : the number of rides for each taxi company from November 15th to 16th, 2017.

The file /datasets/project_sql_result_04.csv contains the following data:

dropoff_location_name : Chicago neighborhoods where the races ended

average_trips : the average number of trips that ended in each neighborhood in November 2017.

For these two datasets, you now need...

import the files
study the data they contain
verify that the data types are correct
Identify the top 10 neighborhoods in terms of destinations.
Create graphs: taxi companies and number of rides, top 10 neighborhoods by number of rides where that neighborhood is the destination.
Draw conclusions based on each graph and explain the results.

'''

import pandas as pd

sql_result = pd.read_csv('sql_result_01.csv')

print(sql_result.head(3))

