#!/usr/bin/env python
# coding: utf-8



"""
- 알파벳으로 이루어진 문자열을 암호화

*  한 번에 두 글자 단위로 암호화를 진행
* I와 J를 동일한 것으로 생각. 
* 두 글자로 이루어진 쌍 파괴
-------------------------------------------------------------------------------------
0. 5*5 크기의 표로 변환

1. 키를 한 글자씩 보면서 왼쪽 위 칸부터 한 줄씩 채운다
2. 이전에 봤던 알파벳이 한번 더 등장하면 무시하고 다음 글자
3. 키를 다 보고도 칸이 남는다면, 아직 등장하지 않은 알파벳을 순서대로 채워넣는다
-------------------------------------------------------------------------------------
0. 메세지를 두 글자씩 나눈다.

1.같은 두 글자로 이루어진 쌍이 생기면 가장 앞에 있는 쌍 사이에 X를 넣고 뒤쪽은 새롭게
쌍 구성
2.마지막에 한 글자가 남는다면 X를 덧붙여 강제로 쌍을 맞춘다
-------------------------------------------------------------------------------------
0. 쌍을 만든 두 글자를 암호화한다.

1. 두 글자가 표에서 같은 행에 존재->오른쪽으로 한 칸 이동한 칸에 적힌 글자로 암호화
2. 두 글자가 같은 열에 존재->아래쪽으로 한 칸 이동한 칸에 적힌 글자로 암호화
3. 두 글자가 표에서 서로 다은 행, 열에 존재->두 글자가 위치하는 칸의 열이 서로 교환된
위치에 적힌 글자로 암호화
"""


'''
1. 문자를 입력받는다
2. 입력받은 문자열을 5*5형태로 바꿔준다->for?,리스트,다시 for?
3. 그렇다면 5*5형태는 어떻게?->일렬로 출력되게끔
4. 5*5형태로 출력이 되어야하나->5로 나누었을때 나머지가 0이라면 다음줄로 enter
5. 지금까지 사용한 알파벳을 리스트에 저장하여 알파벳의 중복여부 확인
6. 그렇다면 각각의 행을 어떻게 저장할 것인지->append?
'''

dup = [] # 중복을 제거하기 위해 (키를 이용해서 5X5 판을 만들 때)
msg_str = input()
msg_str2lst = list(msg_str) 
key_str = input()

# string.h vs char[]

# string str = "hello"
# char chs[] = "hello"

#key_str2lst = list(key_str)

# 5 x 5 array for key init.
# list.append()
# list[i] = 
# [[0,0,0,0,0][][][][]]

# key_str2lst = [] 
key_str2lst = [ [0, 0, 0, 0, 0] for _ in range(5) ]
alphabet = [ chr(i) for i in range(65, 91) if chr(i) != "J" ]
checker = [ False for i in range(65, 91) if chr(i) != "J" ]

# ['A' ..... "Z"]
# [False, ... False]
# alphabet[idx]
# checker[idx]: alphabet[idx]의 사용 여부 

#print(alphabet)



i = 0
k = 0
# print(len(key_str2lst))
# print(len(key_str2lst[0]))
# print(len(key_str))
cnt = 0
while(i < len(key_str2lst)): # row=5, [[0,0,0,0,0][0,0,0,0,0][0,0,0,0,0][0,0,0,0,0][0,0,0,0,0]]
    j = 0
    while(j < len(key_str2lst[0])): # col, len(key_str2lst[0] = 5(열의 개수)
        cnt += 1
        #print(cnt)
        #print(i, j, k)
        if k < len(key_str):
            #print('if')
            if key_str[k] not in dup: # key_str[k]번째 원소가 dup[]에 존재하지 않는다면
                # push key_str[] into key_str2lst[i][j]
                # push key_str[] into tmp
                dup.append(key_str[k]) # 이미 추가된 원소가 아니라면 dup[]에 추가  
                key_str2lst[i][j] = key_str[k]
            
                # get ascii code of key_str[]: A => 65-65 = 0
                # checker False to True
                # if key_str2lst[i][j] > 'J':
                #    key_ord = ord(key_str2lst[i][j]) - 1 
                #else:
                #    key_ord = ord(key_str2lst[i][j]) 
                
                key_ord = ord(key_str2lst[i][j]) if key_str2lst[i][j] <= 'J' else ord(key_str2lst[i][j]) - 1 
                # K: 75
                checker[key_ord-ord('A')] = True # K-A: 10, 
                # ex) k == 75, 75-- 65 = 10
                # a b c d e f g h i  k l 
                # 0 1 2 3 4 5 6 7 8  9 10
                
                j += 1
            k += 1
        elif k == len(key_str): # key를 다 돌은경우
            #print('elif')
            # fill with not used character 
            for idx in range(len(checker)): # checker에 어떤 알파벳이 사용이 되었는지
                if not checker[idx]:
                    key_str2lst[i][j] = alphabet[idx] #5*5표에 idx에 해당하는 알파벳을 채워준다, alphabet과 checker의 인덱스는 같다
                    checker[idx] = True # 이미 사용한 알파벳으로 전환
                    break # 다음 칸으로 넘어간다
            j += 1 
    # print('iiii', i) 
    i += 1  # 행을 바꾼다       
