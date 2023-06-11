import requests
from bs4 import BeautifulSoup
import pandas as pd

## API Key 설정
API_Key = ""
URL = "http://openapi.tago.go.kr/openapi/service/ExpBusInfoService/getCtyCodeList?serviceKey={API}".format(API= API_KEY)

# API로 데이터 불러오기
rq = requests.get(URL)
soup = BeautifulSoup(rq.text, "html.parser")

cityList = []
for item in soup.find_all("item"):
    cityCode = item.find("citycode").text
    cityName = item.find("cityname").text
    cityList.append([cityCode, cityName])

city_df = pd.DataFrame(cityList, columns= ["cityCode", "cityName"])
city_df.head()