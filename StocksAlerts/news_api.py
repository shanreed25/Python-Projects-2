import requests as rq
from stock_api import up_down, diff_percentage
NEWS_API_KEY = ""
NEWS_API_URL = "https://newsapi.org/v2/everything"
COMPANY_NAME = "Dollar Tree Inc"
STOCK = "DLTR"

news_parameters = {
    "q": COMPANY_NAME,
    "apiKey": NEWS_API_KEY,
}

#TODO: Get news from API
response = rq.get(NEWS_API_URL, params=news_parameters)
data = response.json()
articles = data["articles"]
#TODO: Create a list that contains the first 3 articles
    # using slice operator to get the first 3 articles
three_articles = articles[:3]
# print(three_articles)

#TODO: Create a new list of the first 3 articles's headline and description
    # using list comprehensions
# three_articles is a list of dictionaries
#******************************************************************
# articles_list = [{"title":item['title'], "description":item['description']} for item in three_articles]
# for article in articles_list:
#     print(f"Headline: {article["title"]}.\nBrief: {article["description"]}")
#*********************OR********************************
# formatted_articles_list = [f"Headline: {article['title']}.\nBrief: {article['description']}" for article in three_articles]
# print(articles_list)

#**********************With abs() removed from stock_api.py and added to main.py
formatted_articles_list = [f"{STOCK}: {up_down}{diff_percentage}%\nHeadline: {article['title']}.\nBrief: {article['description']}" for article in three_articles]