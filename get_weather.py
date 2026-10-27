import requests
import pandas as pd

url = "https://archive-api.open-meteo.com/v1/archive"
params = {
    "latitude": 43.65,
    "longitude": -79.38,
    "start_date": "2024-01-01",
    "end_date": "2024-12-31",
    "daily": "temperature_2m_mean,precipitation_sum,snowfall_sum,wind_speed_10m_max",
    "timezone": "America/Toronto",
}

r = requests.get(url, params=params)
r.raise_for_status()
df = pd.DataFrame(r.json()["daily"])
df.to_csv("data/weather_2024.csv", index=False)
print(df.head())