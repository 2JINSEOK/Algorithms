"""
- absolutes = [] -> 절댓값 나열
- signs = [] -> 실제 부호를 나열
# 불리언 형식(Boolean type)은 참(True), 거짓(False) 의 두 개 값을 가지는 자료형을 말합니다.

=> 실제 정수들의 합 return
"""

"""
Rules
* absolutes의 길이와 signs의 길이는 같다
* signs[i] = True -> absolutes[i] = Positive
  signs[i] = False -> absolutes[i] = Negative
"""

from typing import List


def solution(absolutes: List[int], signs: List[bool]) -> int:
    res = []

    for ab, sign in zip(absolutes, signs):
        if sign:
            res.append(ab)
        else:
            res.append(-(ab))

    return sum(res)


absolutes = [4, 7, 12]  # 주어짐
signs = [True, False, True]  # 주어짐
# print(type(signs[0]))

# return 합을 구한다->실제 정수들을 알아야 한다
# 결국 부호가 중요->숫자와 부호를 어떻게 매치
# 1. dic 활용?
# 2. 어차피 abs, signs의 길이가 같다는 것을 활용


res = []
ans = 0

for i in range(len(absolutes)):
    if signs[i]:
        res.append(absolutes[i])
    else:
        res.append(-(absolutes[i]))

for i in range(len(res)):
    ans += res[i]

print(ans)
