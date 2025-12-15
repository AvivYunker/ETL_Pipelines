import pandas as pd
import json
import requests
from datetime import datetime

TOKEN = "30a3836d40a27d400d4e8218229d173e"
LAT = "32.10846916666665"
LON = "34.96419472222222"

URL = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={TOKEN}"

response = requests.get(URL)
print(response.status_code)

data = response.json()

record = {
    "city": data["name"],
    "temp_celcius": data["main"]["temp"] - 273.15,
    "humidity": data["main"]["humidity"],
    "weather_description": data["weather"][0]["description"],
    "wind_speed": data["wind"]["speed"],
    "date": datetime.utcfromtimestamp(data["dt"])
}

df = pd.DataFrame([record])
print(df)