# continue 아래는 실행하지 않고 반복문으로 다시 올라감

x = 1
while True : 
    print(x)
    x += 1

    if x == 6 :
        x += 2
        continue # 다시 while 문을 돌리기

    if x == 10 : # 10 출력 안함. 
        break 

    # 1~100까지의 합계 중 4의 배수는 제외하고 합계를 구하시오.

sum = 0
for i in range(1,101) : 
    if i % 4 == 0:
        continue 
    sum += i 
print("1~100까지의 4의 배수를 제외한 합계 : ", sum)