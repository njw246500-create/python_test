
import numpy as np

'''
1. 다음 배열에서 정수형 배열을 생성하고, 변환된 배열의 자료형 및 원본 배열 출력
a = np.array([1.8, 2.5, 3.9, 4.2, 5.7])
'''
# 1번
a = np.array([1.8, 2.5, 3.9, 4.2, 5.7])
arr1 = a.astype(int)
print(arr1)
print(arr1.dtype)
print('-'*30)


'''
2.배열만들기
2.1. 0 이상 1 미만 실수 난수: 2행 3열
2.2. 1 이상 10 이하 정수 난수: 3행 4열
2.3. 표준정규분포 난수: 2행 2열
'''
#2번
from numpy import random

# rand() : 0~1 사이의 실수
b1 = random.rand(2,3)
print(b1)
print('-'*30)

b2 = random.randint(1,11,size = (3,4))
print(b2)
print('-'*30)

b3 = random.randn(2,2)
print(b3)
print('-'*30)

'''
3. 배열 a = [10, 20, 30, 40], b = [2, 4, 5, 8]을 만들고 
    두 배열의 덧셈, 뺄셈, 곱셈, 나눗셈을 각각 출력

'''


a = [10, 20, 30, 40]
b = [2,4,5,8]
a1 = np.array(a)
b1 = np.array(b)
print("두 배열의 덧셈 : ", a1+b1)
print("두 배열의 뺄셈 : ",a1-b1)
print("두 배열의 곱셈 : ",a1*b1)
print("두 배열의 나눗셈 : ",a1/b1)
print('-'*30)

'''
4. 배열 [12, 15, 18, 20, 25, 30]의 합계, 평균, 최댓값, 최솟값, 중앙값, 표준편차를 각각 구하기
'''
c = [12, 15, 18, 20, 25, 30]
c1 = np.array(c)
print(f"합계 : {c1.sum()}")
print(f"평균 : {c1.mean()}")
print(f"최댓값 : {c1.max()}")
print(f"최솟값 : {c1.min()}")
print(f"중앙값 : {np.median(c1)}")
print(f"표준편차 : {c1.std()}")
print('-'*30)

'''
5. 다음 2차원 배열의 전체 평균, 행별 평균, 열별 평균, 전체 합계, 행별 합계, 열별 합계를 구하기
a = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
'''
d = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print(f"전체 평균 : {np.mean(d)}")
print(f"행별 평균 : {np.mean(d, axis = 1)}")
print(f"열별 평균 : {np.mean(d, axis = 0)}")
print(f"전체 합계 : {np.sum(d)}")
print(f"행별 합계 : {np.sum(d, axis = 1)}")
print(f"열별 합계 : {np.sum(d, axis = 0)}")
print('-'*30)


'''
6. 다음 배열의 전체 최솟값, 행별 최솟값, 열별 최솟값, 전체 중앙값, 행별 중앙값, 열별 중앙값을 구하기
a = np.array([[8, 3, 5], [2, 9, 4], [7, 1, 6]])

'''
e = np.array([[8, 3, 5], [2, 9, 4], [7, 1, 6]])
print(f"전체 최솟값 : {np.min(e)}")
print(f"행별 최솟값 : {np.min(e, axis = 1)}")
print(f"열별 최솟값 : {np.min(e, axis = 0)}")
print(f"전체 중앙값 : {np.median(e)}")
print(f"행별 중앙값 : {np.median(e, axis = 1)}")
print(f"열별 중앙값 : {np.median(e, axis = 0)}")
print('-'*30)


'''
7. 아래 배열에서 인덱싱과 슬라이싱으로 출력하기
a = np.array([[10, 20, 30, 40],
              [50, 60, 70, 80],
              [90, 100, 110, 120],
              [130, 140, 150, 160]])


7.1. 값 70
7.2. 첫 번째 행 전체
7.3. 세 번째 열 전체
7.4. 오른쪽 아래 2행 2열
7.5. 두 번째~네 번째 행, 두 번째~세 번째 열
'''
f1 = np.array([[10, 20, 30, 40],[50, 60, 70, 80],[90, 100, 110, 120],[130, 140, 150, 160]])


print("7.1. 값 70:", f1[1][2])
print("7.2. 첫 번째 행 전체:", f1[0, :])
print("7.3. 세 번째 열 전체:", f1[:,2])
print("7.4. 오른쪽 아래 2행 2열:", f1[1,1])
print("7.5. 두 번째~네 번째 행, 두 번째~세 번째 열:", f1[1:3, 1:3])
print('-'*30)


'''
8. 행렬 A = [[1, 2], [3, 4]], B = [[5, 6], [7, 8]]에 대해 계산
8.1. A와 B의 행렬곱
8.2. A의 전치행렬
8.3. B의 전치행렬
8.4. A * B와 A @ B를 비교
'''

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

A1 = np.array(A)
B1 = np.array(B)

print("8.1. A와 B의 행렬곱 : ",A1@B1)
print("8.2. A의 전치행렬 : ",np.transpose(A1))
print("8.3. B의 전치행렬 : ",np.transpose(B1))
print("8.4. A * B와 A @ B를 비교 : ", A1*B1, A1@B1)
print('-'*30)
'''
9. 행렬 A = [[4, 7], [2, 6]]의 역행렬을 구하고, A와 그 역행렬을 곱해 결과 출력
'''

A = [[4, 7], [2, 6]]
A2 = np.array(A)
print(np.linalg.inv(A2))
print(np.round(A2@np.linalg.inv(A2)))
print('-'*30)

'''
10. 아래 배열에서 각 행은 학생, 각 열은 국어·영어·수학 성적
scores = np.array([[80, 90, 70], [60, 75, 85], [95, 80, 90], [70, 85, 75]])

10.1. 전체 평균
10.2. 학생별 평균
10.3. 과목별 평균
10.4. 학생별 최솟값
10.5. 과목별 최댓값
10.6. 전체 중앙값
10.7. 학생별 중앙값
10.8. 과목별 중앙값
10.9. 세 번째 학생의 수학 점수
10.10. 첫 번째~두 번째 학생의 영어·수학 점수
'''
scores = np.array([[80, 90, 70], [60, 75, 85], [95, 80, 90], [70, 85, 75]])

print(f"전체 평균 : {np.mean(scores)}")
print(f"학생별 평균 : {np.mean(scores, axis = 1)}")
print(f"과목별 평균 : {np.mean(scores, axis = 0)}")
print(f"학생별 최솟값 : {np.min(scores, axis = 1)}")
print(f"과목별 최댓값 : {np.max(scores, axis = 0)}")
print(f"전체 중앙값 : {np.median(scores)}")
print(f"학생별 중앙값 : {np.median(scores, axis = 1)}")
print(f"과목별 중앙값 : {np.median(scores, axis = 0)}")
print(f"세 번째 학생의 수학 점수 : {scores[2,2]}")
print(f"첫번째, 두번째 학생의 영어, 수학점수 : {scores[[0,0],[1,2]]},{scores[[1, 1],[1,2]]}")







