'''
- 최대한 많은 부서의 물품을 구매해 준다
- 신청한 금액을 모두 지원
-> 최대 몇 개의 부서에 물품 지원이 가능한지 return
'''

'''
Q1. 빈 리스트 생성시 항상 사이즈를 알아야 하는지

'''

d = []
d.sort() # 크기 순서대로 나열
budget = input()
budget = int(budget) # 매개변수 str->int 전환

# budget 분배를 어떻게 할 것인가.. 
# 최대한 많은 부서에게 돌아가도록->가장 많이->예산이 작은 부서를 우선적으로
# 작은 부서를 먼저 나눠주는게 가장 많이..?

cnt = 0
for i in range(len(d)):
    budget = budget - d[i]
    if budget >= 0:
        cnt += 1 # 몇 개의 부서를 도는지 count
    else:
        break
    
    
