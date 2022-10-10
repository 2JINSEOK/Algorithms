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



def solution(N, stages):
#    number_of_failure = {}
#    number_of_challenger = {}
    probability = {}
    for i in range(1, N + 1):  # i == stage_number
        failure_cnt = 0  # count the number of failure
        challenger_cnt = 0  # count the number of challenger
        for j in range(len(stages)):  # stages[j] == jth user's location
            if stages[j] >= i: challenger_cnt += 1
            if stages[j] == i: failure_cnt += 1

#        number_of_failure[i] = failure_cnt
#        number_of_challenger[i] = challenger_cnt

        # 도전한 사람의 숫자는 어떻게 카운트 할 것인가
        if challenger_cnt == 0:
            probability_of_failure == 0
        else:
            probability_of_failure = failure_cnt / challenger_cnt
        probability[i] = probability_of_failure

    # [(key, value), (key, value), ...]
    res = dict(sorted(probability.items(), key=lambda x: [-x[1], x[0]]))  # x[1] 내림차순, x[0] 오름차순

    return list(res.keys())


N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))
