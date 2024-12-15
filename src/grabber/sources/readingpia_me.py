import requests
from bs4 import BeautifulSoup

def get_details(url):
    res = requests.get(url)
    content = res.content
    soup = BeautifulSoup(content, "html.parser")
    
    details = []
    
    title = soup.find('h1', class_='title')
    if title:
            details.append(title.text.strip())
    else:
        print("Title not found")
    
    chap_list = soup.find('div', class_='seriesLeftSidebarDiv')
    if chap_list:
            chapters = chap_list.find_all('a')
            temp = chapters[-1].text.split()
            chap_num = 0
            for i in temp:
                if i.isdigit():
                    chap_num = int(i)
            details.append(str(chap_num))
    else:
        print("Chapter list not found")
    
    novel_image = soup.find('img', class_='novel-cover')['src']
    if novel_image:
        details.append("https://www.readingpia.me/" + novel_image)
    else:
        print("Novel Cover not found")
    
    return details