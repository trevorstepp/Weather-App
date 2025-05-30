# Weather App (In Progress)
# Description
This is a simple web application where the user enters their city state to get basic weather information, such as temperature, precipitation, wind, and more using OpenWeatherMap's free API.  

The backend is done in Python with FastAPI as the web framework. The project first uses OpenWeatherMap's Geocoding API to fetch the latitude and longitude, which it then uses for OpenWeatherMap's free weather API. Currently, the data will simply be returned to the frontend to be displayed, but in the future I hope to use Python libraries to analyze and transform the data.

The frontend is done in vanilla HTML, CSS, and JavaScript.
# Requirements
An OpenWeatherMap API key is required for this project.

This API key should be placed in an .env file as shown in the .env.example file.
