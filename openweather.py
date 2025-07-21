import requests

API_KEY = "openweathermap api key here"
LOCATION = "Los Angeles, CA, US"

# Build query
location = f"{LOCATION}"
url = "http://api.openweathermap.org/data/2.5/weather"
params = {
    "q": location,
    "appid": API_KEY,
    "units": "metric"  # Optionally "imperial" for Fahrenheit
}

# Make request
response = requests.get(url, params=params)
data = response.json()

# Parse and print
if data.get("cod") == 200:
    weather = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]
    temp_c = data["main"]["temp"]
    temp_f = (temp_c * 9/5) + 32
    wind_mps = data["wind"]["speed"]
    wind_mph = wind_mps * 2.23694
    #temp = data["main"]["temp"]
    #wind = data["wind"]["speed"]

    print(f"📍 {location}")
    print(f"🗺️  Geo coords: {data['coord']['lat']}, {data['coord']['lon']}")
    print(f"🌡️  Temp: {temp_c:.2f}°C / {temp_f:.2f}°F")
    print(f"🌥️  Conditions: {weather}")
    print(f"🌬️  Wind: {wind_mps:.2f} m/s / {wind_mph:.2f} mph")
    print(f"💧 Humidity: {humidity}%")
    print(f"🚀 Powered by OpenWeatherMap API")
else:
    print("❌ Location not found or API error.")
