'''
# 먼저 가장 긴 가로, 세로 길이를 파악 필요
- 어떻게 가로, 세로를 모을 것인가
- 가장 긴 길이에서 어떻게 줄일 것 인가..
- 가장 긴 선분이 포함된 명함의 가로, 세로를 스위치?
- 가장 긴 가로, 세로 쌍을 스위치->스위치 후 그 범위안에 들어가는지?
- 그렇다면 가장 긴 길이가 중복된다면?

# 명함을 가로, 세로 스위치 하는 경우를 생각

=> 가장 작은 지갑의 크기를 return
'''

sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
w = []
h = []

for i in range(len(sizes)): # 가로, 세로 길이 모아놓기
    for j in range(len(sizes[0])):
        if j == 0:
            w.append(sizes[i][j])
        else:
            h.append(sizes[i][j])

longest_widx = 0
longest_hidx = 0
# 가장 긴 선분이 포함된 명함의 가로, 세로를 스위치->가로로 뒤집는다의 논리가..
# 스위치-> 가장 긴 길이가 바뀜->그 안에 들어가는지
for i in range(len(w)): # 가장 긴 길이의 idx를 알아야 함
    if w[i] > longest_widx: # idx저장
        longest_widx = w[i]

for i in range(len(h)):
    if h[i] > longest_hidx: # idx저장
        longest_hidx = h[i]

for i in range()
sizes[longest_hidx] # 세로 길이가 가장 긴 순서쌍, swap이 필요
