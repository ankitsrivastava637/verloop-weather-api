# Verloop Weather API

This is a simple API built with FastAPI to retrieve current weather data for a given city. It fetches weather information from the WeatherAPI.com service and returns the data in JSON or XML format based on the request.

## Getting Started

To run this project locally, follow these steps:

1. Clone this repository to your local machine.
2. Set up a virtual environment and install dependencies:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3. Set up your WeatherAPI.com API key and configure it in the `config.py` file.
4. Run the FastAPI application:

    ```bash
    uvicorn main:app --reload
    ```

5. For JSON FORMAT : Open your browser and navigate to `http://localhost:8000/docs` to access the Swagger UI for testing the API endpoints.

FOR XML : try through POSTMAN API PLATFORM

## API Endpoints

- `POST /getCurrentWeather`: Retrieve current weather data for a city.

    **Request Body:**

    ```json
    {
        "city": "Bangalore",
        "output_format": "json"
    }
    ```

    **Response JSON:**

    ```json
    {
        "Weather": "20 C",
        "Latitude": "12.9716",
        "Longitude": "77.5946",
        "City": "Bangalore India"
    }
    ```

    **Response XML:**

    ```xml
    <?xml version="1.0" encoding="UTF-8" ?>
    <root>
        <Temperature>24.0</Temperature>
        <City>Bangalore</City>
        <Latitude>12.98</Latitude>
        <Longitude>77.58</Longitude>
    </root>
    ```

## Configuration

Make sure to configure your WeatherAPI.com API key in the `config.json` file before running the application.


