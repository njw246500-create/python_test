import numpy as np

'''
<연습문제>

1. 1차원 배열 만들기
NumPy를 사용하여 1차원 배열 생성
[10 20 30 40 50]
'''
print("1번")  
data1 = [10, 20, 30, 40, 50]
# np.arange(10,60,10)
arr1 = np.array(data1)
print(arr1)
print('-'*30)
'''
2. 2차원 배열 만들기
NumPy를 사용하여  2차원 배열 생성
[[1 2 3]
 [4 5 6]]
'''
# 2번 
print("2번")
data2 = [1,2,3]
data3 = [4,5,6]
arr2 = np.array([data2, data3])
# np.array([[1,2,3],[4,5,6]])
print(arr2)
print('-'*30)

'''
3. arange()를 사용하여 5부터 20까지(20포함) 3씩 증가하는 1차원 배열을 생성

'''
# 3번 
print("3번")
arr3 = np.arange(5,21,3)
print(arr3)
print('-'*30)
'''
4. arange()로 1부터 12까지의 숫자를 생성한 뒤, reshape()를 이용하여 3행 4열의 배열로 변환
'''
print("4번")
arr4 = np.arange(1,13)
print(arr4)

arr5 = arr4.reshape(3,4)
print(arr5)
print('-'*30)


'''
5. linspace()를 이용하여 0부터 1까지 동일한 간격으로 나누어진 숫자 6개를 생성
'''
print("5번")
arr6 = np.linspace(0,1,6)
print(arr6)
print('-'*30)



'''
6. 모든 원소가 0인 3행 4열의 배열 생성
'''
print("6번")
arr7 = np.zeros((3,4))
print(arr7)
print('-'*30)




'''
7. 모든 원소가 1인 2행 5열의 배열 생성. 단, 데이터 타입은 정수형으로
'''
print("7번")
arr8 = np.ones((2,5),dtype = int)
print(arr8)
print('-'*30)


'''
8. 다음 조건을 만족하는 배열 생성
- 2부터 24까지 짝수를 생성
- 생성한 배열을 3행 4열로 변환한다.
'''
print("8번")
arr9 = np.linspace(2,24,12)
# np.arange(2, 25,2).reshape(3,4)
print(arr9)
arr10 = arr9.reshape(3,4)
print(arr10)
print('-'*30)

'''
9. 다음 조건을 만족하는 배열을 생성
- 10부터 50까지 균등한 간격의 숫자 9개를 생성
- 생성한 배열을 3행 3열로 변환
'''
print("9번")
ar11 = np.linspace(10,50,9)
print(ar11)
ar12 = ar11.reshape(3,3)
# np.linspace(10,50,9).reshape(3,3)
print(ar12)
print('-'*30)



'''
10. 다음 세 가지 배열을 각각 생성
1. arange()와 reshape()를 사용해 1부터 16까지의 숫자를 4행 4열로 만든다.
2. 모든 원소가 0인 4행 4열의 배열을 만든다.
3. 모든 원소가 1인 4행 4열의 정수형 배열을 만든다.
'''
#1번#
print("10-1번")
ar13 = np.arange(1,17)
print(ar13)
ar14 = ar13.reshape(4,4)
print(ar14)
print('-'*30)

#2번#
print("10-2번")
ar15 = np.zeros((4,4))
print(ar15)
print('-'*30)

# 3번 # 
print("10-3번")
ar16 = np.ones((4,4),dtype=int)
print(ar16)
print('-'*30)

'''
11. 4행 4열의 단위행렬을 생성(자료형 정수형(int))

'''
print("11번")
ar17 = np.identity(4, dtype = int)
print(ar17)
print('-'*30)


'''
12. 3행 5열의 배열에서 주대각선보다 한 칸 오른쪽에 1이 위치하도록 만들기
    자료형은 정수형으로 지정
'''
print("12번")
ar18 = np.eye(3,5,1, dtype = int)
print(ar18)
print('-'*30)

