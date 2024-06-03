from pydantic import BaseModel

class WeatherRequest(BaseModel):
    city: str
    output_format: str

class WeatherResponse(BaseModel):
    Weather: str
    Latitude: str
    Longitude: str
    City: str
