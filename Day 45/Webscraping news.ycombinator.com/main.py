from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(class_="titleline")
# print(article_tag)

article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.find(name="a").get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(class_="score")]
print(article_texts)
print(article_links)
print(article_upvotes)

max_upvotes = max(article_upvotes)
max_index = article_upvotes.index(max_upvotes)
print(max_upvotes)
print(max_index)

highest_upvoted_title = article_texts[max_index]
highest_upvoted_link = article_links[max_index]

print(highest_upvoted_title)
print(highest_upvoted_link)


#
# with open("website.html", encoding="utf8") as webpage:
#     contents = webpage.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title)
# # print(soup.title.string)
# #
# # print(soup.prettify())
#
# # print(soup.a)
#
# # all_anchor_tags = soup.find_all(name="a")
# # # print(all_anchor_tags)
# #
# # for tags in all_anchor_tags:
# #     # print(tags.getText())
# #     print(tags.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading.string)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)

