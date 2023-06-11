import requests
from bs4 import BeautifulSoup

# 4~6 request 단계
url = 'https://en.wikipedia.org/wiki/Sorting_algorithm'
response = requests.get(url)

if response.status_code == 200: #성공이면

    #parsing
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    
    title = soup.select_one('#p-lang-btn-checkbox') #id값이 p-lang-btn-checkbox 인것을 select해라
    print(title.get_text().split()[0])
else :
    print(response.status_code)