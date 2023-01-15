from bs4 import BeautifulSoup
import requests

#TEST YEAR
# year_to_travel = "2005-03-20"

year_to_travel = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

billboard_url = f"https://www.billboard.com/charts/hot-100/{year_to_travel}/"

response = requests.get(billboard_url)
songs_page = response.text
# print(songs_page)

soup = BeautifulSoup(songs_page, "html.parser")

# MAIN Solution
song_titles = soup.select(selector="li h3.c-title")
# print(song_titles)

#ALTERNATIVE SOLUTION:
# song_titles = soup.select("li h3[class*=c-title]")
# print(song_titles)

song_list = [song.getText() for song in song_titles]

print(song_list)

all_songs = [song.strip('\n\t') for song in song_list]
print(all_songs)
