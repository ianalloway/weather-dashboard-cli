import requests

class WeatherService:
    def __init__(self):
        self.weather_url = "https://api.open-meteo.com/v1/forecast"
        self.geocoding_url = "https://geocoding-api.open-meteo.com/v1/search"

    def get_coordinates(self, city_name):
        """Converts a city name to latitude and longitude using Open-Meteo Geocoding API."""
        params = {
            "name": city_name,
            "count": 1,
            "language": "en",
            "format": "json"
        }
        try:
            response = requests.get(self.geocoding_url, params=params, timeout=10)
            response.raise_for_status()
            results = response.json().get("results")
            if results:
                return results[0]["latitude"], results[0]["longitude"], results[0]["name"]
            return None, None, None
        except requests.exceptions.RequestException as e:
            print(f"Error fetching coordinates: {e}")
            return None, None, None

    def get_weather(self, latitude, longitude):
        """Fetches current weather for given coordinates using Open-Meteo API."""
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "current_weather": True
        }
        try:
            response = requests.get(self.weather_url, params=params, timeout=10)
            response.raise_for_status()
            return response.json().get("current_weather")
        except requests.exceptions.RequestException as e:
            print(f"Error fetching weather: {e}")
            return None

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def format_weather(data, city_name, unit="C"):
    if not data:
        return "Could not fetch weather data."
    
    temp = data['temperature']
    if unit.upper() == "F":
        temp = celsius_to_fahrenheit(temp)
        unit_str = "°F"
    else:
        unit_str = "°C"
        
    return (f"Current Weather for {city_name}:\n"
            f"Temperature: {temp:.1f}{unit_str}\n"
            f"Windspeed: {data['windspeed']} km/h")
