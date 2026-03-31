import requests

class WeatherService:
    def __init__(self):
        self.base_url = "https://api.open-meteo.com/v1/forecast"

    def get_weather(self, latitude, longitude):
        """Fetches current weather for given coordinates using Open-Meteo API."""
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "current_weather": True
        }
        try:
            response = requests.get(self.base_url, params=params, timeout=10)
            response.raise_for_status()
            return response.json().get("current_weather")
        except requests.exceptions.RequestException as e:
            print(f"Error fetching weather: {e}")
            return None

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def format_weather(data, unit="C"):
    if not data:
        return "Could not fetch weather data."
    
    temp = data['temperature']
    if unit.upper() == "F":
        temp = celsius_to_fahrenheit(temp)
        unit_str = "°F"
    else:
        unit_str = "°C"
        
    return (f"Current Weather:\n"
            f"Temperature: {temp:.1f}{unit_str}\n"
            f"Windspeed: {data['windspeed']} km/h")
