#.........API AUTHENTICATION.........................
#How do you authentiate yourself
#....API KEY............
import requests
import os
from twilio.rest import Client
api_key = os.environ.get("OWM_API")
api_url = "https://api.openweathermap.org/data/2.5/onecall"
account_sid = os.environ.get("TWILO_ACCT_SID")
auth_token = os.environ.get("TWILO_AUTH_TOKEN")


parameters = {
    "lat":37.964252,
    "lon": -91.831833,
    "appid":api_key,
    "exclude": "current,minutely,daily"
}
response = requests.get(api_url, params=parameters)
response.raise_for_status()
#print(response.status_code)
weather_data = response.json()
hourly_data = weather_data["hourly"]

will_rain = False
for hour_data in range(len(hourly_data)-35): # Use SLICE instaed for hour_data in hourly_data[:12]
    condition_code = hourly_data[hour_data]["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today, Remember to bring an Umbrella ☂️",
        from_='+12059463647',
        to='+18166026168'
    )

    print(message.status)
