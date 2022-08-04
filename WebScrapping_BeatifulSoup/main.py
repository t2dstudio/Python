from bs4 import BeautifulSoup
import requests
response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="a", class_="titlelink")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
print(article_texts)
print(article_links)
print(article_upvote)
highest_score = max(article_upvote)
highest_score_index = article_upvote.index(highest_score)
print(highest_score_index)
print(article_texts[highest_score_index])
print(article_links[highest_score_index])
"""
#.................BEAUTIFUL SOUP..........................
#....This is a Python Lib forpulling data out of Html and XML files


with open("website.html", "r", encoding='utf-8') as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.string)
# print(soup.prettify())

#...........SELECTING PARTICULAR ELEMENTS................
#......Find_all()

all_anchor_tags = soup.find_all(name ="a")
# print(all_anchor_tags)
for tag in all_anchor_tags:
    # print(tag.getText())
    # print(tag.get("href"))
    pass

heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name='h3', class_ ="heading")
print(section_heading.getText())

#.......USING CSS SELECTORS

company_url= soup.select_one(selector="p a")
# company_url= soup.select_one(selector="#name")
# company_url= soup.select(selector=".heading")

print(company_url)
"""
