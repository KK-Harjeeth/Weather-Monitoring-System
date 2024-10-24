# Weather Monitoring System

## Overview
The **Weather Monitoring System** is a real-time weather data collection, analysis, and visualization tool. It collects weather data from the OpenWeatherMap API for several major cities in India, processes the data to create daily summaries, triggers alerts for specific conditions, and generates insightful visualizations.

The key features of the system include:
- **Real-time Data Collection**: Collects weather data from OpenWeatherMap for Delhi, Mumbai, Chennai, Bangalore, Kolkata, and Hyderabad.
- **Daily Summaries**: Generates daily summaries including average, maximum, and minimum temperatures.
- **Alerts**: Triggers alerts based on user-defined temperature thresholds.
- **Visualizations**: Visualizes historical trends and daily summaries for each city.

## Prerequisites
1. **Python 3.8+**
2. **Virtual Environment** (recommended for dependency management)
3. **API Key** for OpenWeatherMap (sign up at [OpenWeatherMap](https://openweathermap.org/))
4. **SQLite** (comes with Python)

## Project Structure
```
weather-monitoring-system/
├── api/
│   ├── weather_api.py           # Collects weather data from OpenWeatherMap
│   ├── data_processor.py        # Handles data aggregation and processing
│   └── alerts.py                # Contains alert logic
├── database/
│   ├── db_setup.py              # Setup and initialization of the SQLite database
│   └── models.py                # Database operations
├── visualizations/
│   ├── trends.py                # Historical trends and daily summaries visualization
├── config/
│   └── config.py                # API keys and configurations
├── tests/
│   ├── test_api.py              # Unit tests for API
│   ├── test_conversion.py       # Unit tests for data processing and conversion
└── README.md                    # Project documentation
```

## Setup and Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd weather-monitoring-system
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate    # For macOS/Linux
   # For Windows:
   # venv\Scripts\activate
   ```

3. **Install Dependencies**:
   Create a `requirements.txt` file with the following content:
   ```
   requests
   matplotlib
   ```
   Then install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API Key**:
   - Navigate to `config/config.py`.
   - Add your **OpenWeatherMap API key**.
   ```python
   API_KEY = "your_openweathermap_api_key_here"
   ```

5. **Set Up the Database**:
   - Run the database setup script to create the required tables.
   ```bash
   python database/db_setup.py
   ```

## Running the Project

### 1. **Collect Weather Data**
To collect real-time weather data continuously:
```bash
python api/weather_api.py
```
- This will fetch weather data for the specified cities every 5 minutes and store it in `weather_data.db`.

### 2. **Generate Daily Summaries**
To process the collected raw data into daily summaries:
```bash
python api/data_processor.py
```
- Run this at the end of the day to generate daily summaries for each city.

### 3. **Trigger Alerts**
To check for any threshold breaches and trigger alerts:
```bash
python api/alerts.py
```
- This script will check conditions such as temperature thresholds and print alerts to the console.

### 4. **Visualize Data**
To visualize historical trends and daily summaries:
```bash
python visualizations/trends.py
```
- This will generate charts showing temperature trends and other weather-related visualizations.

## Example Usage
1. **Weather Data Collection**: Run `weather_api.py` continuously to collect data every 5 minutes.
2. **Daily Summaries**: Run `data_processor.py` at the end of each day to summarize the data.
3. **Alert Generation**: Use `alerts.py` to get notified if the weather exceeds certain thresholds.
4. **Visualizations**: Run `trends.py` to create graphs for daily summaries and historical trends.

## Automation Tips
- **Automate Data Collection** using a scheduler:
  - Use `cron` on Unix/macOS or Task Scheduler on Windows to run `weather_api.py` every 5-10 minutes.
  - Schedule `data_processor.py` at the end of each day to generate summaries.

## Testing
To run unit tests, use:
```bash
python -m unittest discover tests
```
- **`test_api.py`**: Tests the API calls and response parsing.
- **`test_conversion.py`**: Tests data processing and conversion functions.

## Future Improvements
- **Deploy a Dashboard**: Use **Streamlit** or **Dash** to create an interactive web-based dashboard for visualizations.
- **Add Notifications**: Send alerts via email using SMTP or SMS using Twilio.
- **Compare Cities**: Visualize comparisons of weather data across multiple cities in a single graph.

## License
This project is licensed under the MIT License.

## Acknowledgments
- **OpenWeatherMap**: For providing the weather data.
- **Matplotlib**: For visualization.

## Contact
For any questions, contact **Harjeeth Kuchar Kal** at kkharjeeth@gmail.com
