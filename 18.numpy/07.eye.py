import numpy as np

# 정방행렬, 단위행렬
# 행과 열이 같은 n x n 의 대각선이 모두 1이고 나머지는 0인 행렬
print(np.identity(5)) # 3행 3열 단위행렬
print('-'*30)

# 직사각행렬
# eye(N, M=None, k=0, dtype = float # 기본값이 실수)함수 
# N(필수) : 행(row)의 개수
# M(선택) : 열의 개수(지정하지 넣지 않으면 정방행렬 생성)
# k(선택) : 1을 채울 대각선의 위치 
# dtype(선택) : 배열의 데이터 타입

# 3x3 단위행렬 생성
arr1 = np.eye(3)
print(arr1)
print(f"배열 구조 : {arr1.shape}")
print('-'*30)

# 2 x 4
arr2 = np.eye(2, 3)
print(arr2)
print(f"배열 구조 : {arr2.shape}")
print('-'*30)

# 대각선의 위치 변경
# k가 양수이면 위로, 음수이면 아래로
# print(np.eye(5, k=2))
print(np.eye(4, 5, -2))

arr3 = np.eye(3, dtype = int)
print(arr3)