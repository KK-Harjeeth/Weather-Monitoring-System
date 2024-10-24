# Directory: weather-monitoring-system
#
# The structure below will represent each file as a section, explaining its purpose and content with Python code implementation.



# 3. api/alerts.py
# Alert system for notifying when weather conditions surpass thresholds.

class WeatherAlertSystem:
    
    def __init__(self, threshold_temp=35):
        self.threshold_temp = threshold_temp
        self.alert_triggered = False

    def check_threshold(self, city, temp):
        if temp > self.threshold_temp:
            print(f"ALERT: {city} temperature exceeded {self.threshold_temp} degrees Celsius! Current temperature: {temp}")
            self.alert_triggered = True
            # You could add functionality to send an email notification here










# 8. README.md

"""
# Weather Monitoring System

## Project Overview
This project monitors real-time weather data from OpenWeatherMap for major metros in India. It retrieves data, processes it, generates rollups and aggregates, and alerts based on thresholds.

## Installation
1. Clone this repository.
2. Set up a virtual environment and install dependencies with:
   ```
   pip install -r requirements.txt
   ```
3. Obtain an OpenWeatherMap API key and set it in `config/config.py`.
4. Run the database setup using `python database/db_setup.py`.

## Run Instructions
1. Start the API data retrieval by running `python api/weather_api.py`.
2. Data will be stored and processed, and alerts will be triggered if thresholds are breached.
3. Use `visualizations/trends.py` to generate visual insights.

## Dependencies
- `requests` for API calls.
- `sqlite3` for database interactions.
- `matplotlib` for visualizations.

## Docker Setup
- Build the image with:
  ```
  docker build -t weather-monitor .
  ```
- Run the container:
  ```
  docker run -p 5000:5000 weather-monitor
  ```

## Design Choices
- SQLite is used for easy prototyping. For production, consider PostgreSQL.
- Modular design for easy maintenance and upgrades.
"""


# End of Files

# Notes:
# - Replace placeholders like `your_openweathermap_api_key_here` with your actual API keys.
# - Extend the system based on bonus requirements as needed.
