from geopy.geocoders import Nominatim
import requests
import sys

# Function to get latitude and longitude using geopy
def get_location(location):
    try:
        geolocator=Nominatim(user_agent="weather_app")
        location_data=geolocator.geocode(location)
        if location_data:
            return location_data.latitude, location_data.longitude
        else:
            raise ValueError("Location not found. Please try again.")
    except Exception as e:
        print(f"Error finding location: {e}")
        sys.exit()

# Function to get weather information using OpenWeatherMap API
def get_weather_info(lat, lon, api_key):
    try:
        url=f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
        response=requests.get(url)
        response.raise_for_status()  
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        sys.exit()

# Function to display weather details
def display_weather(weather_data):
    try:
        temperature=weather_data['main']['temp']
        humidity=weather_data['main']['humidity']
        weather_condition=weather_data['weather'][0]['description']
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather Conditions: {weather_condition.capitalize()}")
    except KeyError as e:
        print(f"Error processing weather data: {e}")
        sys.exit()

# Main function
def main():
    api_key="Enter Your API KEY"  # Add your OpenWeatherMap API key here
    
    location=input("\nEnter your location: ")
    lat, lon=get_location(location)
    
    print(f"Coordinates for {location}: Latitude={lat}, Longitude={lon}")
    
    weather_data = get_weather_info(lat, lon, api_key)
    display_weather(weather_data)

if __name__=="__main__":
    try:
        while 1:
            main()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
