
# i: odd +1
# i: event +3

i = 1
cnt = 1
while (i < 11): 
    if i % 2  != 0:
        i += 1
    else:
        i += 3
    print(cnt)
    cnt += 1
    
cnt = 1        
for idx in range(1, 11):
    if idx % 2  != 0:
        idx += 1
    else:
        idx += 3
    print(cnt)
    cnt += 1
    