#Practical : 23- Write a python program for web scrapping with BeautifulSoup Library

import requests
from bs4 import BeautifulSoup


response = requests.get("https://news.ycombinator.com/")
content = response.content
print(content)

soup = BeautifulSoup(response.content, 'html.parser')
print(soup.title)

hyper_links = soup.find_all('a')
print(len(hyper_links))

print(soup.get_text())
print(soup.tr)
print(soup.table)

print(soup.find(id = "hnmain"))
print(soup.find(class_ = "athing"))
