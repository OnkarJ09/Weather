import requests
import json

def get_weather(location):
    api_key = '1b86abaedd0604dce27bfbc2b40ae211'
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': location, 'appid': api_key, 'units': 'metric'}
    response = requests.get(base_url, params=params)
    data = response.json()
    temperature = str(data['main']['temp'])
    humidity = str(data['main']['humidity'])
    weather_conditions = str(data['weather'][0]['description'])
    print(f"the weather condition in '{location}' city is:'{weather_conditions}' tempearture is:'{temperature}°C' and humidity is:'{humidity}%'")

    get_weather(input("Enter the location of the city you want to know the weather of: "))
