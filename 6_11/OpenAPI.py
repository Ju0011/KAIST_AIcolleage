import requests
import json
import datetime

vilage_weather_url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst?"

#일반 인증키(encoding)
service_key = "clCEJad0tTqdiSPIpwIKf1s%2FmOlQyCBXSVK6yt2OxzqUmgboB4KjsR2NnNuCo2vsS3LmoZQQKZD9bMP48ZZ8gg%3D%3D"

today = datetime.datetime.today()
base_date = today.strftime("%Y%m%d") # "20200214" == 기준 날짜
base_time = "0800" # 날씨 값

nx = "60"
ny = "128"

payload = "serviceKey=" + service_key + "&" +\
    "dataType=json" + "&" +\
    "base_date=" + base_date + "&" +\
    "base_time=" + base_time + "&" +\
    "nx=" + nx + "&" +\
    "ny=" + ny

# 값 요청
res = requests.get(vilage_weather_url + payload)

items = res.json().get('response').get('body').get('items')

#print(res) #200

print(res.json().get('response').get('body').get('items'))
#type(res.json().get('response').get('body').get('items')) #타입은 딕셔너리

data = dict()
data['date'] = base_date

weather_data = dict()
for item in items['item']:
    # 기온
    if item['category'] == 'TMP':
        weather_data['tmp'] = item['fcstValue']

    # 기상상태
    if item['category'] == 'PTY':

        weather_code = item['fcstValue']

        if weather_code == '1':
            weather_state = '비'
        elif weather_code == '2':
            weather_state = '비/눈'
        elif weather_code == '3':
            weather_state = '눈'
        elif weather_code == '4':
            weather_state = '소나기'
        else:
            weather_state = '없음'

        weather_data['code'] = weather_code
        weather_data['state'] = weather_state

data['weather'] = weather_data
print(data['weather'])

'''
#공식문서 샘플 코드 - #일반 인증키(decoding)
import requests
from bs4 import BeautifulSoup

url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'
params ={'serviceKey' : 'clCEJad0tTqdiSPIpwIKf1s/mOlQyCBXSVK6yt2OxzqUmgboB4KjsR2NnNuCo2vsS3LmoZQQKZD9bMP48ZZ8gg==', 'pageNo' : '1', 'numOfRows' : '1000', 'dataType' : 'XML', 'base_date' : '20230611', 'base_time' : '0600', 'nx' : '55', 'ny' : '127' }

response = requests.get(url, params=params)

bsObject = BeautifulSoup(response.content, "html.parser")
'''