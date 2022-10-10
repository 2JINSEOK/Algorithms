# 1. "제거
# 2. 숫자, 알파벳을 어떻게 구분
# 3. 결국엔 아스키코드?
# 3-1. input값의 아스키코드값이 97-122 / 48-57 로 구분
# 4. 알파벳을 마주했을 때 어떻게 처리할 것인가..
# 4-1. 알파벳이 연속될 경우 어떻게 끊을 것인가..
# 5. 변환된 s를 연속적으로 저장해야 한다
def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    d = {w: n for w, n in zip(words, nums)}

    res = ''
    tmp = ''
    for i in s:
        tmp += i
        if tmp in words: res += d[tmp]; tmp = ''
        elif tmp in nums: res += tmp; tmp = ''
    return int(res)


s = input()
li_s = list(s)  # 리스트 변환 -> 각각의 글자를 분리하기 위해
# print(li_s)
# print(ord("o"))
#print(ord(li_s[1]))
for i in range(len(li_s)):
    if ord(li_s[i]) == 34: continue # "
    elif ord(li_s[i]) >= 97 and ord(li_s[i]) <= 122:
        
        # alphabet
    else:
            
