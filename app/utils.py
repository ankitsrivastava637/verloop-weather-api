import io
import json
import logging
import requests
import xml.etree.ElementTree as ET
from app.schemas import WeatherResponse

logger = logging.getLogger(__name__)

def load_config(file_path: str) -> dict:
    with open(file_path, "r") as f:
        return json.load(f)

CONFIG = load_config("config/config.json")

API_KEY = CONFIG.get("API_KEY")
API_ENDPOINT = CONFIG.get("API_ENDPOINT")
API_HOST = CONFIG.get("API_HOST")

if not API_KEY:
    logger.error("API_KEY not found in config file")
    raise ValueError("API_KEY not found in config file")
if not API_ENDPOINT:
    logger.error("API_ENDPOINT not found in config file")
    raise ValueError("API_ENDPOINT not found in config file")
if not API_HOST:
    logger.error("API_HOST not found in config file")
    raise ValueError("API_HOST not found in config file")

async def fetch_weather_data(city: str) -> dict:
    headers = {
        "x-rapidapi-key": API_KEY,
        "x-rapidapi-host": API_HOST
    }
    params = {"q": city}
    try:
        response = requests.get(API_ENDPOINT, headers=headers, params=params)
        response.raise_for_status()  # Raise exception for non-200 status codes
        return response.json()
    except Exception as e:
        logger.error(f"Failed to fetch weather data for {city} from WeatherAPI: {str(e)}")
        raise

def parse_weather_data(data: dict, output_format: str) -> str:
    if output_format.lower() == "json":
        return {
            "Weather": data["current"]["temp_c"],
            "Latitude": data["location"]["lat"],
            "Longitude": data["location"]["lon"],
            "City": data["location"]["name"]
        }
    elif output_format.lower() == "xml":
            # Create the root element
        root = ET.Element("root")
        
        # Create sub-elements
        temperature = ET.SubElement(root, "Temperature")
        temperature.text = str(data["current"]["temp_c"])
        
        city = ET.SubElement(root, "City")
        city.text = data["location"]["name"]
        
        lat = ET.SubElement(root, "Latitude")
        lat.text = str(data["location"]["lat"])
        
        lon = ET.SubElement(root, "Longitude")
        lon.text = str(data["location"]["lon"])
        
        # Create an ElementTree object
        tree = ET.ElementTree(root)
        
        # Write to a bytes buffer with encoding and XML declaration
        xml_buffer = io.BytesIO()
        tree.write(xml_buffer, encoding="utf-8", xml_declaration=True)
        
        # Get the XML string from the buffer
        xml_data = xml_buffer.getvalue()
        
        return xml_data
    else:
        raise ValueError("Invalid output format specified")
