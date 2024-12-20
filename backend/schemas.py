# pydantic schemas
from pydantic import BaseModel

class GetWeather(BaseModel):
    city: str
    state: str
    country: str

class ReturnWeather(BaseModel):
    temp: float