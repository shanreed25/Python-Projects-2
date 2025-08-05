from other.business_days import get_last_two_business_days

#TODO: Get the dates of the last two business days not including today
last_two_business_days = get_last_two_business_days()
day_a = last_two_business_days[0]
day_b = last_two_business_days[1]
# print(f"Day 1: {day_a}")
# print(f"Day 2: {day_b}")
#*****************************************************************************************


#NEWS*************************************************************

#TODO: Get news from API
# print(three_articles)
dummy_articles = []
#
#
#
# #TODO: Get stock prices from API
# response = rq.get(STOCK_API_URL, params=parameters)
# data = response.json()
# print(data["Time Series (Daily)"])

# Last Day
# last_day = stock_data["Time Series (Daily)"][day_a.strftime("%Y-%m-%d")]

#Using a set amount because api limit has been reached
dummy_stock_data = []
last_day = "2025-08-04"
print(f"{day_a}: {last_day}")

# Day Before the last Day
# day_before_last = stock_data["Time Series (Daily)"][day_b.strftime("%Y-%m-%d")]
day_before_last = "2025-08-01"
print(f"{day_b}: {day_before_last}")








# TODO: When STOCK price increase/decreases by 5% between yesterday and the day before yesterday
#  then print("Get News")
def check_price_range(price_a, price_b):
    five_percent = 0.05 * price_b
    lower_bound = price_b - five_percent
    upper_bound = price_b + five_percent
    print(lower_bound)
    print(upper_bound)
    if price_a >= upper_bound or price_a <= lower_bound:
        print("Get News")
    else:
        print("Do Nothing")

check_price_range(99, 103)
check_price_range(float(last_day["4. close"]), float(day_before_last["4. close"]))

#TODO Fetch some news about our stock whenever we get a slightly extraordinary rise or fall


#TODO: Send SMS message
    # What was the increase or decrease
    # What is the relevant news




## STEP 1: Use https://www.alphavantage.co
# .

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
