import requests
from bs4 import BeautifulSoup

url = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%84%9C%EC%B4%88AI&oquery=%EC%84%9C%EC%B4%88+%EB%A8%80&tqi=ic8RWdp0YidssKroiJKsssssthN-042430'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    print(soup)
else :
    print(response.status_code)