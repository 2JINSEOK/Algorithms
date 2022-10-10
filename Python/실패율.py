'''
* 실패율
- 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수

=> 실패율이 높은 스테이지부터 내림차순으로 배열 return
======================================================================================================
** 실패율이 같은 스테이지->작은 번호의 스테이지가 먼저 오도록
** 스테이지 도달한 유저가 없는 경우-> 실패율=0
'''

'''
1. 실패율 계산 작업이 필요 -> 실패율 저장

'''

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

number_of_failure = []
number_of_challenger = []
for i in range(N): # i == stage_number
    cnt1 = 0 # count the number of failure
    cnt2 = 0 # count the number of challenger
    for j in range(len(stages)):
        if i == N - 1: # i == final_stage
            if stages[j] == N + 1: continue
        else:
            if stages[j] == i + 1: cnt1 += 1
    number_of_failure.append(cnt1)

# 도전한 사람의 숫자는 어떻게 카운트 할 것인가
for i in range(len(number_of_failure)): # calculate probability of failure
    probability_of_failure = 0
    if number_of_failure[i] != 0:
        probability_of_failure = (number_of_failure[i]) / number_of_challenger[i]



