'''
문
로또 프로그램 만들기

사용자로부터 몇 회분을 살건지 물어보고 
그 횟수만큼 번호를 랜덤으로 추출하여 출력하기

1회
2, 14, 26, 32, 41, 43


2회
5, 17, 25, 32, 41, 43


'''
import random
a = int(input("로또를 시작합니다. 몇회분을 하실 예정이신가요?"))

for count in range(a) : 
    result = set()
    for x in range(6) : 
        number = random.randint(1,45)
        result.add(number)
    while len(result) <= 5 :
        number = random.randint(1,45)
        result.add(number)
    print(result)
    print("6개가 전부 출력되었습니다.")
    print(f"6개의 숫자는 {result}입니다. ")
