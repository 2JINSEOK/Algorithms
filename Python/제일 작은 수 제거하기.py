"""
* arr에서 가장 작은 수를 제거한 배열을 return
* return 값이 빈 배열인 경우엔 -1을 채워서 return
"""
from typing import List


def solution(arr: List[int]) -> List[int]:
    if len(arr) == 1:
        return [-1]

    min_value = arr[0]
    min_idx = 0
    for i in range(1, len(arr)):
        if arr[i] < min_value:
            min_value = arr[i]
            min_idx = i

    arr.pop(min_idx)
    return arr


def solution(arr):
    min_value = arr[0]
    res = []
    for i in range(1, len(arr)):
        if arr[i] < min_value:
            res.append(min_value)  # 기존 min_value 추가
            min_value = arr[i]
            print(res, "if")

        else:
            res.append(arr[i])
            print(res, "else")

    if len(res) == 0:
        res = [-1]

    return res


arr = [4, 3, 2, 1]
# arr = [10]
print(solution(arr))
