
# nn = []
# for i in range(5):
#     nn.append(i)

# print(nn)

nn = [x for x in range(5)]
print(nn)

def inputNum(n) : 
    for x in n : 
        n[x] = int(input(f'{x+1}번째 정수 입력 : '))

inputNum(nn)
print(nn) # 사용자가 입력한 수로 덮어쓰기

def outputNum(n):
    print('--------------- 출력 ------------------')
    for i, v in enumerate(n) : 
        print(n[i], end='')
        # print(v, end='')

outputNum(nn)