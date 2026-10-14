'''
문
로또 프로그램 만들기

사용자로부터 몇 회분을 살건지 물어보고 
그 횟수만큼 번호를 랜덤으로 추출하여 출력하기

1회
2, 14, 26, 32, 41, 43


2회
5, 17, 25, 32, 41, 43


# '''
# import random
# a = int(input("로또를 시작합니다. 몇회분을 하실 예정이신가요?"))

# for count in range(a) : 
#     result = set()
#     for x in range(6) : 
#         number = random.randint(1,45)
#         result.add(number)
#     while len(result) <= 5 :
#         number = random.randint(1,45)
#         result.add(number)
#     print(result)
#     print("6개가 전부 출력되었습니다.")
#     print(f"6개의 숫자는 {sorted(result)}입니다. ") # sorted 해야함!! set은 순서없으니까


## 정답 

import random
count = int(input("몇회분을 구매하시겠습니까? "))
print(f"\n------- 로또 {count}회분 생성 결과 -------")
for i in range(count) : 

    lotto_set = set()
    while len(lotto_set) < 6 : 
        num = random.randint(1,45)
        lotto_set.add(num)

    lotto_list = sorted(lotto_set)
    print(f"{i+1}회차 : {lotto_list}")
