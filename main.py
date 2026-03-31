import sys
from weather import WeatherService, format_weather

def main():
    service = WeatherService()
    
    if len(sys.argv) < 2:
        print("Usage: python main.py [city_name] or [latitude] [longitude]")
        print("Example: python main.py 'New York' or python main.py 40.7128 -74.0060")
        return

    if len(sys.argv) == 2:
        city_input = sys.argv[1]
        print(f"Searching for city: {city_input}...")
        lat, lon, city_name = service.get_coordinates(city_input)
        if not lat:
            print(f"Error: Could not find coordinates for city '{city_input}'.")
            return
    elif len(sys.argv) >= 3:
        try:
            lat = float(sys.argv[1])
            lon = float(sys.argv[2])
            city_name = f"({lat}, {lon})"
        except ValueError:
            print("Error: Latitude and longitude must be numbers.")
            return
    
    print(f"Fetching weather for {city_name}...")
    weather_data = service.get_weather(lat, lon)
    print(format_weather(weather_data, city_name))

if __name__ == "__main__":
    main()
