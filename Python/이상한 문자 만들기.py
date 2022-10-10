"""
*Rules

- 각 단어는 하나 이상의 공백문자로 구분
- 각 단어의 짝수번째->대문자, 홀수번째->소문자
- 단어별로 짝/홀수 인덱스 판단
- 첫 번째 글자는 0번째 인덱스
"""

# 띄어쓰기->각 단어별 분리
# 단어를 분리할 방법은?->인덱스가 초기화 되어야하므로 분리가 필요->분리가 아니라 다시 인덱스를 0으로?
# 입력 받은걸 어떻게 저장..


def solution(s):
    ans = []
    j = 0
    for i in range(len(s)):
        if s[i] == " ":  # 공백을 만나게 된다면...?->인덱스를 0으로 인식하도록..
            ans.append(s[i])
            j = 0
            # 미완성 부분..
        else:
            if j % 2 == 0:  # 인덱스->짝수->대문자
                if ord(s[i]) >= 65 and ord(s[i]) <= 90:
                    ans.append(s[i])
                else:
                    ans.append(chr(ord(s[i]) - 32))  # 대문자로 변환

            else:  # 인덱스->홀수->소문자
                if ord(s[i]) >= 97 and ord(s[i]) <= 127:
                    ans.append(s[i])
                else:
                    ans.append(chr(ord(s[i]) + 32))  # 소문자로 변환
            j += 1

    print(ans)
    sol = ""
    for i in range(len(ans)):
        sol += ans[i]  # sol = sol + ans[i] // sol = ans[i] + sol

    print(sol)
    return sol


s = "try hello world"
print(solution(s))


####################################################################
####################################################################
######### clean code version
def solution2(s):
    ans = []
    j = 0
    for i in range(len(s)):
        revised_str = s[i]
        if s[i] == " ":  # 공백을 만나게 된다면...?->인덱스를 0으로 인식하도록..
            j = 0
            # 미완성 부분..
        else:
            if j % 2 == 0:  # 인덱스->짝수->대문자
                if s[i].islower():
                    revised_str = chr(ord(s[i]) - 32)  # 대문자로 변환

            else:  # 인덱스->홀수->소문자
                if s[i].isupper():
                    revised_str = chr(ord(s[i]) + 32)  # 소문자로 변환
            j += 1
        ans.append(revised_str)

    # str -> list: split()
    # list -> str: join()
    return "".join(ans)


s = "try hello world"
print(solution2(s))


####################################################################
######### code version (using split())
def solution3(s):
    if s == " ":
        return s

    answer = ""
    words = s.split()
    print(words)
    for word in words:
        for i, val in enumerate(word):
            if i % 2 == 0:
                answer += val.upper()
            else:
                answer += val.lower()
        answer += " "

    return answer[:-1]


s = "try hello world"
s = " "  # " " -> ""
print(solution3(s), "aaa")
