###########################################################
######### Something a little more challenging #############
###########################################################

import requests

def get_weather_data(city):
    """
    Simulates an API call to fetch weather data
    """
    response = requests.get(f'https://api.weather.com/data/{city}')
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to fetch weather data")

def analyze_weather(city):
    """
    Perform analysis on weather data
    """
    data = get_weather_data(city)

    if data['temperature'] > 25 and data['humidity'] < 70:
        return "Hot and dry"
    elif data['temperature'] < 10:
        return "Cold"
    else:
        return "Moderate"
