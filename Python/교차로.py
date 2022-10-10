# 자신을 기준으로 오른쪽에 위치한 차량 존재 -> 1초 동안 출발x
# 각 위치마다 1초에 한 대씩만 교차로 통과 가능
# 1번 차량은 t1초 때에 w1 위치 진입
# 매초마다 모든 차량이 진입한 직후, 각 위치의 맨 앞 차량은 오른쪽에 차량이 없는지 확인
# 각 차량이 교차로를 통과하는 시각이 언제인지 계산

'''
1. N 입력받기
2. N개 줄 생성
3. 각각의 리스트에 시간 위치 저장
4. 리스트 원소 중 첫번째를 int형으로
5. 리스트 원소를 통해 시간을 계산
5-1. 시간을 정하기 전 우선순위를 먼저 배치..?
5-2. B > C(B출C출), A > B(A출B출), C > D(C출D출), D > A(D출A출), A=C, B=D

6. 리스트에서 동시 출발인 차량을 먼저 파악
6-1. 패스타임 후..?->패스타임을 리스트에 저장
6-2.

7. 패스타임을 바탕으로 순서 정하기
- 가장 빠른 패스타임을 지정?
- 패스타임 지정후 지정된 패스타임을 갖는 차량끼리 비교
7-1. 패스타임이 같은 경우
- 같은 패스타임끼리 위치를 비교
'''
import copy

    
def getPassedCarAtCurrentTime(cur_inter, len_key) -> tuple:
    passed = [] # 현재 시간에 통과할 수 있는 차량 리스트
    # 1 2 3
    # 1: 1 -> 2 -> 3
    # 2: 2 -> 3
    # 3: 3
    for i in range(len(cur_inter)):
        cur_car = cur_inter[i]
        right_car = getLocationofRightCar(cur_car, len_key)
        while right_car in cur_inter:
            cur_car = right_car
            right_car = getLocationofRightCar(cur_car, len_key)
        
        if cur_car not in passed:
            passed.append(cur_car)
            
    non_passed = cur_inter.copy()
    for pa in passed:
        if pa in non_passed:
            non_passed.remove(pa)
        
    return passed, non_passed
    
    
# 교차로 우선순위 차량 확인 (나의 오른쪽 차량의 교차로 번호가 반환) 
# B > C (B출C출), A > B (A출B출), C > D (C출D출), D > A (D출A출), A=C, B=D            
def getLocationofRightCar(car: str, len_key: int) -> str:
    return chr(ord(car) - 1 + len_key) if not chr(ord(car) - 1).isalpha() else chr(ord(car) - 1)


# 주어진 시간이 있을 때 현재 교차로 상황
def getCurrentLocationAtCurrentTime(cur_time: int, time_by_loc: dict) -> list:
    cur_inter = [] # intersection location
    for key in time_by_loc.keys(): # [(key, []), , , ,] 
        for j in range(len(time_by_loc[key])):
            if time_by_loc[key][j] == cur_time:
                #if key not in cur_inter:
                cur_inter.append(key)
    return cur_inter


