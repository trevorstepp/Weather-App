import requests
from dotenv import load_dotenv
import os
# tomorrow.io is another option

load_dotenv()
API_KEY = os.getenv("API_KEY")

def get_lat_lon(city_name, state_code, country_code, api_key):
    location_response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={api_key}")

    print(location_response)
    print(location_response.json())

# Example call
get_lat_lon("Dallas", "TX", "US", API_KEY)

def get_weather(lat, lon, api_key):
    #weather_response = requests.get(f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={api_key}")
    pass