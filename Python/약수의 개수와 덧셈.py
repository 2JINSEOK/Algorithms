'''
- left, right 가 매개변수로
- left<=      <=right
- 약수의 개수 짝수 : + 
- 약수의 개수 홀수 : -
'''

# 약수의 개수는 어떻게 구할 것인지
# 약수를
# 사이의 숫자는 배열로 저장해서?
 
# ex_li = []
ans = 0
for i in range(left, right + 1):
    if isinstance(i ** 0.5, int):
        ans -= i
    else:
        ans += i


# sum = 0        
# for i in range(left, right + 1):
#     sum += i # 100

# ans = sum
# for i in ex_li:
#     ans -= (i*2)
    
    
                 