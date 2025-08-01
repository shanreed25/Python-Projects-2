import datetime as dt
import pandas as pd
import random
import smtplib

# TODO-1: Check if today matches a birthday in the birthdays.csv

# TODO: Get current month and day
current_datetime = dt.datetime.now()
current_date = current_datetime.date()# .strftime("%Y-%#m-%#d") changes the date from 2025-07-31 to 2025-7-31
current_month = current_datetime.month
current_day = current_datetime.day
today = (current_month, current_day)

#TODO Read CSV file and convert data into a list of dictionaries
df = pd.read_csv("birthdays.csv")
dict_list = df.to_dict(orient="records")

birthday_people = []
for person in dict_list:
    person_month = person["month"]
    person_day = person["day"]
    birthday = (person_month, person_day)

    # TODO: if current month and date matches a month and day in the list
    if today == birthday:
        # TODO: Add person to birthday list
        birthday_people.append(person)
print(birthday_people)

#TODO-2 Pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

#TODO Pick a random letter from letter templates
file_num = random.randint(1, 3)
with open(f"letter_templates/letter_{file_num}.txt") as letter:
    letter = letter.read()
    print()

my_email = "myemail@email.com"
other_email = ""
password = "password"
PORT = 587
#TODO Replace the [NAME] with the person's actual name from birthdays.csv
for person in birthday_people:
    birthday_card = letter.replace("[NAME]", person["name"])
    # print(birthday_card)

#TODO-3  Send the letter generated in step 3 to that person's email address.

    birthday_person_email = person["email"]
    print(birthday_person_email)
    with smtplib.SMTP("smtp.gmail.com", port=PORT) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_person_email,
                            msg=f"Subject:HAPPY BIRTHDAY!!!!!\n\n {birthday_card} ")

