# 4. database/db_setup.py
# Setting up the database.

import sqlite3

DB_NAME = "weather_data.db"

class DatabaseSetup:

    def __init__(self):
        self.conn = sqlite3.connect(DB_NAME)
        self.create_weather_table()

    def create_weather_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS daily_weather_summary (
            city TEXT,
            date TEXT,
            average_temp REAL,
            max_temp REAL,
            min_temp REAL,
            dominant_condition TEXT
        )
        """
        self.conn.execute(query)
        self.conn.commit()

if __name__ == "__main__":
    db_setup = DatabaseSetup()