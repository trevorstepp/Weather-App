# Main file of app that contains all FastAPI functionality
from fastapi import FastAPI, status, HTTPException
import weather, schemas

app = FastAPI()

origins = []

app.add_middleware(
    
)

@app.get("/get-weather/", status_code=status.HTTP_200_OK, response_model=schemas.ReturnWeather)
def get_weather(location: schemas.GetWeather, exclude: str = None):

    city = location.city
    state = location.state
    country = location.country
    # Get latitude and longitude
    location_info = weather.get_lat_lon(city_name=city, state_code=state, country_code=country)

    # Use above to get the weather
    latitude = location_info[0]["lat"]
    longitude = location_info[0]["lon"]
    weather_info = weather.get_weather(lat=latitude, lon=longitude, exclude=exclude)

if __name__ == "__main__":
    pass