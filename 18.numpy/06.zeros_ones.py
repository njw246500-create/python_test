import numpy as np

# 모든 값이 0인 numpy 배열 생성
arr1 = np.zeros(10)
print(f"arr1 데이터 : {arr1}")

arr2 = np.zeros((2,3))
print(f"arr2 데이터 : {arr2}")

arr3 = np.zeros((2,3, 3))
print(f"arr3 데이터 : {arr3}")

# 모든 값이 1인 numpy배열 생성
arr4 = np.ones(10)
print(f"arr4 데이터 : {arr4}")

arr5 = np.ones((2,3))
print(f"arr5 데이터 : {arr5}")

arr6 = np.ones((2, 3, 3))
print(f"arr6 데이터 : {arr6}")