import requests

url = "https://velog.io/@bbell/posts"

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"}

res = requests.get(url, headers=headers)
res.raise_for_status()
print("웹 스크래핑 성공")

# with open("mygoogle.html", "w", encoding="utf-8") as f:
#     f.write(res.text)
