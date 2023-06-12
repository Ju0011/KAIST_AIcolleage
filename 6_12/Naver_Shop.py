import requests
from bs4 import BeautifulSoup
import urllib

#a = requests.get(url)

category = "50000151"
keyword = "천일염"
url = "https://search.shopping.naver.com/search/all?frm=NVPGLET&query=" + keyword

bs = BeautifulSoup(requests.get(url).content, "html.parser")
product_list = bs.select('div[class=product_item__MDtDF]')

# for li in product_list:
#     for goods in li.contents:
#         title = price = registerdate = 0

#         title = goods.select("a[adProduct_link__NYTV9 linkAnchor']")[0].title
#         print(title)
#         # price = goods.select("span[class^='price_num__']")[0].text
#         # registerdate = goods.select("div[class^='basicList_etc_box__'] > span")[0].text

#         # print(title, price, registerdate)