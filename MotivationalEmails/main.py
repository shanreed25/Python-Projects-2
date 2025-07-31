import smtplib
import datetime as dt
import random

my_email = ""
other_email = ""
password = ""
PORT = 587
# Send Motivation Quote via email
#TODO Open quotes.txt file and get the list of quotes
with open("quotes.txt", mode='r' ) as data:
    quotes_list = [quote.strip() for quote in data.readlines()]
    print(quotes_list)


#TODO Pick out a random quote from the list of quotes
quote = random.choice(quotes_list)
print(quote)


#TODO: Get current day of the week
current_datetime = dt.datetime.now()
week_day = current_datetime.weekday()
print(week_day)

if week_day == 3:
     #TODO: Use SMTP to send email
    with smtplib.SMTP("smtp.gmail.com", port=PORT) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=other_email,
                            msg=f"Subject:Motivational\n\n {quote} ")
