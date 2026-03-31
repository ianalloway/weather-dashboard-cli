import sys
from weather import WeatherService, format_weather

def main():
    service = WeatherService()
    
    if len(sys.argv) < 3:
        print("Usage: python main.py [latitude] [longitude]")
        print("Example: python main.py 40.7128 -74.0060")
        return

    try:
        lat = float(sys.argv[1])
        lon = float(sys.argv[2])
    except ValueError:
        print("Error: Latitude and longitude must be numbers.")
        return

    print(f"Fetching weather for ({lat}, {lon})...")
    weather_data = service.get_weather(lat, lon)
    print(format_weather(weather_data))

if __name__ == "__main__":
    main()
