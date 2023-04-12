Weather Information Retrieval

This Python code retrieves weather information for a given city using an API. It prompts the user to enter a city name, makes an API call to fetch weather data in JSON format, and then parses the JSON data to extract relevant weather information such as temperature, atmospheric pressure, humidity, and weather description. If the city is found in the API response, the weather information is displayed. Otherwise, a "City not found" message is printed.
Requirements

    Python 3.x
    Requests (Python library for making HTTP requests)
    JSON (Python library for handling JSON data)

Usage

    Replace "API_key_here" with your actual API key in the api_key variable. You can obtain an API key from the respective weather API provider.
    Replace "base_url_variable" with the base URL of the weather API you are using.
    Run the script and enter the desired city name when prompted.
    The script will make an API call and retrieve weather information for the given city, if found.
    The retrieved weather information, including temperature, pressure, humidity, and weather description, will be printed to the console.
    If the city is not found in the API response, a "City not found" message will be displayed.

Customization

You can customize the weather API and API key by modifying the base_url and api_key variables in the script, respectively.


  # Enter the API key here
    api_key = "API_key_here"

  # base_url variable to store url
    base_url = "base_url_variable"

You may also customize the displayed weather information by modifying the print statement according to your needs.


# print the temperature
    print("Temperature (in Kelvin unit) = " +
      str(temperature) +
      "\nAtmospheric pressure (in hPa unit) = " +
      str(pressure) +
      "\nHumidity (in percentage) = " +
      str(humidity) +
      "\nDescription = " +
      str(weather_description))

Contributing

If you would like to contribute to this weather information retrieval code, feel free to submit a pull request with your improvements or open an issue for any bug reports or feature requests.
License

This weather information retrieval code is released under the MIT License, which allows for free use, modification, and distribution of the code. Please refer to the LICENSE file for more details.

Credits

This weather information retrieval code was created by Jean-Luc Affourtit and uses the Requests and JSON libraries for making API calls and handling JSON data, respectively.
