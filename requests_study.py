import requests
res = requests.get("http://google.com")
# res = requests.get("http://testbbell.tistory.com") # 접근 권한 없음 404
res.raise_for_status() # 문제가 생겼을 경우 오류를 내뱉고 프로그램 종료
print("웹 스크래핑을 진행합니다.")

# print("응답코드 :", res.status_code) # 200 이면 정상
# if res.status_code == requests.codes.ok:
#     print("정상입니다")
# else:
#     print("문제 발생. [에러코드 ", res.status_code, "]")

print(len(res.text))
print(res.text)

with open("mygoogle.html", "w", encoding="utf-8") as f:
    f.write(res.text)