jumsu = 87

'B학점'

if jumsu >= 80 and jumsu < 90 : print("B학점") # 한줄로도 가능함!!

score = int(input("점수를 입력하세요 : "))
if score >= 90 and score <= 100: 
    print("A학점")

if score >= 80 and score < 90 : 
    print("B학점")

if score >= 70 and score < 80: 
    print("C학점")

if score >= 60 and score < 70 : 
    print("D학점")

if score >= 0 and score < 60: # else 쓰면 안된다. else 쓰면 위에 60에서 70사이만 아닌값이 F로 출력됨. 
    print("F학점")


