# 중첩 for 문

for i in range(3) : # 0, 1, 2
    for j in range(2) : # 0, 1
        print(f"i = {i}, j = {j}")

print("-"*30)

for dan in range(2, 10) : 
    print('  ', dan, '단')
    for i in range(1,10) : 
        print(f'{dan} * {i} = {dan*i}')
    print()

# 구구단 가로

'''
2*1 = 2  3*1 = 3  4*1 = 4 ... 9*1 =  # 안변하는거 바깥에꺼
2*2 = 4  3*2 = 6                     # 변하는거 안쪽꺼
...
2*9 = 18
'''

for i in range(1,10) : 
    for dan in range(2,10) :
        # print('%d*%d=%2d', %(dan, i, dan*i), end = '   ') # 끝에 바꾸기-> end  = '   '
        print(f"{dan}*{i}={dan*i:2d}", end = '   ')
    print()

    