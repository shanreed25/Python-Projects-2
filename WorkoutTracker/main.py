import requests as rq
import datetime as dt

#TODO-1: Create Constants to store the APP_ID, API_KEY, HOST_DOMAIN and NLE_ENDPOINT
APP_ID = " "
API_KEY = " "
HOST_DOMAIN = "https://trackapi.nutritionix.com"
NLE_ENDPOINT = "/v2/natural/exercise"
#*********************************************************************
#TODO-2: Get Exercise Stats with Natural Language Queries
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

body = {
    "query": input("Tell me what exercises you did: ")
}

res = rq.post(url=f"{HOST_DOMAIN}{NLE_ENDPOINT}", headers=headers, json=body)
exercise_list = res.json()["exercises"]
print(exercise_list)
#*********************************************************************

#TODO-3: Generate a new row of data in your Google Sheet for each of the exercises that you get back from the Nutritionix API
SHEETY_BASE_URL = "https://api.sheety.co/"
SHEETY_USER_ID = " "
sheety_project_name = "workoutTracking"
sheet_name = "workouts"
BEARER_TOKEN = " "
sheety_headers = {
    "Authorization": f"Bearer {BEARER_TOKEN}",
}
sheety_body = {}
workout = {}
for item in exercise_list:
    exercise = item['user_input'].title()
    duration = item['duration_min']
    calories = item['nf_calories']

    cur_datetime = dt.datetime.now()
    cur_date = cur_datetime.strftime("%m/%d/%Y")
    cur_time = cur_datetime.strftime("%H:%M")

    workout["date"] = cur_date
    workout["time"] = cur_time
    workout["exercise"] = exercise
    workout["duration"] = duration
    workout["calories"] = calories
    sheety_body["workout"] = workout

    res = rq.post(url=f"{SHEETY_BASE_URL}{SHEETY_USER_ID}/{sheety_project_name}/{sheet_name}", json=sheety_body, headers=sheety_headers)
    print(res.json())

