# 모든 링크의 텍스트 & 주소 가져오기
# tag :a & href를 찾아보자

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://news.daum.net/digital#2")
bsObject = BeautifulSoup(html, "html.parser")

atags = bsObject.find_all('a')

for a in atags:
    href = a.get('href')
    if 'https://v.daum.net/v/20230608' in href:
        print(a.text.strip())
        print(a.get('href'))