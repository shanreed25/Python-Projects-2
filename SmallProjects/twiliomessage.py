import requests as rq
from twilio.rest import Client


account_sid = ""
auth_token = ""
client = Client(account_sid, auth_token)



# print(message.status)





OWM_API_KEY = ""
LAT = 36.169941
LON= -115.139832
API_URL = "https://api.openweathermap.org/data/2.5/forecast"
parameters = {
"lat": LAT,
"lon": LON,
"appid": OWM_API_KEY,
"cnt": 4
}

# api.openweathermap.org/data/2.5/forecast?lat=36.169941&lon=-115.139832&appid=12eaac17ed6b664396f293dfdb752f98
# dt: TIME STAMP: THE AMOUNT OF TIME THAT HAS PASSES SINCE 1/1/1970IN uNIX TIME: SECONDS
# "dt_txt" IS THE HUMAN READABLE
response = rq.get(url=API_URL, params=parameters,)
response.raise_for_status()

data = response.json()
status_code = data["cod"]
print(data)
print(status_code)

print(data["list"])


is_clear = False
for day in data["list"]:
    weather_id = day["weather"][0]["id"]
    if int(weather_id) <= 800:
        is_clear = True
if is_clear:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_="whatsapp:+14155238886",
        body="Its sunny today,🌞",
        to="whatsapp:+1234567897"
    )
    print(message.status)
