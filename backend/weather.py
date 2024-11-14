import requests
from dotenv import load_dotenv
import os
# tomorrow.io is another potential weather API choice

# Load OpenWeatherMap API key from .env file
load_dotenv()
API_KEY = os.getenv("API_KEY")

# OpenWeatherMap's weather API call requires latitude and longitude
# Use OpenWeatherMap's geocoding API for this 
def get_lat_lon(city_name, state_code, country_code, api_key):
    location_response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={api_key}")

    # For testing purposes
    print(location_response)
    print(location_response.json())

# Example call
get_lat_lon("Dallas", "TX", "US", API_KEY)

# This function takes in the latitude and longitude of a location and the API key
# It returns the weather at said location
# Weather data can be excluded in &exclude={}
def get_weather(lat, lon, api_key):
    #weather_response = requests.get(f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={api_key}")
    pass