from bs4 import BeautifulSoup
import requests
import smtplib
import dotenv
import os

from dotenv import load_dotenv

load_dotenv()

#
# URL = "https://appbrewery.github.io/instant_pot/"
#
#
# res = requests.get(URL)
# page_contents = res.text
# soup = BeautifulSoup(page_contents, 'html.parser')
# print(soup)
#**************************************************************************************
# TODO: From the first 30 stories, print out the titlefor all 154 movies
# item_title = soup.find(id="productTitle").getText().strip()
# price = float(soup.find(class_="a-offscreen").getText().split("$")[1])
# print(item_title)
# print(price)
#
my_email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
PORT = os.getenv("PORT")
smtp_address = os.getenv("SMTP_ADDRESS")
#
# if price <= 100:
#     mesage = f"{item_title} is now ${price}\nhttps://appbrewery.github.io/instant_pot/"
#     print("price lowered")
#     with smtplib.SMTP(smtp_address, port=PORT)as connection:
#         # TODO-2: Secure Connection
#         connection.starttls()
#
#         # TODO-3: Log into email account
#         connection.login(user=my_email, password=password)
#
#         # TODO-4: Send Email
#         connection.sendmail(from_addr=my_email,
#                     to_addrs="tralainereed@yahoo.com",
#                     msg=f"Subject:Amazon Price Alert!!!\n\n{mesage}".encode("utf-8"))

#**********************************Live Scraping of Amazon site*************************************************************
URL = "https://www.amazon.com/AmazonBasics-Puresoft-PU-Padded-Mid-Back-Computer/dp/B081H3Y5NW/ref=sr_1_1_ffob_sspa?crid=12QZ5J047HZJ2&dib=eyJ2IjoiMSJ9.lyZHkyBHCCMmXbzslnY9CZstoHa1DUmgAVUXAJTyyvABcYjDuwtllDv6Wo4bA9hC6i1HlGvg0ryTzAcRWPeFI6MJlyhqNbr1FikUWSTD7Rrubs3nina7-6VGqimlNs2ewCDIYZ_MweJELcWgYYKrJTA0okXU3ixF4RGYhRZ85ciFoqyniaLYeewacaKz6PrL31B7yS3n7kU4hzsqwVzK2bm3mpfUeVEphs36OfU_wuXfm43RCR9ijN1L4PP3Sg3eK4w3dlC-Dcy7sT03AcSK1def-GDXeYUh6VtYEslXcyc.hV0lJxZhKFZbD1CaaWNEknPR1puQFhx153WIs0KGrns&dib_tag=se&keywords=computer%2Bchair&qid=1755475509&sprefix=computer%2Bchair%2Caps%2C203&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"

header = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
"Accept-Encoding": "gzip, deflate, br, zstd",
"Accept-Language": "en-US,en;q=0.9",
"sec-fetch-site": "cross-site",
"sec-fetch-mode": "navigate",
"sec-fetch-user": "?1",
"sec-fetch-dest": "document",
"upgrade-insecure-requests": "1"
}

res = requests.get(URL, headers=header)
page_contents = res.text
soup = BeautifulSoup(page_contents, 'html.parser')
# print(soup)

item_title = soup.find(id="productTitle").getText().strip()
price = float(soup.find(class_="aok-offscreen").getText().split("$")[1])
print(item_title)
print(price)



if price <= 80:
    mesage = f"{item_title} is now ${price}\n{URL}"
    print("price lowered")
    with smtplib.SMTP(smtp_address, port=PORT)as connection:
        # TODO-2: Secure Connection
        connection.starttls()

        # TODO-3: Log into email account
        connection.login(user=my_email, password=password)

        # TODO-4: Send Email
        connection.sendmail(from_addr=my_email,
                    to_addrs="tralainereed@yahoo.com",
                    msg=f"Subject:Amazon Price Alert!!!\n\n{mesage}".encode("utf-8"))