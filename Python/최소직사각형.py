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



# for i in range(len(sizes)): # 가로, 세로 길이 모아놓기
#     for j in range(len(sizes[0])):
#         if j == 0:
#             w.append(sizes[i][j])
#         else:
#             h.append(sizes[i][j])
#
# longest_widx = 0
# longest_hidx = 0
# # 가장 긴 선분이 포함된 명함의 가로, 세로를 스위치->가로로 뒤집는다의 논리가..
# # 스위치-> 가장 긴 길이가 바뀜->그 안에 들어가는지
# for i in range(len(w)): # 가장 긴 길이의 idx를 알아야 함
#     if w[i] > longest_widx: # idx저장
#         longest_widx = w[i]
#
# for i in range(len(h)):
#     if h[i] > longest_hidx: # idx저장
#         longest_hidx = h[i]
#
# for i in range()
# sizes[longest_hidx] # 세로 길이가 가장 긴 순서쌍, swap이 필요


def solution(sizes):
    short = [0] * len(sizes)  # 50 30 30 40
    long = [0] * len(sizes)  # 60 70 60 80

    # [(), (), (), ]
    for i, size in enumerate(sizes):
        w, h = size
        long[i] = max(w, h)
        short[i] = min(w, h)
        # if w >= h: long[i], short[i] = w, h
        # else: long[i], short[i] = h, w

    res_short = max(short)
    res_long = max(long)

    A = res_long * res_short
    return A

sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
print(solution(sizes))


def solution2(sizes):
    max_w_idx, max_w = 0, 0
    max_h_idx, max_h = 0, 0

    for i, size in enumerate(sizes):
        w, h = size
        if w > max_w: max_w_idx, max_w = i, w
        if h > max_h: max_h_idx, max_h = i, h
    if max_w_idx == max_h_idx: return max_w * max_h

    # max_w_idx != max_h_idx
    # switch between max width and corresponding height
    w, h = sizes[max_w_idx]
    sizes[max_w_idx] = [h, w]
    new_max_w = max([w for w, h in sizes])
    new_max_h = max([h for w, h in sizes])
    if new_max_w < max_w and new_max_h <= max_h:
        max_w = new_max_w
        max_h = new_max_h
    else:
        sizes[max_w_idx] = [w, h]
    print(sizes)


    # switch between max height and corresponding width
    w, h = sizes[max_h_idx]
    sizes[max_h_idx] = [h, w]
    new_max_w = max([w for w, h in sizes])
    new_max_h = max([h for w, h in sizes])
    if new_max_h < max_h and new_max_w <= max_w:
        max_h = new_max_h
        max_w = new_max_w
    else:
        sizes[max_h_idx] = [w, h]

    print(sizes)
    return max_w * max_h


sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
print(solution2(sizes))
