# import numpy as np 

# f1 = np.random.rand()
# print(f1)

# from numpy.random import rand, randint, randn
# f1 = rand()
# print(f1)

from numpy import random

# rand() : 0~1 사이의 실수
f1 = random.rand()
print(f1)

# 실수 10개의 배열 생성
f2 = random.rand(10)
print(f2)
print('-'*30)

# 실수 2행 3열의 2차원 배열 생성
f3 = random.rand(2,3)
print(f3)
print('-'*30)

# 실수 3차원 배열 생성
f4 = random.rand(3,2,3)
print(f4)
print('='*30)

# randint(low = 0, high, size=1)
# low <= 난수 < high 정수배열 생성
# size : n차원 

n1 = random.randint(10)
print(n1)
print('-'*30)

n2 = random.randint(1,10,size = (5,))
print(n2)
print(n2.shape)
print('-'*30)

n3 = random.randint(1,10,size=(2,3))
print(n3)
print(n3.shape)
print('-'*30)

n4 = random.randint(1,10,size = (2,3,4))
print(n4)
print(n4.shape)
print('-'*30)

# randn() : 표준정규분포(gaussian function) 난수 
weights = random.randn(2,3)
print(weights) # 전체 값의 평균 = 0