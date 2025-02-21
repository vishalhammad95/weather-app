import requests

# Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
API_KEY = "YOUR_API_KEY"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        print(f"\n🌍 Weather in {city.capitalize()}:")
        print(f"🌡 Temperature: {temp}°C")
        print(f"☁️ Condition: {weather.capitalize()}")
        print(f"💧 Humidity: {humidity}%")
        print(f"💨 Wind Speed: {wind_speed} m/s")
    else:
        print("❌ City not found! Please enter a valid city name.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
