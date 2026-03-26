import requests

class WeatherService:
    def __init__(self, api_key=None):
        self.api_key = api_key
        self.base_url = "https://api.open-meteo.com/v1/forecast"

    def get_weather(self, latitude, longitude):
        """Fetches current weather for given coordinates using Open-Meteo API."""
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "current_weather": True
        }
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            return response.json().get("current_weather")
        else:
            return None

def format_weather(data):
    if not data:
        return "Could not fetch weather data."
    return f"Temperature: {data['temperature']}°C\nWindspeed: {data['windspeed']} km/h"
