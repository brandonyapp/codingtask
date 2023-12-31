import requests
import sys
# OpenWeatherMap API base URL and API key
base_url = "https://api.openweathermap.org/data/2.5/weather?"
api = "f78ed7b94a63a1d54e616bfdd446f640"
# Get user input for the city
city = input("Enter the name of a city for which you want to get the weather information:")
print("Weather in " + city )
# Function to convert temperature from Kelvin to Celsius
def kelvin_to_celsius(kelvin): 
    celsius = kelvin - 273.15
    return celsius
# Construct the URL for the API request
url = base_url + "appid=" + api + "&q=" + city


try:
    # Make the API request and parse the JSON response
    response = requests.get(url).json()
except requests.exceptions.RequestException as e:
     # Handle exceptions related to the request
    print(f"Error fetching data: {e}")
    sys.exit(1)
# Check if the city was found in the response
if 'main' not in response:
    print(f"City not found: {city}")
    sys.exit(1)

# Extract weather information from the response
temp_kelvin = response['main']['temp']
temp_celsius = kelvin_to_celsius(temp_kelvin)
humidity = response['main']['humidity']
windspeed = response['wind']['speed']
description = response['weather'][0]['description']

# Display weather information
print(f"-Temperature: {temp_celsius:.1f}°C")
print(f"-Humidity: {humidity}%")
print(f"-Wind Speed {windspeed}m/s")
print(f"-Description: {description}")

