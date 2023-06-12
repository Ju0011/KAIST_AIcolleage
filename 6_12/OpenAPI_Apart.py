
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

date = 202201  #3
gu_code = 11305  #4
service_key = 'clCEJad0tTqdiSPIpwIKf1s%2FmOlQyCBXSVK6yt2OxzqUmgboB4KjsR2NnNuCo2vsS3LmoZQQKZD9bMP48ZZ8gg%3D%3D' #5

url = f'http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/'\
    f'getRTMSDataSvcAptRent?LAWD_CD={gu_code}&DEAL_YMD={date}&'\
    f'serviceKey={service_key}'  #6

result = urlopen(url)  #7
house = BeautifulSoup(result, 'lxml-xml')  #8
te = house.find_all('item')

datas = []  # 1

for i in range(len(te)):  # 2
    deposit = te[i].보증금액.string.strip()
    rent_fee = te[i].월세금액.string.strip()
    built_yr = te[i].건축년도.string.strip()
    dong_name = te[i].법정동.string.strip()
    apt_name = te[i].아파트.string.strip()
    size = te[i].전용면적.string.strip()
    gu_code = te[i].지역코드.string.strip()

    data = [deposit, rent_fee, built_yr, dong_name, apt_name, size, gu_code]  # 3
    datas.append(data)  # 4

df = pd.DataFrame(datas, columns=['deposit', 'rent_fee', 'built_yr', 'dong_name', 'apt_name',
                                  'size', 'gu_code'])