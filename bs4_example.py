import requests
from bs4 import BeautifulSoup

url = "https://iridescent-zeal.tistory.com/151"
res = requests.get(url)
res.raise_for_status()

# soup = BeautifulSoup(res.text, "lxml")
soup = BeautifulSoup(res.text, "html.parser")

# print(soup.title) # 제목을 가져옴
# print(soup.title.get_text()) # 텍스트만 가져옴

# print(soup.a) # 문서에서 첫 번째 <a> 태그를 가져옴(soup 객체)
# print(soup.a.attrs) # a태그 element의 속성을 딕셔너리로 출력
# print(soup.a["class"]) # a태그 element의 class 속성 값 정보를 출력

# print(soup.find("a", attrs={"class":"VelogTab_item__ijN3R VelogTab_active__P7YGA"}))
print(soup.find(attrs={"class":"ico_skin ico_cate"}))