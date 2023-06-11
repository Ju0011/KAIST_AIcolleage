## "https://music.bugs.co.kr/chart?wl_ref=M_left_02_01" : 다음 링크에서 음악 차트를 출력해보자
from urllib.request import urlopen
from bs4 import BeautifulSoup
url = urlopen('https://music.bugs.co.kr/chart')
soup = BeautifulSoup(url.read(), 'html.parser')

# td 태그에 check라는 class가 있는 td 태그를 모두 가져온다.
param = {
    'class' : 'check'
}
musics = soup.find_all('td', param)

# musics의 각 태그들에 대해서
for i, music in enumerate(musics):
    # input 태그안에 title 속성값을 parsing한다.
    detail = music.input
    title = detail.get('title')
    print(i+1, title)