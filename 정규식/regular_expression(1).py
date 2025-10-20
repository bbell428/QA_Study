""" 정규식 """
import re
# ca?e
# care, cafe, case, cave
# caae, cabe, cace, cade, ...

p = re.compile("ca.e")  # . : 하나의 문자를 의미
# . : 하나의 문자를 의미 > care, cafe, case (O) | caffe (X)
# ^ (^de) : 문자열의 시작 > desk, detination (O) | fade (X)
# $ (se$) : 문자열의 끝 > case, base (O) | face (X)


def print_match(m):
    if m:
        print(m.group())
    else:
        print("매칭되지 않음")


m = p.match("case")  # match: 주어진 문자열의 처음부터 일치하는지 확인
print_match(m)
