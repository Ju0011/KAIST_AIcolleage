from bs4 import BeautifulSoup

html = """
<html>
    <body>
        <h1 id='title'>[1]크롤링이란?</h1>;
        <p class='cssstyle'>웹페이지에서 필요한 데이터를 추출하는 것</p>
        <p id='body' align='center'>파이썬을 중심으로 다양한 웹크롤링 기술 발달</p>
    </body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

# 가장 먼저 검색되는 태그를 반환
paragraph_data = soup.find('p')

print(paragraph_data)
print(paragraph_data.string)
print(paragraph_data.get_text())