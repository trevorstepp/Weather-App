import requests
import os
from dotenv import load_dotenv
# tomorrow.io is another potential weather API choice

# Load OpenWeatherMap API key from .env file
load_dotenv()
API_KEY = os.getenv("API_KEY")

# OpenWeatherMap's weather API call requires latitude and longitude
# Use OpenWeatherMap's geocoding API for this 
def get_lat_lon(city_name: str, state_code: str = "", country_code: str = "", limit: int = 0):
    # Get location info (lat and lon)
    location_response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&limit={limit}&appid={API_KEY}")
    return location_response

# Example call
info = get_lat_lon(city_name="London", limit=1)
#print(info.json())

# This function takes in the latitude and longitude of a location and the API key
# It returns the current weather at said location
def get_curr_weather(lat: float, lon: float):
    weather_response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}")
    return weather_response

"""
resp1 = get_curr_weather(info.json()[0]['lat'], info.json()[0]['lat'])
#print(resp.json())
"""

# This function takes in the latitude and longitude of a location and the API key
# It returns the forecast at said location
def get_forecast(lat: float, lon: float):
    forecast_response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}")
    return forecast_response