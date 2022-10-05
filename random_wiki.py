import requests
from bs4 import BeautifulSoup

url = requests.get("https://en.wikipedia.org/wiki/Special:Random")
soup = BeautifulSoup(url.content, 'html.parser')
title = soup.find(class_ = "firstHeading").text
title = title.split(" ")
link = ""
for word in title:
    link = link + word + '_'
print(link[:-1])
site = f"https://en.wikipedia.org/wiki/%s" % link
print(site[:-1])
