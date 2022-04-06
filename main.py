import requests
import os
from twilio.rest import Client

account_sid = 'account sid'
auth_token = "account token"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "api key"
ciudad = "Buenos%20Aires"

response = requests.get(url=f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}")
response.raise_for_status()

weather_params = {
    "lon": -58.381557,
    "lat": -34.603683,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}
print(weather_params)
api2 = requests.get(OWM_Endpoint, params=weather_params)
api2.raise_for_status()
weather_data = api2.json()

id2slice = weather_data["hourly"][:12]
id2 = weather_data["hourly"][12]["weather"][0]["id"]}
lluvia = False
for hour_data in id2slice:
    condition_code = (hour_data["weather"][0]["id"])
    if int(condition_code) < 700:
        lluvia = True
if lluvia:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Hoy llueve Gato, recuerda llevar impermeable.",
        from_='+19036485177',
        to='+my number'
    )
    print(message.status)
