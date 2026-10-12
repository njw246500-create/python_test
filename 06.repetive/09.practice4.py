import random
# x = random.random()
# i = random.randint(1,3) # end 포함 -> 1,2,3 중에서 랜덤으로 하나 추출함. 
# print(x)
# print(i)

# 문제 : 주사위를 3개를 동시에 던져서 동일한 숫자가 나오면 탈출하는 게임
# 출력 : 주사위에 나온 숫자와 횟수 출력 
# count = 0
# while True :
#     print("주사위 세개를 던지겠습니다")
#     x = random.randint(1,6)
#     y = random.randint(1,6)
#     z = random.randint(1,6)

#     if x == y and y == z and x == z :
#         print(f"세개의 숫자는 {x}, {y}, {z}로 모두 같게 나왔습니다. 게임이 종료되었습니다.")
#         break
#     else : 
#         print(f"숫자 세개는 {x}, {y}, {z}에요. 세개가 아직 동일하지 않습니다. 다시 실행할게요")
#         count += 1
#         continue 

# 문제 : 주사위의 숫자 맞추기. 몇회만에 맞췄는지 , 맞힐때까지 무한반복

print("주사위의 숫자를 맞춰보세요")
i = 0
while True : 
    
    a = int(input("1~6까지의 숫자중 하나를 입력하세요."))
    b = random.randint(1,6)
    
    if a == b : 
        print(f"당신의 숫자 {a}와 주사위의 숫자{b}가 일치합니다. {i}번 실행해서 맞췄습니다.게임을 종료할게요.")
        break
    else :
        print(f"당신의 숫자는 {a} 이지만 주사위는 {b}로 서로 일치하지 않습니다. 다시입력해주세요")
        i += 1
        continue



## 정답
count = 0
while True : 
    count += 1
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice3 = random.randint(1,6)

    if dice1 == dice2 == dice3 : 
    # if (dice1 == dice2) and (dice2 == dice3) : 
        break
print("주사위의 숫자 :", dice1)
print(count, '번에 맞혔습니다')

## 정답 
count = 0
while True : 
    count += 1
    print(f"게임 {count}회")
    com = random.randint(1,6)
    user = int(input("주사위의 숫자는 어떤 숫자일까요?"))
    if com == user :
        # print('정답입니다.', count, '회에 맞췄습니다.')
        break
    else : 
        print("안타깝네요", com, '입니다. 다시합니다')
        continue