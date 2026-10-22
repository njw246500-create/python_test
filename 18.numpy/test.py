import numpy as np

a = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

# axis = 0 층 
# axis = 1 행
# axis = 2 열

suma = a.sum(axis = 0) # (17,2+8,3+9) 이런식
print(suma)

sumr = a.sum(axis = 1) # (1+4, 2+5, 3+6) 이런식
print(sumr)
print(sumr.shape)


sumv = a.sum(axis = 2) # (1+2+3, 4+5+6, 7+8+9, 10+11+12) 이런식
print(sumv) ## 배열은 맨 끝에서부터 열, 그다음이 행

# 4차원 이상은 잘 안씀. 