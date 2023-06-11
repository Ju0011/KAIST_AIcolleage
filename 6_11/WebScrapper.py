from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://ko.wikipedia.org/wiki/%EA%B0%95%EC%95%84%EC%A7%80")
bsObject = BeautifulSoup(html, "html.parser")

#for link in bsObject.find_all('a'):
#    print(link.text.strip(), link.get('href'))

for link in bsObject.find_all('p'):
    print(link.text.strip(), link.get('src'))