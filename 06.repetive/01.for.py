str = 'abcdefg'
for x in str :  # 지역변수 x -> for문 안에서만 사용함. 
    print(x)

print("-"*30)

num = [0,6,8,3]
for i in num : 
    print(i)


'''

range(시작값, 종료값, step) 
range(종료값) -> 시작값 default = 0, step default = 1
range(시작값, 종료값) -> step = 1


'''

for x in range (5) : # 0부터 4까지 
    print(x)

for x in range(3,10) : 
    print(x)
print("-"*30)

for x in range(1, 10, 3):
    print(x)

# 내 풀이 

for x in range(1, 20, 2):
    if x <= 17 : 
        print(x, end=', ') # 옆으로 나오게 하고싶을때
    else : 
        print(x)

# 정답

for x in range(1, 20, 2):
        print(x, end=', ') # 옆으로 나오게 하고싶을때
print()

for x in range(1, 20, 2) : 
    if x < 19 : 
        print(x, end = ', ')
    else : 
        print(x)

