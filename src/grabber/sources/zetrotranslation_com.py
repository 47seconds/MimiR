import requests
from bs4 import BeautifulSoup

def get_details(url):
    res = requests.get(url)
    content = res.content
    soup = BeautifulSoup(content, "html.parser")

    details = []
    
    title = soup.find('div', class_='post-title')
    if title:
            details.append(title.text.strip())
    else:
        print("Title not found")
        details.append(None)
    
    chap_list = soup.find('ul', class_='version-chap')

    if chap_list:
            chapters = chap_list.find_all('li')
            temp = chapters[0]['a'].text.split()
            chap_num = 0
            for i in temp:
                if i.isdigit():
                    chap_num = int(i)
            details.append(str(chap_num))
    else:
        print("Chapter list not found")
        details.append(None)
    
    novel_image = soup.find('div', class_='summary_image').find('img')['src']
    if novel_image:
        details.append(novel_image)
    else:
        print("Novel Cover not found")
        details.append(None)
    
    return details