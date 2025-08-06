import requests as rq
import datetime as dt
# https://pixe.la/ ---> How to use
# https://docs.pixe.la/


pixela_endpoint = "https://pixe.la/v1/users"
MY_TOKEN = " "
USERNAME = " "
user_params = {
    "token": MY_TOKEN, #password
    "username": USERNAME, #username
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

#TODO-1: Set up new account with pixela
# res = rq.post(url=pixela_endpoint, json=user_params)
# print(res.text)# give you the response as a piece of text


GRAPH_ID = "graph1"
graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "hour",
    "type": "float",
    "color": "ajisai"

}

headers = {
    "X-USER-TOKEN": MY_TOKEN
}

#TODO-2: Create a new graph on pixela for your account
create_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# res = rq.post(create_graph_endpoint, json=graph_config, headers=headers)
# print(res.text)



#TODO-3: Get the graph!
# Go to graph in browser with more info: https://pixe.la/v1/users/yourusername/graphs/youridfromgraphconfig.html
# Go to graph in browser with less info: https://pixe.la/v1/users/yourusername/graphs/youridfromgraphconfig




coding_date = dt.date(year=2025, month=8, day=2)#for passed date
# coding_date = dt.datetime.now()# for current date
formatted_coding_date = coding_date.strftime("%Y%m%d")

my_body = {
    "date": formatted_coding_date,
    "quantity": input("How many hours did you spend coding?")
}
#TODO-4: Post value to the graph
post_value_to_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
res = rq.post(post_value_to_graph_endpoint,  json=my_body, headers=headers)
print(res.text)

#TODO-5: Update Pixel
# update_value_to_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{formatted_coding_date}"
# res = rq.put(update_value_to_graph_endpoint, json={"quantity": "9.0"}, headers=headers)
# print(res.text)


#TODO-6: Delete Pixel
# delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{formatted_coding_date}"
# res = rq.delete(delete_pixel_endpoint, headers=headers)
# print(res.text)