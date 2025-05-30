# pydantic schemas
from pydantic import BaseModel

class GetWeather(BaseModel):
    city: str
    state: str = ""
    country: str = ""
    limit: int = 0

class ReturnWeather(BaseModel):
    temp: float