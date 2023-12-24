# WeatherNotificationAppWithPython

This app is a simple weather notification app that can be used to get the weather forecast for a specific geographical location and send an SMS message if it is likely to rain. The code requires a properly configured API key and other information in your OpenWeatherMap and Twilio accounts to run. Once you provide this information, you can customize the code to suit your needs.

#### 1- First, the necessary libraries requests and twilio.rest are added.
#### 2- API keys and other information are assigned to variables. To get this information, you need to sign up for OpenWeatherMap and Twilio accounts and obtain the necessary keys.
#### 3- It uses the OpenWeatherMap API to retrieve weather data. The variables lat and lon represent a specific geographic location.
#### 4- Checks the status of the HTTP request (raise_for_status()) to verify the accuracy of the data received.
#### 5- Converts received JSON data into a Python dictionary.
#### 6- It creates a boolean variable named will_rain and checks the weather data and returns True if it is likely to rain.
#### 7- If will_rain is True, it sends an SMS message using the Twilio API.
