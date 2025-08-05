import requests as rq
from twilio.rest import Client
from stock_api import diff_percentage
from news_api import formatted_articles_list

#stock_api.py************************************************************************
#TODO: Get Stock price data
#TODO: Get yesterday's closing price
#TODO: Get the day before yesterday's closing price
#TODO: Get the positive difference between the closing prices
#TODO: Work out the percentage difference in the closing prices
#*************************************************************************************
#TODO: If diff_percentage is greater than 5 then get three news articles from the news api

# REAL CODE*******************************************************
# if diff_percentage > 5:
#     print("Get News")
#*****************************************************************
#TESTING CODE: changed to 4 to test code with current numbers
#abs has to be put here if removed from stock_api.py
# if diff_percentage > 4:
if abs(diff_percentage) > 4:
#news_api.py*********************************************************************************
#TODO: Get news from API
#TODO: Create a list that contains the first 3 articles
#TODO: Create a new list of the first 3 articles's headline and description
#*************************************************************************************
    account_sid = ""
    auth_token = ""
    client = Client(account_sid, auth_token)

    for article in formatted_articles_list:
        print(article)
        # message = client.messages.create(
        #     from_="whatsapp:+14155238886",
        #     body=article,
        #     to="whatsapp:+1234567898"
        # )
        # print(message.status)
    # print(f"Articles: {three_articles}")
