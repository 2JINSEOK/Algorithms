'''
1. n 입력받기

2. 뒤집기
- 빈 리스트를 만든다
- 리스트에 거꾸로 입력한다
- 그렇다면 글자를 하나씩 어떻게 분리할 것인가
- n의 자리수를 알아내려면?->10,100,1000,10000,... => 1. 로그 12345/10
'''
n = input()
n = int(n) # str -> int 변환

# n이 몇 자리수인지 알아내기 위한 부분
cnt = 0
num = n
while True:
    if (num // 10) >= 1:
        cnt += 1
        num = (num // 10)
    elif (num // 10) >= 0: # 몫이 0.xx가 되는 순간 탈출
        cnt += 1
        break

# 큰수부터 거꾸로 나눈다->몫만큼 원래값에서 빼준다
print(cnt)

digit_li = []
for i in range(cnt, 0, -1):
    print(cnt)
    share = n // 10**(i-1)
    digit_li.append(share)
    n = n - ((10**(i-1))*share)
    print(n)


digit_li.reverse()
print(digit_li)    
            
