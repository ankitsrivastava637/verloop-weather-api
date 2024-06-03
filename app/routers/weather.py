from fastapi import APIRouter, HTTPException
from app.utils import fetch_weather_data, parse_weather_data
from app.schemas import WeatherRequest, WeatherResponse

router = APIRouter()

@router.post("/getCurrentWeather")
async def get_current_weather(request: WeatherRequest):
    try:
        data = await fetch_weather_data(request.city)
        response_data = parse_weather_data(data, request.output_format)
        return response_data
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
