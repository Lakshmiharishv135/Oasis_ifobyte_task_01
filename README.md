```markdown
# Weather Application

This is a command-line-based weather application that fetches the current weather information based on user-provided location data. The application uses Geopy to convert location names into latitude and longitude, and the OpenWeatherMap API to get real-time weather details such as temperature, humidity, and weather conditions.

## Features
- Converts location name to latitude and longitude using Geopy.
- Fetches real-time weather information from the OpenWeatherMap API.
- Displays temperature, humidity, and weather conditions.
- Handles errors gracefully (e.g., invalid location, network errors).

## Prerequisites
- Python 3.x
- Install the required Python libraries:
    - `geopy`: Used for geocoding location names into coordinates.
    - `requests`: Used to make HTTP requests to the OpenWeatherMap API.

### Install the required libraries via pip:
```bash
pip install geopy requests
```

## Setup
1. **Get an API Key** from [OpenWeatherMap](https://openweathermap.org/api). This API key is required to fetch weather data.

2. **Clone the repository**:
```bash
git clone https://github.com/your_username/weather_app.git
```

3. **Add your OpenWeatherMap API Key** in the `main()` function of the script:
```python
api_key = "Enter Your API KEY"
```

## Usage
1. Run the script:
```bash
python weather_app.py
```

2. Enter your location when prompted, and the application will display the following:
   - Temperature (in Celsius)
   - Humidity (percentage)
   - Weather conditions (e.g., clear sky, rain, etc.)

Example:
```bash
Enter your location: New York
Coordinates for New York: Latitude=40.7128, Longitude=-74.0060
Temperature: 25°C
Humidity: 60%
Weather Conditions: Clear sky
```

## Error Handling
- The application provides meaningful error messages if:
  - The location is not found.
  - The API request fails (e.g., network issue or incorrect API key).
  - Weather data cannot be processed due to missing or unexpected fields.

