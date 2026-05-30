'''
Step 1. Write code to analyze the weather data for Chicago in November 2017 on the website:

https://practicum-content.s3.us-west-1.amazonaws.com/data-analyst-eng/moved_chicago_weather_2017.html

The DataFrame name should be weather_records and must be specified when searching:

attrs={"id": "weather_records"}.

 Print the entire DataFrame.

'''
import pandas as pd

url = 'https://practicum-content.s3.us-west-1.amazonaws.com/data-analyst-eng/moved_chicago_weather_2017.html'

attrs = {"id": "weather_records"}

weather_records = pd.read_html(url, attrs = attrs)[0]

weather_records = weather_records.rename(columns={
    'Date and time': 'ts',
    'Temperature': 'temperature',
    'Description': 'description'
})

weather_records['ts'] = pd.to_datetime(weather_records['ts'])

#weather_records.to_csv('weather_chicago.csv', index=False)
