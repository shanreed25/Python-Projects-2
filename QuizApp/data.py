import requests as rq



AMOUNT = 10
TYPE = 'boolean'

parameters = {
"amount": AMOUNT,
"type": TYPE,
}

#API: https://opentdb.com/api.php?amount=10&type=boolean

# Format parameters in URL String
# You can paste this URL in a browser with a json formatter and see a nicer version of the data
# response = rq.get(url="https://api.sunrise-sunset.org/json?lat=36.169941&lng=-115.139832")
#OR use params option*******************************************
response = rq.get(url="https://opentdb.com/api.php", params=parameters,)
response.raise_for_status()
data = response.json()
question_data = data["results"]


# print(question_data)


