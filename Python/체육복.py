"""
*Rules
- 바로 앞번호의 학생, 바로 뒷번호의 학생에게만 대여 가능
=> 최대한 많은 학생 return
"""

# 번호의 순서를 어떻게 알 것인가..
# return_min = n - lost, return_max = n
# 인접숫자만.. 1-2-3/2-3-4/3-4-5/
# n이 짝수일 때와 홀수일 때를 구별..?->무조건 내앞, 혹은 내뒤를 빌려주도록
# lost의 숫자를 어떻게 기억할것인가...
# checker를 이용한다?

n = 5  # 12345
lost = [2, 4]
reserve = [1, 3, 5]
cloth_chk = [0 for i in range(n)]  # 체커를 0으로 초기화, 한 줄 표현 질문, [0 0 0 0 0]
# cloth_chk = [0] * n

for i in range(n):
    cloth_chk[i] += 1  # 모든 체커에 기본 옷 부여

    if i + 1 in lost:
        cloth_chk[i] -= 1

    if i + 1 in reserve:
        cloth_chk[i] += 1

for i in range(len(cloth_chk)):
    if cloth_chk[i] == 0:
        if i > 0 and cloth_chk[i - 1] == 2:
            cloth_chk[i - 1] -= 1
            cloth_chk[i] += 1
        elif i < len(cloth_chk) and cloth_chk[i + 1] == 2:
            cloth_chk[i + 1] -= 1
            cloth_chk[i] += 1

cnt = 0
for cloth in cloth_chk:
    if cloth != 0:
        cnt += 1


print(cloth_chk, cnt)
# for i in range(len(lost)):
#    lost[i] = lost_num # 우선 lost숫자를 저장->해당 번호의 체커를 -1
#    for j in range(n): # lost_num에 해당하는 숫자를 어떻게 알아낼것인가..
#        if cloth_chk[j] == lost_num: # cloth_chk에서 lost_num에 해당하는 체커를 어떻게 지울것인가..
