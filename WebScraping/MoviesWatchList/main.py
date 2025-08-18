from bs4 import BeautifulSoup
import requests


URL = "https://editorial.rottentomatoes.com/guide/best-black-movies-21st-century/"

res = requests.get(URL)
page_contents = res.text
soup = BeautifulSoup(page_contents, 'html.parser')
# print(soup)
#**************************************************************************************
# TODO: From the first 30 stories, print out the titlefor all 154 movies
movie_atags_list = soup.select(selector=".article_movie_title h2 a")
# print(movie_atags_list)

movie_title_list = [movie.getText() for movie in movie_atags_list]
print(movie_title_list)

#TODO: Reverse the List: you can do this different ways
# 1. use reverse() method.
# 2. use slicing [start:stop:step]
# 3. use a for loop with the range

movie_title_list.reverse()# list reverse method

print(movie_title_list)

# with open(f"movielist.txt", mode="w") as file:
#     movie_num = 1
#     for movie in movie_title_list:
#         file.write(f"{movie_num}. {movie}\n")
#         movie_num += 1
#     # print(contents)