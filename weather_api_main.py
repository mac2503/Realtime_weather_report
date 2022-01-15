import requests
from datetime import datetime

user_api = 'API_KEY'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api
api_link = requests.get(complete_api_link)
api_data = api_link.json()

# Create variables to store & display data
temperature = ((api_data['main']['temp']) - 273.15)
weather_description = api_data['weather'][0]['description']
humidity = api_data['main']['humidity']
wind_speed = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")

print ("Current temperature is: {:.2f} deg C".format(temperature))
print ("Current weather desc  :", weather_description)
print ("Current Humidity      :", humidity, '%')
print ("Current wind speed    :", wind_speed, 'kmph')
