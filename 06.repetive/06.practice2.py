# 문제 : 두개의 숫자를 입력받아 합계 구하기, 무한반복

# 사용자가 첫번째 값에 0을 넣으면 종료
# 그렇지 않으면 무한반복

while True : # break 만날때가지 계속 반복된다.
    a = int(input("첫번째 숫자를 입력하세요(종료하려면 0)"))
    if a == 0:
        break
    b = int(input("두번째 숫자를 입력하세요"))

    print(f"{a} + {b} = {a+b}")
    print()
print('계산 종료')


        
