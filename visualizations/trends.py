import matplotlib.pyplot as plt
import sys
import os

# Add the root directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.models import WeatherDatabase

class WeatherVisualizer:

    def plot_daily_summary(self, city):
        """
        Plot a bar chart for the daily weather summary of a city using real data from the database.
        
        Args:
        - city (str): Name of the city.
        """
        db = WeatherDatabase()
        # Fetch the latest daily summary from the database for the given city
        summary = db.get_daily_summary(city, "2024-10-24")  # Assuming you have a method like this in models.py
        if summary:
            labels = ["Average Temp", "Max Temp", "Min Temp"]
            values = [summary["average_temp"], summary["max_temp"], summary["min_temp"]]
            colors = ['blue', 'red', 'green']

            plt.bar(labels, values, color=colors)
            plt.title(f"Daily Weather Summary for {city}")
            plt.ylabel("Temperature (Celsius)")
            plt.grid(axis='y', linestyle='--', alpha=0.7)  # Adding gridlines for better readability
            plt.savefig(f'daily_weather_summary_{city.lower()}.png')
            plt.show()

    def plot_historical_trends(self, city, historical_data):
        """
        Plot a line chart for historical temperature trends of a city.
        
        Args:
        - city (str): Name of the city.
        - historical_data (list of dicts): Each entry should contain "date" and "average_temp".
        """
        dates = [entry["date"] for entry in historical_data]
        temps = [entry["average_temp"] for entry in historical_data]

        plt.plot(dates, temps, marker='o')  # Adding markers to show individual data points
        plt.title(f"Historical Temperature Trends for {city}")
        plt.xlabel("Date")
        plt.ylabel("Average Temperature (Celsius)")
        plt.xticks(rotation=45)
        plt.grid(axis='y', linestyle='--', alpha=0.7)  # Adding gridlines
        plt.show()

if __name__ == "__main__":
    visualizer = WeatherVisualizer()
    # Example usage:
    city = "Delhi"
    # Plot daily summary using real data from the database
    visualizer.plot_daily_summary(city)
    
    # Example historical data for visualization
    historical_data = [
        {"date": "2024-10-20", "average_temp": 29},
        {"date": "2024-10-21", "average_temp": 31},
        {"date": "2024-10-22", "average_temp": 28}
    ]
    
    # To visualize historical trends for the city
    visualizer.plot_historical_trends(city, historical_data)
