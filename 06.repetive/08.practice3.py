# 무한반복으로 구구단 중 출력할 단수를 입력받아 출력하기

# 출력 후 구구단을 계속할 것인지 확인 'yes' 'no'

while True : 
    a = 0
    b = 0

    a = int(input("출력할 단수를 입력하세요 : "))

    for i in range(1,10):
        print(f"{a}*{i}={a*i}")

    b = input("구구단을 새로운 단으로 계속 실행할까요? 계속 : y, 중단 : n")

    if b == 'y':
        continue
    if b == 'n' : 
        print("구구단이 끝났습니다")
        break

    ### 정답

    ###

    while True : 
        dan = int(input("몇 단을 출력할지 입력 : "))
        for x in range(1,10) : 
            print(f"{dan}*{x}={dan*x}")

        choose = input("계속하려면 'y'입력 : ")
        if choose == 'y'or choose == 'Y' : 
        # if choose.lower() == 'y' :
            continue
        else : 
            print("프로그램 종료")
            break 


##lower() : 소문자로 바꾸기 upper() : 대문자로 바꾸기 

## 