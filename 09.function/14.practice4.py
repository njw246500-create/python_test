prices = [10000,20000,30000,40000]
# 20% 할인된 가격을 리스트로 만들어 출력하기. lambda 이용하기
print([(lambda x : x*0.8)(a) for a in prices])

# print([(lambda x : x**2)(a) for a in range(1,6)])

# 정답 

dis_prices = [
    (lambda p : p*0.8)(p) for p in prices
]
print(dis_prices)