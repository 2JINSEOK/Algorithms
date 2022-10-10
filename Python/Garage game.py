'''
- 자동차의 색이 같다면 모두 사라진다.
-> 게임을 3차례 반복, 주어진 조건에서 얻을 수 있는 가장 큰 점수
'''
'''
1. N 입력 받기
2. 3N줄 생성? 숫자들을 어떻게 저장할 것인지
2-1. for문을 통해 리스트를 생성한다
2-2. 각각의 리스트에 입력 받은 숫자를 저장한다(리스트안에 리스트)
2-3. 리스트 마다 숫자를 입력하려면?->처음부터 숫자를 같이 입력 받아야하는지,
아니라면 나중에 입력 받아도 상관이 없는지
2-3. 리스트에 한 번에 입력하려면?-> 각각의 리스트
3. 칸을 선택하고, 그걸 어떻게 지워나갈 것인지
3-0. N*N의 격자를 설정
3-1. 격자 안에서 임의의 한 칸을 설정
3-2. 선택된 숫자를 어떻게 계산할 것인지
'''
N = int(input())
#M = 3*N+1
#O = 3*N-1
input_lst = [[] for _ in range(3*N)] # 바깥쪽 리스트 초기화
#car_lst = []
for i in range(3*N): # 3N만큼 반복
    # map(f, seq (tuple, list, str))
    # car_lst = list(map(int, input().split()))
    
    # list comprehension
    car_lst = [int(element) for element in input().split()] # '1 1' -> ['1', '1']
    input_lst[i] = car_lst # ex) input_lst[0] = [1, 1]
    
    # '1 1' -> ['1', '1']
    # car_lst = input().split() 
    #car_lst = [x for x in input().split()]
    #for j in range(len(car_lst)):
    #    car_lst[j] = int(car_lst[j])
           
    #input_lst.append(list(map(int, input().split())))->이게 안되는 이유
#    car_lst = [] # [[]]에서 안쪽 리스트 생성
#    for j in range(N): # N회만큼 반복
#        car_lst.append(0) # 
#    input_lst.append(car_lst)    

print(input_lst) # [[1, 1], [2, 2], [1, 1], [3, 3], [4, 4], [1, 2]]

grid_lst = [] # [[4, 4], [1, 2]]
for i in range(2*N, 3*N): # 인덱스 표기법
    grid_lst.append(input_lst[i])
print(grid_lst) # [[4, 4], [1, 2]]

# d[key] = value
grid_lst_location = {} # {4:[(0,0), (0,1)], 1:[(1,0)], 2:[(1,1)]}, *?왜 grid_lst_location 변수를 두 번 설정?
grid_lst_set = [] # [4, 1, 2]
for i in range(N): # N = 2, [[4, 4], [1, 2]]
    for j in range(N): # grid_lst[i][j], grid_lst[1][1] = 2
        if grid_lst[i][j] not in grid_lst_set:
            grid_lst_set.append(grid_lst[i][j])
        
# ->        
grid_lst_location = {key: [] for key in grid_lst_set} # grid_lst_set에 들어있는 원소로부터 dic 생성
for i in range(N):
    for j in range(N):
        current_number = grid_lst[i][j] # [[4, 4], [1, 2]]
        grid_lst_location[current_number].append((i, j))        
print(grid_lst_set)
print(grid_lst_location) # *?, {4: [(0, 0), (0, 1)], 1: [(1, 0)], 2: [(1, 1)]}
        
        
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 하, 상, 좌, 우
# {4, [[(0,0), (0,1)], [(0,1), (0,0)] [(2,0), (2,1)], [(2,1), (2,0)]]}, *?
path = {key: [] for key in grid_lst_set} # [4, 1, 2], *? path의 역할
for i in grid_lst_set: # [4, 1, 2]
    for j in range(len(grid_lst_location[i])): # start point, len(grid_lst_loc) = 2
        print('iiii jjj', i, j)
        print('len', len(grid_lst_location[i]))
        start_point = grid_lst_location[i][j] # (0, 0)
        p = [start_point] # [(0, 0)], ok
        k = 0
        while k < len(direction): # *?
            row = p[-1][0] + direction[k][0] # *?
            col = p[-1][1] + direction[k][1]
            print(row, col)
            
            if (row, col) in p:
                k += 1
                continue
            
            if 0 <= row < N and 0 <= col < N and i == grid_lst[row][col]:
                p.append((row, col))
                k = 0
            else:
                k += 1
        path[i].append(p)
        print(path)
print(path[4])
# 1) calculate the score (area + #car)
'''
- 직사각형 최대의 면적은 그리드 사이즈
- 직사각형 면적 최소는 1
- 사라지는 자동차의 개수 -> 짝수 : 최소 직사각형의 넓이와 같나-> X
                        -> 홀수 : 
- 자동차의 개수를 카운트
- 그렇다면 면적은 어떻게 파악? -> 직사각형을 만드려면? -> 가로, 세로만 알면 ok                        
- 가로, 세로 = 열의 개수, 행의 개수
- 그리드 리스트에서 숫자 하나 선택 -> path 이용해서 같은 숫자에 모두 접근
- path를 이용하여 숫자가 몇개인지 파악, 경로 안으로 들어가서 
- len(path)가 가장 큰 것을 지목->가장 크므로 사라지는 개수가 많다 -> 하지만 len이 같다면?
- max_lop인 인덱스를 찾아서 사라지는 개수를 파악
- 결국 모든 경우의 수를 다 체크
'''
score = [] # score라는 빈 리스트를 만들어서 모든 score를 저장 -> 그 중 최대값을 뽑음

for i in grid_lst_set:
    if i in path:
        
        max_lop = 0 # lop = len of path[i][j]
        vanish_num = 0
        for j in path[i]: # path[4] 들어가서 첫번째 value
            if len(path[i][j]) > max_lop:
                max_lop = len(path[i][j])
        vanish_num = max_lop         
                    




# h.w.
# 1) calculate the score (area + #car)
# 2) calculate the depth of garage for next simulation
# ex) 3x3, if you choose 1 at the first step, you need to know depth array [3,0,0]
# 3) (not must) get the garage array for next simulation
        
        
def isMember(li, target):
    for i in range(len(li)):
        if li[i] == target:
            return True
    else: # i == len(li)-1
        return False
        
# for i in grid_lst:
#     for j in i:
#         vanish_num = 0
#         chosen_num = grid_lst[i][j]
#     if chosen_num = grid_lst[i][j+1] or chosen_num = grid_lst[i][j-1]:
#         vanish_num += 1
        
            
   
#    for j in range(N):
#        input_lst[i][j]
#for i in input_lst:
#    for j in car_lst:
#        j = list(map(int, input().split()))
        
#print(input_lst)

# calculate the score
'''
- 직사각형 최대의 면적은 그리드 사이즈
- 직사각형 면적 최소는 1
- 사라지는 자동차의 개수 -> 짝수 : 최소 직사각형의 넓이와 같나-> X
                        -> 홀수 : 
- 자동차의 개수를 카운트
- 그렇다면 면적은 어떻게 파악? -> 직사각형을 만드려면? -> 가로, 세로만 알면 ok                        
- 가로, 세로 = 열의 개수, 행의 개수
'''