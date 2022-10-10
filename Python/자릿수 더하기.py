"""
- 자연수 N
- N의 각 자릿수의 합을 구한다
"""

# N = input()
# N = int(N)

# 자릿수 분리 작업 필요
"""
- N이 몇자리 숫자인지 알아야한다
- 각 자릿수 별로 분류?
1000, 10000, 100으로 나눈다..
그렇다면 1000, 10000, 100으로 나눌때의 기준은 어떻게..?
- 정수가 4자리수인지 3자리수인지 판단가능?
- 정수를 크기별로 분류..?
"""

# str로 변환 뒤 len으로 출력
# str_N = str(N)
# L = len(str_N) # 7->1000000
# digit = []
# # 각 자릿수 분리
# for i in range(L, 0, -1):


def solution(N):
    return sum(map(int, list(str(N))))


N = input()
N = str(N)  # list를 활용하기 위한 str 타입 변환

arr = list(N)  # ['2', '2', '3', ...] 분리
ans = []  # 빈 리스트 생성

for i in arr:
    ans.append(int(i))  # str->int 변환 후 저장
print(ans)

res = 0
for i in ans:
    res += i

print(res)
