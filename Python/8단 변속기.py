"""
- ascending : 1 2 3 4 5 6 7 8
- descending : 8 7 6 5 4 3 2 1
- mixed

=> 변속한 순서가 ascending, descending, mixed 인지 판단
"""
"""
Rules
- 1부터 8까지 숫자가 한번씩 등장
"""
"""
Q1. 만약 map함수를 사용하지 않는다면?
"""
# 1 입력한 숫자를 리스트에 저장
# 2 리스트에 저장된 숫자를 기준으로 판단
# 3 연속적이라는 것을 어떻게 판단할 것인지
# 3-1 각각의 원소를 하나씩 비교?
# 4 sort 이용?

from tabnanny import check


gear = input()
gear = gear.split()  # ['1', '2', '3', '4', '5', '6', '7', '8']
gear = [
    int(gear[i]) for i in range(len(gear))
]  # list(map(int, gear))  # [1, 2, 3, 4, 5, 6, 7, 8]
asc = [1, 2, 3, 4, 5, 6, 7, 8]
des = [8, 7, 6, 5, 4, 3, 2, 1]

if gear == asc:  # element compare 1) length 2) element
    print("ascending")
elif gear == des:
    print("descending")
else:
    print("mixed")


checker = "ascending" if gear[1] - gear[0] > 0 else "descending"
for i in range(2, len(gear)):
    if checker == "ascending" and gear[i] - gear[i - 1] > 0:
        checker = "ascending"
    elif checker == "descending" and gear[i] - gear[i - 1] < 0:
        checker = "descending"
    else:
        chekcer = "mixed"


# gear = [8, 2, 3, 4, 5, 6, 7, 1]
checker = ""
for i in range(8):
    if i == 0:
        if gear[0] == asc[0]:
            checker = "ascending"
        elif gear[0] == des[0]:
            checker = "descending"
        else:
            chekcer = "mixed"

    else:
        if chekcer == "ascending" and gear[i] == asc[i]:  # 여기서 계속 asc리스트와 비교하려면?
            chekcer = "ascending"
        elif chekcer == "descending" and gear[i] == des[i]:
            chekcer = "descending"
        else:
            chekcer = "mixed"

print(checker)
