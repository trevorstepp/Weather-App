# Main file of app that contains all FastAPI functionality
from fastapi import FastAPI, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware # Needed since React is a different application, 
                                                   # need to enable cors (cross-origin resource sharing)
import weather, schemas

app = FastAPI()
"""
origins = [
    "http://localhost:3000",
    "localhost:3000"
] # Frontend origin

# Let FastAPI allow requests from React app (if I decide to use React)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"] 
)
"""

@app.get("/get-weather/", status_code=status.HTTP_200_OK, response_model=schemas.ReturnWeather)
def get_weather(location: schemas.GetWeather):

    city = location.city
    state = location.state
    country = location.country

    # Get latitude and longitude
    location_info = weather.get_lat_lon(city_name=city, state_code=state, country_code=country)

    latitude = location_info.json()[0]["lat"] # lat
    longitude = location_info.json()[0]["lon"] # lon

    # Retrieve current weather
    curr_weather = weather.get_curr_weather(lat=latitude, lon=longitude)

    # Retrieve weather forecast
    forecast = weather.get_forecast(lat=latitude, lon=longitude)

if __name__ == "__main__":
    pass