'''
1. N개의 구간으로 나뉨->구간의 총 합은 100m
2. 각 구간별 구간의 길이와 제한 속도 모두 양의 정수
'''

'''
- N, M 입력받기
- 구간 나누기
- 구간별로 어떻게 비교할 것 인가..
1. 구간 길이가 같아야 한다..
2. inspect와 lst비교
2-1. 만약 inspect의 길이가 total을 벗어나면 끝
2-2. 
3. 총 누적 검사 길이도 체크해야 함
'''

'''
질문 리스트
1. 정수를 공백을 기준으로 여러개 입력받기
2. 사이즈가 지정된 리스트 만들기
'''
N, M = input().split()
N = int(N)
M = int(M) 
print(N)
print(M)


lst_section = [0] * N # [0,0,0,...]
lst_section = [0 for i in range(N)]
lst_speed_lim = [0 for i in range(N)] #ok, 만약 리스트 변수명이 section과 speed 였다면? 

for i in range(N):
    # str -> list: split()
    # list -> str: join()
    
    # map(func, sequence (list, tuple, str))
    section, speed = tuple(map(int, input().split())) # '50 50' -> ['50', '50']   
    # section, speed = [int(s) for s in input().split()]
    # int(input().split()) (X)
    
    lst_section[i] = section
    lst_speed_lim[i] = speed

print(lst_section)
print(lst_speed_lim)

lst_section_inspect = [0 for i in range(M)]
lst_speed_lim_inspect = [0 for i in range(M)]

for i in range(M):
    section, speed = tuple(map(int, input().split()))
        
    lst_section_inspect[i] = section
    lst_speed_lim_inspect[i] = speed    


inspect_length = 0 # 이러면 비교 길이가 맞지 않음, 누적거리를 비교해야함
section_length = 0 # 검사 구간 길이를 더해주는 기능이 필요, 구간 길이가 main
'''
* 검사 구간의 길이가 원래 구간 길이를 초과한다면
1. 원래 구간의 길이만큼 거리를 자른후 원래와 비교
1-1. 그렇다면 현재 조사 구간의 길이를 알아야 함
2. 남은 거리만큼 원래 구간과 비교하여 계산

'''
# def get_index_of_inspect_section_length(current_inspect_length, lst_section):
#     t_len = 0
#     for i in range(len(lst_section)):
#         t_len += lst_section[i]
        
#         if t_len >= current_inspect_length:
#             return i    

max_sub = 0
acc_section_len = 0
for i in range(N): # section    
    current_section_length = lst_section[i]
    current_speed_lim = lst_speed_lim[i]
    acc_section_len += current_section_length
    
    print()
    acc_inspect_section_len = 0    
    for j in range(M): # inspect
        current_inspect_section_length = lst_section_inspect[j]
        current_inspect_speed_lim = lst_speed_lim_inspect[j]
        acc_inspect_section_len += current_inspect_section_length
        
        print(acc_inspect_section_len)
        print(current_inspect_section_length)
        if acc_inspect_section_len < acc_section_len:
            print(j)
            for k in range(j): 
                print()
                print(current_inspect_speed_lim, lst_speed_lim[k])
                if current_inspect_speed_lim > lst_speed_lim[k]:
                    max_sub = max(max_sub, current_inspect_speed_lim - lst_speed_lim[k])
           #current_sub = current_inspect_speed - lst_speed_lim[j]
           #if current_sub > max_sub: max_sub = current_sub 
         

#  if inspect_length > section_length:
#      lst_section
print(max_sub)    
    
#print(lst_section) 
#print(lst_speed_lim)
        