from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/"
                        "best-movies-2/")
response.encoding = "utf-8"
empire_web_page = response.text

soup = BeautifulSoup(empire_web_page, "html.parser")
titles = soup.find_all(name="h3", class_="title")
# print(titles)

title_list = []

for title in titles:
    title_text = title.getText()
    title_list.append(title_text)

title_list.reverse()
print(title_list)

with open("movies.txt", "w") as file:
    for movie in title_list:
        file.write(f"{movie}\n")
