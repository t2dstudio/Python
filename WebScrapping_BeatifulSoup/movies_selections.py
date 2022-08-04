import requests
from bs4 import BeautifulSoup

response = requests.get('https://web.archive.org/web/20200518055830/https://www.empireonline.com/movies/features/best-movies-2/')
empire_online_html = response.text
soup = BeautifulSoup(empire_online_html, "html.parser")
# print(soup)
all_movies = soup.find_all(name="h3", class_="title")
movie_title = [movie.getText() for movie in all_movies]
#print(movie_title[::-1])
# for n in range(len(movie_title)-1,-1,-1):
#     print(movie_title[n])

movies = movie_title[::-1]

with open("movie.txt", "w") as file:
    for movie in movies:
        file.write(f"{movie}\n")