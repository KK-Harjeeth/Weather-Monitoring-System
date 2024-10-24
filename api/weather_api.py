import sys
import os
import requests
import time

# Add the root directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.config import API_KEY

CITY_IDS = {
    "Delhi": 1273294,
    "Mumbai": 1275339,
    "Chennai": 1264527,
    "Bangalore": 1277333,
    "Kolkata": 1275004,
    "Hyderabad": 1269843
}

class WeatherAPI:
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

    def get_weather_data(self, city_id):
        params = {
            'id': city_id,
            'appid': API_KEY,
            'units': 'metric'  # default is Celsius
        }
        response = requests.get(self.BASE_URL, params=params)
        print(f"Fetching weather for city ID {city_id}, Status Code: {response.status_code}")

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}, Response: {response.text}")
            return None

    def get_all_cities_weather(self):
        city_data = {}
        for city, city_id in CITY_IDS.items():
            data = self.get_weather_data(city_id)
            if data:
                print(f"Weather data for {city}: {data}")
                city_data[city] = data
            else:
                print(f"Failed to get data for {city}")
        return city_data

if __name__ == "__main__":
    api = WeatherAPI()
    while True:
        weather_data = api.get_all_cities_weather()
        print(weather_data)
        time.sleep(300)  # 5-minute interval
