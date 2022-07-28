#.........API AUTHENTICATION.........................
#How do you authentiate yourself
#....API KEY............
import requests
api_key = ""
api_url = "https://api.openweathermap.org/data/2.5/onecall"
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
    print("Bring Umbrella")
