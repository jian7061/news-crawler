from unittest import result
from urllib import response
import requests
from bs4 import BeautifulSoup

result = requests.get("https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=100")
html = response.text
soup = BeautifulSoup(html, 'html.parser')
titles = soup.select('.cluster_text')

print(titles)

for title in titles : 
    print(title.text.strip())