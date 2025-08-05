import requests as rq
#
# #TODO: Get Stock price data
# STOCK_API_KEY = ""
# STOCK = "DLTR"
# COMPANY_NAME = "Dollar Tree Inc"
# STOCK_DATA_API = "TIME_SERIES_DAILY"
# STOCK_API_URL = "https://www.alphavantage.co/query"
# parameters = {
#     "function": STOCK_DATA_API,
#     "symbol": STOCK,
#     "apikey": STOCK_API_KEY
# }
#
# response = rq.get(STOCK_API_URL, params=parameters)
# stock_data = response.json()["Time Series (Daily)"]
# stock_data_list = [value for (key,value) in stock_data.items()]# a list of the values for each key
#
# #TODO: Get yesterday's closing price
# yesterday_data = stock_data_list[0]#get hold of yesterday's data by getting the object at index 0
# yesterday_closing_price = yesterday_data["4. close"]
# # print(yesterday_closing_price)
#
# #TODO: Get the day before yesterday's closing price
# day_before_yesterday_data = stock_data_list[1]#get hold of day before yesterday's data by getting the object at index 1
# day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
# # print(day_before_yesterday_closing_price)


# Dummy Prices to check if code works
dummy_yesterday_closing_price = "1568.360"
dummy_day_before_yesterday_closing_price = "1643.0000"



#**************************************************************************************
# #TODO: Get the positive difference between the closing prices
# # difference can be a negative number so
# # we can use the abs() function: returns the absolute value of a number
# difference = abs(float(dummy_yesterday_closing_price) - float(dummy_day_before_yesterday_closing_price))
#
#
# #TODO: Work out the percentage difference in the closing prices
# # difference / yesterday_closing_price returns a decimal and to turn it into a percentage
# # we need to multiply it by 100
# diff_percentage = (difference / float(dummy_yesterday_closing_price)) * 100
# print(f"STOCK PRICE DIFFERENCE: {diff_percentage}")


#*********************************OR
#TODO:Alternate to above, instead of using abs: add emoji to show if stock is up or down and a rounded percentage
# instead of using abs, but abs() will have to be put back
difference = float(dummy_yesterday_closing_price) - float(dummy_day_before_yesterday_closing_price)
up_down = None
if difference > 0:#if difference is positive
    up_down = "🔺"
else:#if difference is negative
    up_down = "🔻"

diff_percentage = round((difference / float(dummy_yesterday_closing_price)) * 100)
# print(f"STOCK PRICE DIFFERENCE: {diff_percentage}")








#MY CODE********************************************************
# response = rq.get(STOCK_API_URL, params=parameters)
# stock_data = response.json()
# # print(data["Time Series (Daily)"])