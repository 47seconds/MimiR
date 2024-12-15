import requests
from bs4 import BeautifulSoup
from unidecode import unidecode

url = r"https://zetrotranslation.com/novel/a-story-about-a-girl-who-took-life-for-granted-and-fell-in-love-with-a-kind-nerdy-boy"
res = requests.get(url)
content = res.content
soup = BeautifulSoup(content, "html.parser")
soup = soup.find(attrs={'id':'wp-manga-current-chap'})
chapter_raw = soup.text
chapter_formated = chapter_raw.replace('<br>', '\n').replace('&nbsp;', '')
chapter = unidecode(chapter_raw)
with open('chapter.txt', 'w') as file:
    file.write(str(soup))