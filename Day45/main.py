from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movies_page = response.text

soup = BeautifulSoup(movies_page, "html.parser")

movie_titles = soup.find_all(name="h3", class_="title")

titles = [title.getText() for title in movie_titles]

titles.reverse()
print(titles)