# print(key_str2lst)
# print(dup)
# print(checker)
# print(msg_str2lst)    
#msg_dup = []

#for(int i = start; i < stop; i+=step)
# range(start, stop, step)

# sequence datatype (indexing, slicing, in, len(), membership)
# li[start:stop:step]
# s[start:stop:step]
# tuple[start:stop:Step]


# 1) ['HE', 'LL', ]
# 2) [['H', 'E'], ['L', 'L'], ]



# li.append vs li[i] = data
# li.append(l) vs li.extend(l)
# li = [1, 2]
# l = [3, 4]

# [1, 2, [3, 4]]
# [1, 2, 3, 4]

# helloworld->msg
# i: he ll ow or ld e
#

# hx hh ll o
# hhhllo/hx hh ll o
li = [] # 두 개씩 알파벳을 쪼개 넣는다 [[] []...]
for i in range(0,len(msg_str2lst),2): # 두 개씩 0, 2, 4, 6,... 
    li.append(msg_str2lst[i:i+2]) # 알파벳을 두 개씩 끊는다
    #print(msg_str2lst[i:i+2])
#print(li)

i = 0
new_li = []
while i < len(li):
    tmp = []
    left = []
    if len(li[i]) == 2:
        if li[i][0] == li[i][1]: # 두 글자가 서로 같다면
             # code
            tmp = [li[i][0], 'X'] if li[i][0] != 'X' else [li[i][0], 'Q']
            new_li.append(tmp) # 새로 조합된 단어를 저장
            left = [li[i][1]] #  leftover
            
            for j in range(i+1,len(li)): # [[]->[]]
                if len(li[j]) == 2: # [['a', 'b']]
                    left.extend([li[j][0], li[j][1]]) 
                else: # [['a']]
                    left.extend([li[j][0]])
            #print('left', left)
            
            i = 0
            li = []
            for k in range(0, len(left),2):
                li.append(left[k:k+2])
        else:
            new_li.append(li[i])     
            i += 1 
    else: # len(li[i]) != 2
         new_li.append([li[i][0], 'X'])
         i += 1
          
    #print(new_li)                        
    #[ , ]    
# 1) key_str len (k) < 25  
# 2) key_str len == 25
# 3) key_str len > 25 (dont need to consider (total alphabet : 25 (i=j)))


#c[1][2]
#print(key_str2lst)

def getLocationofKey(li, key_str2lst): 
    save_idx = []
    for i in range(len(key_str2lst)): # row = 5
        for j in range(len(key_str2lst[i])): # 열
            if li[0] == key_str2lst[i][j]: # 두 개씩 쪼개서 넣은 li
                save_idx.append((i, j)) # 첫번째 글자 해당되는 위치 저장
                
    for i in range(len(key_str2lst)):
        for j in range(len(key_str2lst[i])):
            if li[1] == key_str2lst[i][j]:
                save_idx.append((i, j)) # save_idx = [[i1 , j1], [i2 , j2]]
                
    return save_idx # 위치 좌표 반환

    
def isSameRow(index):
    return index[0][0] == index[1][0]

def isSameColumn(index):
    return index[0][1] == index[1][1]

i = 0
j = 0
k = 0 # first index of new list
while k < len(new_li):
    index = getLocationofKey(new_li[k], key_str2lst)# [[i1 , j1], [i2 , j2]]
    if isSameRow(index): # key_str2lst에서 index가 정확히 의미하는 바
        new_li[k][0] = key_str2lst[index[0][0]][(index[0][1]+1) % len(key_str2lst[0])]
                                # [      i1   ][(j1 + 1) % 5-> 나머지                ]
        new_li[k][1] = key_str2lst[index[1][0]][(index[1][1]+1) % len(key_str2lst[0])]
    elif isSameColumn(index):
        new_li[k][0] = key_str2lst[(index[0][0]+1) % len(key_str2lst)][index[0][1]]
        new_li[k][1] = key_str2lst[(index[1][0]+1) % len(key_str2lst)][index[1][1]]
    else:
        # 기존 문자의 row, col 저장
        # 두 문자의 row 그대로, col만 바꿔준다->바뀐 idx 저장->해당위치 문자 찾는다 swap
        # 그렇다면 new_li의 idx를 어떻게 접근할 것인가
        # tmp1 = []
        # tmp2 = [] # 위치 좌표 값 저장
        
        # for i in range(len(index[0])):
        #     for j in range(index[0][i]):
        #         tmp1.append(index[0][i]) # index 저장
                
        # for i in range(len(index[1])):
        #     for j in range(index[1][i]):
        #         tmp2.append(index[0][i])
        
        # index[0][1] = index[1][1] # 위치 좌표 대입
        # index[1][1] = tmp1[0][1] # 위치 좌표 교환
        
        new_li[k][0] = key_str2lst[index[0][0]][index[1][1]]
        new_li[k][1] = key_str2lst[index[1][0]][index[0][1]] 
    k += 1
        
#print(new_li)
res = ''
for i in range(len(new_li)):
    for j in range(len(new_li[0])):
        res += new_li[i][j]
        
print(res) # '[]' 
                #new_li[k][0] = key_str2lst[i][j+1]
                                   
        




