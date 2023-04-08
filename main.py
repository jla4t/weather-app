import requests
import json

# Enter the API key here
api_key = "API_key_here"

# base_url variable to store url
base_url = "base_url_variable"

# city_name variable to store the city name
city_name = input("Enter city name: ")

# complete_url variable to store the complete url address
complete_url = base_url + "appid=" + api_key + "&q=" + city_name

# get method of requests module return response object
response = requests.get(complete_url)

# json method of response object convert json format data into python format data
weather_data = json.loads(response.text)

# check the value of "cod" key in the returned JSON data. If it is not equal to "404", then the city is found
if weather_data["cod"] != "404":

    # store the value of "main" key in variable weather
    weather = weather_data["main"]

    # store the value corresponding to "temp" key of weather dictionary
    temperature = weather["temp"]

    # store the value corresponding to "pressure" key of weather dictionary
    pressure = weather["pressure"]

    # store the value corresponding to "humidity" key of weather dictionary
    humidity = weather["humidity"]

    # store the value of "weather" key in variable weather_description
    weather_description = weather_data["weather"][0]["description"]

    # print the temperature
    print("Temperature (in Kelvin unit) = " +
          str(temperature) +
          "\nAtmospheric pressure (in hPa unit) = " +
          str(pressure) +
          "\nHumidity (in percentage) = " +
          str(humidity) +
          "\nDescription = " +
          str(weather_description))
else:
    # if city not found
    print("City not found")