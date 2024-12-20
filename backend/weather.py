import requests
import os
from dotenv import load_dotenv
# tomorrow.io is another potential weather API choice

# Load OpenWeatherMap API key from .env file
load_dotenv()
API_KEY = os.getenv("API_KEY")

# OpenWeatherMap's weather API call requires latitude and longitude
# Use OpenWeatherMap's geocoding API for this 
def get_lat_lon(city_name: str, state_code: str, country_code: str):
    # Get location info (lat and lon)
    location_response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_KEY}")
    return location_response

# Example call
info = get_lat_lon("Dallas", "TX", "US")

# This function takes in the latitude and longitude of a location and the API key
# It returns the weather at said location
# Weather data can be excluded in &exclude={}
def get_weather(lat: float, lon: float, exclude = None):
    # Get weather
    weather_response = requests.get(f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={exclude}&appid={API_KEY}")
    return weather_response