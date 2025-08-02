import requests
from datetime import datetime
import smtplib
import time
MY_LAT = 36.169941 # Your latitude
MY_LONG = -115.139832 # Your longitude

#TODO: Check to see if the ISS is close to my current position

def is_over_head():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_data = iss_response.json()
    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])
    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude <= 5 + MY_LAT and MY_LONG - 5 <= iss_longitude<= 5 + MY_LONG:
            return True

#TODO: Check to see if it is dark
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    hour_now = datetime.now().hour

    if hour_now >= sunset or hour_now <= sunrise:
        return True


#TODO: send me an email to tell me to look up.
while True:
    time.sleep(60)# BONUS: run the code every 60 seconds.
    if is_over_head() and is_night():
        my_email = "youremail@email.com"
        password = "yourapppassword"
        PORT = 123456
        with smtplib.SMTP("smtpaddress.com", port=PORT)as connection:
            # TODO-2: Secure Connection
            connection.starttls()

            # TODO-3: Log into email account
            connection.login(user=my_email, password=password)

            # TODO-4: Send Email
            connection.sendmail(from_addr=my_email,
                            to_addrs="sendtoemail@email.com",
                            msg="Subject:LOOK UP!!!!\n\nThe ISS is above you in the sky")