if __name__ == '__main__':
    N = int(input()) # N 입력받기

    lst_tw = [[] for _ in range(N)] # tw 저장하는 리스트 생성, 설명 필요
    tnw = [0] * N # [element for element in input().split()]

    for i in range(N):
        tnw[i] = input().split()
        tnw[i][0] = int(tnw[i][0]) # 입력 숫자 str->int


    time_by_loc = {'A':[], 'B':[], 'C':[], 'D':[]}
    index_by_loc = {'A':[], 'B':[], 'C':[], 'D':[]}
    for i in range(len(tnw)): # 2       
        time_by_loc[tnw[i][1]].append(tnw[i][0])
        index_by_loc[tnw[i][1]].append(i)        
    
    
    
    
    # shallow copy: 1d copy
    # deep copy: 2d copy
    cur_time = tnw[0][0]
    passed_time = [-1 for _ in range(N)]
    
    idx = 0
    while True:
        # cur_inter = 3, 4, 5
        cur_inter = getCurrentLocationAtCurrentTime(cur_time, time_by_loc)
        
        if len(cur_inter) == 0: break
        elif len(cur_inter) >= 4: break
        
        
        passed_car, non_passed_car = getPassedCarAtCurrentTime(cur_inter, len(time_by_loc.keys()))
        if len(passed_car) == 1:
            if len(time_by_loc[passed_car[0]]) > 0 and len(index_by_loc[passed_car[0]]) > 0:
                passed_time[index_by_loc[passed_car[0]][0]] = cur_time
                time_by_loc[passed_car[0]].pop(0)
                index_by_loc[passed_car[0]].pop(0)
        else:
            for pc in passed_car:
                if len(time_by_loc[pc[0]]) > 0 and len(index_by_loc[pc[0]]) > 0:
                    passed_time[index_by_loc[pc[0]][0]] = cur_time
                    time_by_loc[pc[0]].pop(0)
                    index_by_loc[pc[0]].pop(0)
            
        cur_time += 1
        
        # non-passed car += 1
        for key in time_by_loc.keys():
            if key in non_passed_car:
                time_by_loc[key][0] += 1
                
    for pt in passed_time:
        print(pt)
        
        # 1) len(passed_car) == 1
        # 2) len(passed_car) == 4
        # 3) 1 < len(passed_car) < 4 
            
        
                


    # pass_time_lst = []

    # for i in range(N):    
    #     for j in range(N):
    #         pass_time = tnw[i][0] 
    #     pass_time_lst.append(int(pass_time))
    # pass_time_lst.sort() # 입력 시간을 오름차순으로 정렬
    # tnw.sort()

    # 정렬된 시간을 기준으로 위치값과 함께 저장
    # 정렬된 시간 리스트 따로, 위치 리스트 따로 생성..?
    # tnw.sort 활용
    # 시간이 같은 원소들끼리 위치를 비교 -> 그렇다면 시간이 같은 원소들을 어떻게 추출?
    # 결국 dic을 통한 재배열이 필요?

    # w_lst = [] # 위치값을 저장하기 위한 리스트 생성
    # for i in range(N):
    #     w = tnw[i][1]
    #     w_lst.append(tnw[i][1])
    # w_lst.sort()

    # tnw_lst = list(zip(pass_time_lst, w_lst)) # 각 시간별로 위치를 짝짓기

    # 시간별로 위치를 비교->순서 지정
    # A: [10], B: [10, 11], C: [], D: []
    # dict {'A': [10], 'B': [10, 11], 'C':[], 'D':[]}

    # B > C(B출C출), A > B(A출B출), C > D(C출D출), D > A(D출A출), A=C, B=D
    # current_time = 
    # for i in range(len(pass_time_lst)):
        




    # fst_ptm = 10^9 # fastest passtime     
    # for i in range(N):
    #     if fst_ptm > pass_time_lst[i]: # fst_ptm이 ptm보다 크면 ptm으로 대체
    #         fst_ptm = pass_time_lst[i] # 가장 빠른 ptm을 뽑아낸다->그것을 기준으로 차량정렬하기위해
            

    # 위치 비교
    # 위치를 따로 저장하는 리스트 필요..?
    # 시간과 위치를 함께 저장하여 dic활용..?
    # 굳이 시간을 나열할 필요가 있는가..
    # 시간이 같은 차량일 경우
    # 시간에 다른 차량일 경우
    #for i in range(N):
        
                
        
                
                
    # print(tnw[0][0])
    # print(pass_time)
    # print(pass_time_lst)
    # print(type(pass_time_lst[0]))
    # print(tnw[0][1])
    # print(tnw[1][1])
    # print(tnw[1][0])
    #print(tnw)

    # print(w_lst)
    # print(tnw_lst)
    #print(lst_tw)