import requests, json
from datetime import datetime

API_KEY = "00cffbfc124fd0ba32a4eaa89d7f7860"
cities = ["Lahore", "Islamabad", "Multan", "Depalpur", "Okara", "Basirpur"]

def fetch_weather(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        data = requests.get(url).json()
        return {
            "city": city,
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"],
            "sunrise": data["sys"]["sunrise"],
            "sunset": data["sys"]["sunset"]
        }
    except Exception as e:
        print(f"Error fetching {city}: {e}")
        return {
            "city": city,
            "temperature": 0,
            "humidity": 0,
            "description": "N/A",
            "sunrise": 0,
            "sunset": 0
        }

all_weather = [fetch_weather(c) for c in cities]
last_update = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

data = {
    "last_update": last_update,
    "cities": all_weather
}

with open("weather.json","w") as f:
    json.dump(data,f,indent=2)

print("Weather updated for all cities at", last_update)
