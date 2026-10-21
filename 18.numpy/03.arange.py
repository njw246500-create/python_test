# 범위를 지정하여 numpy 배열 생성
# arrange(start, end, step)
import numpy as np

arr1 = np.arange(0, 10, 2)
print(f"데이터 : {arr1}")
print(f"배열 구조 : {arr1.shape}")
print('-'*30)

arr2 = np.arange(1,10)
print(f"데이터 : {arr2}")
print(f"배열 구조 : {arr2.shape}")
print('-'*30)

arr3 = np.arange(5)
print(f"데이터 : {arr3}")
print(f"배열 구조 : {arr3.shape}")
print('-'*30)