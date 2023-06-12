import requests
import datetime
import json

url = 'http://apis.data.go.kr/B552584/UlfptcaAlarmInqireSvc/getUlfptcaAlarmInfo'
params ={'serviceKey' : 'clCEJad0tTqdiSPIpwIKf1s/mOlQyCBXSVK6yt2OxzqUmgboB4KjsR2NnNuCo2vsS3LmoZQQKZD9bMP48ZZ8gg==', 'returnType' : 'xml', 'numOfRows' : '100', 'pageNo' : '1', 'year' : '2020', 'itemCode' : 'PM10' }

response = requests.get(url, params=params)
print(response)
print(response.content)
items = response.json().get('response').get('body').get('items')
#활용

today = datetime.datetime.today()
areaName = input("검색 지역 입력 : ")

data = dict()
data['districtName'] = areaName

area_data = dict()
for item in items['item']:

    # 상태
        area_code = item['issueGbn']

        if area_code == '주의보':
            area_state = '주의보'
        elif area_code == '경보':
            area_state = '경보'

        else:
            area_state = '없음'

        area_data['code'] = area_code
        area_data['state'] = area_state

data['districtName'] = area_data
print(data['districtName'])