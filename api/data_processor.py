from datetime import datetime

class WeatherDataProcessor:

    def __init__(self):
        self.daily_summaries = {}

    def process_weather_data(self, city, data):
        date_str = datetime.now().strftime("%Y-%m-%d")
        temp = data["main"]["temp"]
        main_condition = data["weather"][0]["main"]
        
        if city not in self.daily_summaries:
            self.daily_summaries[city] = {}
        if date_str not in self.daily_summaries[city]:
            self.daily_summaries[city][date_str] = {
                "temperatures": [],
                "conditions": []
            }
        
        self.daily_summaries[city][date_str]["temperatures"].append(temp)
        self.daily_summaries[city][date_str]["conditions"].append(main_condition)

    def calculate_daily_summary(self, city, date_str):
        city_data = self.daily_summaries[city][date_str]
        avg_temp = sum(city_data["temperatures"]) / len(city_data["temperatures"])
        max_temp = max(city_data["temperatures"])
        min_temp = min(city_data["temperatures"])
        dominant_condition = max(set(city_data["conditions"]), key=city_data["conditions"].count)

        return {
            "average_temp": avg_temp,
            "max_temp": max_temp,
            "min_temp": min_temp,
            "dominant_condition": dominant_condition
        }
