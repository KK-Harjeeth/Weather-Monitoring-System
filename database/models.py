import sqlite3
from datetime import datetime

DB_NAME = "weather_data.db"

class WeatherDatabase:

    def __init__(self):
        self.conn = sqlite3.connect(DB_NAME)  # Creates or opens a connection to the SQLite database

    def insert_raw_weather_data(self, city, data):
        query = """
        INSERT INTO raw_weather_data (city, temperature, feels_like, condition, wind_speed, timestamp)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        self.conn.execute(query, (
            city,
            data["main"]["temp"],
            data["main"]["feels_like"],
            data["weather"][0]["main"],
            data["wind"]["speed"],
            data["dt"]
        ))
        self.conn.commit()

    def get_daily_summary(self, city, date_str):
        """
        Fetches the daily summary from the database for the given city and date.
        """
        query = """
        SELECT average_temp, max_temp, min_temp, dominant_condition
        FROM daily_weather_summary
        WHERE city = ? AND date = ?
        """
        cursor = self.conn.execute(query, (city, date_str))
        row = cursor.fetchone()
        if row:
            return {
                "average_temp": row[0],
                "max_temp": row[1],
                "min_temp": row[2],
                "dominant_condition": row[3]
            }
        else:
            return None

    def close(self):
        self.conn.close()

if __name__ == "__main__":
    db = WeatherDatabase()
    # Example: Insert raw weather data or perform other actions here
    db.close()
