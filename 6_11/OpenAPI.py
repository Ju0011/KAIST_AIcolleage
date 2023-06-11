import requests
import json
import datetime

vilage_weather_url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst?"


service_key = "MIe3DGXhgZez8IKsUCzyozfnp9dI8s5CTUpKRvta07JqEs7uLA3tA58Io9TqmV0z8uF1g9rgeWsTDiuSqJs3MA%3D%3D"

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