# Comprehension

# 특히 리스트에서 많이 사용 -> list comprehension 불림

# for문이나 if문을 한줄에 넣는다
# result = [0,0,0,0,0,0,0,0,0,0...100개]

# result = [0 for i in range(100)]
# print(result)

# result = [10 for i in range(100)]
# print(result)

# result = [i+1 for i in range(100)] # 원래는 0부터 돌아가서 99에서 끊김
# print(result)

# result = ["더조은" for i in range(100)]
# print(result)

# data = [3,5,7,9]
# result = [i**2 for i in data]
# print(result)

# numList = [int(input("숫자입력 : ")) for x in range(5)]
# print(numList)
# print('합계 : ', sum(numList))

# if와 for문이 함께 들어있을때 무조건 for 문 부터 !!
# <expression> for 변수 in <iterable>
# if만 있는 경우는 맨 뒤에 
# if-else 잇는 경우는 맨 앞에 

print("-"*30)
result = []
for num in range(1,20) : 
    if num % 2 == 0 : 
        result.append(num*3)

result = [num*3 for num in range(1,20) if num % 2 == 0 ]
print(result)

result = []
for num in range(1,10):
    if num % 2 == 0 : 
        result.append(num)
    else :
        result.append(0)

result = [num if num % 2 == 0 else 0 for num in range(1,10)]
print(result)

#1~5까지 ['홀수','짝수','홀수','짝수','홀수']
total = [f'홀수' if num % 2 != 0 else "짝수" for num in range(1,6) ]
print(total)

print("-" * 30)
# for문이 중첩으로 들어갈 때
result = []
for x in [1,2,3] : 
    for y in [10,20] : 
        result.append((x,y))

# [(1,10), (1,20), (2,10), (2,20) ...]

result = [(x,y) for x in [1,2,3] for y in [10,20]]
print(result)

result = []
for x in range(1,4) : 
    for y in range(1,4) : 
        if (x+y) % 2 == 0 :
            result.append((x,y))
        else: 
            result.append((0,0))
# if else 먼저쓰고 뒤에 for문을 작성하기
result = [(x,y) if (x+y) % 2 == 0 else (0,0) for x in range(1,4) for y in range(1,4)]
print(result)

# unpacking 
list1 = [(1,11),(2,21),(3,31)]
for (first, last) in list1 :
    print(first + last)
print("-"*30)

# result = [first+last for (first,last) in list1]
# print(result)

# print([first+last for (first,last) in list1])

# enumerate() : 인덱스번호와 데이터를 tuple의 형태로 반환
t = [1,5,7,33,39,52]
for p in enumerate(t) : 
    print(p)
print('-'*30)

for i, v in enumerate(t) : 
    print(f'index : {i}, value : {v}')

# zip() : 리스트들을 동일한 위치값을 묶어서 관리. tuple 로 반환, 두개만 들어갈 수 있음.
# 길이가 다르면 짧은 길이로 묶음 
list1 = [10, 20, 30]
list2 = [100,200,300]

for z in zip(list1, list2) : 
    print(z)

for a,b in zip(list1, list2) : 
    print(a+b)
    print(a*b)