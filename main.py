import requests
import os
from twilio.rest import Client

# Twilio Account Information
auth_token = os.environ.get("AUTH_TOKEN")
account_sid = os.environ.get("ACCOUNT_SID")

# OpenWeather Map Information
LAT = 33.94
LON = -84.31
API = os.environ.get("OWM_API_KEY")
END_POINT = "https://api.openweathermap.org/data/2.5/forecast"
CNT = 4

parameters = {
    "lat": LAT,
    "lon": LON,
    "appid": API,
    "cnt": CNT,
}

response = requests.get(url=END_POINT, params=parameters)
response.raise_for_status()
openweather_data = response.json()

index_num = 0
condition_codes = []

while index_num < CNT:
    weather_ids = openweather_data["list"][index_num]["weather"][0]["id"]
    index_num += 1
    condition_codes.append(weather_ids)
    # print("Condition Codes:", condition_codes)
    if int(weather_ids) < 700:
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body="It's going to rain today. Remember to bring an umbrella ☂️",
            from_='+18668418494',
            to='+15559998282'
        )
        print(message.status)
        index_num = CNT

# Another solution to solving the issue provided in course material#
# openweather_data = openweather_data["list"]
# will_rain = False

# for val in openweather_data:
#     condition_code = val["weather"][0]["id"]
#     if int(condition_code) < 700
#       will_rain = True
# if will_rain:
#   print("Bring an umbrella.")

# Print Test #
# print("Condition Codes:",condition_codes)
# print("Date_Time:", data["list"][0]["dt"])
# print("Weather_ID:", data["list"][1]["weather"][0]["id"])
# print(data["city"]["name"])
# print("JSON Information:")
# print(data)
