"""
Rules
* participant - completion
* 완주하지 못한 선수의 이름을 return
"""


# 효율성 실패 케이스
def in_list(li, target):
    for i, c in enumerate(li):
        if c == target:
            return i
    return -1


def solution(participant, completion):
    # ****
    # python for statment problem

    for idx, name in enumerate(participant):
        i = in_list(completion, name)
        if i != -1:  # 인덱스를 찾았으면 (index가 0이면 False)
            participant[idx] = ""
            completion[i] = ""
    return [name for name in participant if name != ""][0]


#  효율성 성공 케이스
def solution(participant, completion):
    # pre-processing
    part_dic = {name: 0 for name in participant}

    for name in participant:
        part_dic[name] += 1

    for name in completion:
        part_dic[name] -= 1

    return [k for k, v in part_dic.items() if v != 0][0]


# 1. participant와 completion을 어떻게 매치
# 1-1. 각각의 배열을 일일이 대조?
