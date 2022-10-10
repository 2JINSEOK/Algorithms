"""
- N * M 좌석
- 안전도 : 다른 사람까지의 거리 중 가장 가까운 거리
- 사람들은 상하좌우에 붙어 앉을 수 X
- 경계 밖은 고려 X
- 안전도가 가장 높은 좌석을 배정
- 현재 모든 좌석이 비어있다면 (1, 1) 배정
"""
# input : N M Q
# 1 N * M 좌석표는 어떻게 만들것인지 -> 행이 N개, 열이 M개 [[], [], [], ...]

import sys
from webbrowser import get

N, M, Q = input().split()  # QnA, 원래 split을 하게되면 list로 return이 아닌지
N = int(N)
M = int(M)
Q = int(Q)


work_li = []
for i in range(Q):
    In, ID = input().split()
    ID = int(ID)
    work_li.append([In, ID])  # QnA, 쌍을 지어 리스트로 append하는게 맞는 코드인지

seat_li = [[0] * M] * N
# 0 * M = 0
# [0] * M = [0, 0, 0, 0, 0 ... 0]


def print_2d_array(arr2d):
    for i in range(len(arr2d)):
        for j in range(len(arr2d[0])):
            print(arr2d[i][j], end=" ")
        print()


def get_index_of_possible_location(seat_li, current_index):
    if seat_li == [[0] * M] * N:
        return [0, 0]
    else:
        seat_max = -sys.maxsize - 1
        seat_loc = [-1, -1]
        for i in range(N):
            for j in range(M):
                # print("iii", i, j)
                safty_min = sys.maxsize
                safty_loc = [-1, -1]

                if seat_li[i][j] == 0:
                    in_list = list(current_index.values())
                    # print("asdasd", in_list)
                    # [[i,j], [i,j], [i,j]] # dict_values
                    # print("ddd", in_list)
                    # print()
                    checker = False
                    for k in range(len(in_list)):  # current state index
                        d = ((in_list[k][0] - i) ** 2 + (in_list[k][1] - j) ** 2) ** 0.5
                        print("in_list", in_list)
                        print("i, j", i, j, end=" ")
                        print("d", d)
                        # [0,0]
                        # [1,0] # d: 1
                        if int(d) == 1:
                            checker = False
                            break  # 상하좌우

                        # print(safty_min)
                        if safty_min > d:
                            safty_min = d
                            safty_loc = [i, j]
                            checker = True
                        # print(safty_min)
                        # print(safty_loc)

                    if checker and seat_max < safty_min:
                        seat_max = safty_min
                        seat_loc = [safty_loc[0], safty_loc[1]]
                    # print(seat_max)
                    # print(seat_loc)
        return seat_loc


# in: 1
# in-out: 2 (in: 1, out: 2)
current_state = {}  # key: id, value: In/Out
current_index = {}  # key: id, value: location (list)
for i in range(len(work_li)):
    # print(f"{work_li[i][1]} ", end=" ")
    if work_li[i][0] == "In":
        if work_li[i][1] in current_state.keys():
            # message print
            if current_state[work_li[i][1]] == 1:
                # already seated
                print(f"{work_li[i][1]} already seated.")
            elif current_state[work_li[i][1]] == 2:
                # already ate lunch
                print(f"{work_li[i][1]} already ate lunch.")

        else:
            idx = get_index_of_possible_location(seat_li, current_index)
            # print("idx", idx)
            if idx == [-1, -1]:
                print(f"There are no more seats.")

            else:
                seat_li[idx[0]][idx[1]] = work_li[i][1]
                current_state[work_li[i][1]] = 1
                current_index[work_li[i][1]] = [idx[0], idx[1]]
                # print_2d_array(seat_li)
                print(f"{work_li[i][1]} gets the seat ({idx[0]+1}, {idx[1]+1}).")

        # 1) distance 비교해서 가장 먼 곳에 지정 (seat_li[i][j] = Id)
        # 2) current_state[Id] = 'In'

    else:  # "Out"
        if work_li[i][1] not in current_state.keys():
            print(f"{work_li[i][1]} didn't eat lunch.")
        elif current_state[work_li[i][1]] == 2:
            print(f"{work_li[i][1]} already left seat.")
        else:
            current_state[work_li[i][1]] = 2
            x, y = current_index[work_li[i][1]]
            seat_li[x][y] = 0
            print(f"{work_li[i][1]} leaves from the seat ({x+1}, {y+1}).")
# 안전도 체크는 어떻게?
