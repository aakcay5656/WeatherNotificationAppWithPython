import requests
from twilio.rest import Client


AccountSID ="Your Account SID"
AuthToken = "Your Account Token"
api_key = "Your Account Api key"
OWM_Enpoint = "https://api.openweathermap.org/data/2.5/forecast"
lat = 40.9167
lon = 39.8333


weather_params = {

        "lat":lat,
         "lon":lon,
        "appid":api_key,
        "cnt":4

}

data = requests.get(OWM_Enpoint,params =weather_params)
data.raise_for_status()
weather_data = data.json()



will_rain = False
for hour_data in weather_data["list"] :
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code)<700:
        will_rain = True


if will_rain:
    client = Client(AccountSID,AuthToken)
    message = client.messages.create(
            body = "Join Earth's mightiest heroes. Like Kevin Bacon.",
        from_='YOUR TWILIO VIRTUAL NUMBER',
        to='YOUR TWILIO VERIFIED REAL NUMBER'
        )
    print(message.status)