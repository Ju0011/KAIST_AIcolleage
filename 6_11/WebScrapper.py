from urllib.request import urlopen
import soupsieve
from bs4 import BeautifulSoup
import requests


html = urlopen("https://ko.wikipedia.org/wiki/%EA%B0%95%EC%95%84%EC%A7%80")
bsObject = BeautifulSoup(html, "html.parser")

# 내용 출력하기
for link in bsObject.find_all('p'):
    #print(link.text.strip(), link.get('src'))
    print(link.text)

# 이미지 저장하기


'''
#강사님 답
html = urlopen("https://en.wikipedia.org/wiki/Sociality#Presociality")
bsObject = BeautifulSoup(html, "html.parser")

bs = BeautifulSoup(html, "html.parser")
body = bs.find('div',{'id':'bodyContent'})

for p in body.find_all('p'):
    print(p.text)
'''

#추가 구현
'''
# Wikipedia 본문 스크래퍼
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("https://en.wikipedia.org/wiki/Sociality")
bs = BeautifulSoup(html, "html.parser")

body = bs.find('div',{'id':'bodyContent'}) #

for p in body.find_all('p'):
    print(p.text)

for h in body.find_all('span',{'class':'mw-headline'}):
    print(h.text)


for element in body.find_all(['p','span','h3',;]):
    if element.get('class') == 'mw-headline':
        print()
    elif element.get('p') is None:
        print()

'''