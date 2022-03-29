import requests
import pprint
from datetime import datetime
# the activity is broken use this as a mock response 
weatherMockResponse = {
    "description": "Partly cloudy",
    "forecast": [
        {"day": 1, "temperature": "+22 C", "wind": "12 km/h"},
        {"day": 2, "temperature": " C", "wind": "14 km/h"},
        {"day": 3, "temperature": "5 C", "wind": " km/h"}
    ],
    "temperature": "21 C",
    "wind": "9 km/h"
}
#make a request to weather Api
#API is broken returns 404 not found...
#API_URL = "https://goweather.herokuapp.com/weather/" 
# I wrote this node api that gives the mock response above 
API_URL = "https://weather-api-node-wisc.herokuapp.com/weather/seattle"
city = "seattle"
r = requests.get(API_URL + city)
response = r.json()
print(response)

forecast_list = response['forecast']
today = datetime.now().strftime("%b-%d-%Y")

# make data in format for graphing library
to_graph = {}
#trakc day past current dt
count = 1

for day in forecast_list:
    current_date = int(today[4:6]) + count
    #the activity incorrectly shows you this_day = f"{today[0:4]}{current_date}{this_day[6:]}"
    #correct line is below since this_day is being defined so you can't refrenece itself
    this_day = f"{today[0:4]}{current_date}{today[6:]}"
    count+=1 if current_date <= 31 else 1
    to_graph[this_day] = day['wind']

print(to_graph)