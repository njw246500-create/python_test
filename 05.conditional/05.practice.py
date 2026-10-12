# 문 : 점수를 입력받아 학점 출력
# 101점 이상, 음수입력시 잘못넣었다고 해야함

jumsu = int(input('점수 입력 :'))

if jumsu > 100 : 
    print("점수가 100을 넘어갔습니다. 다시입력하세요")

elif jumsu >= 90 :
    print("A학점")
elif jumsu >= 80 :
    print("B학점")
elif jumsu >= 70 :
    print("C학점")
elif jumsu >= 60 : 
    print("D학점")
elif jumsu >= 0 :
    print("F학점")
else :
    print("점수가 0보다 작습니다. 다시입력하세요")

### 

###

if jumsu >= 90 and jumsu <= 100 : 
    print("A학점")
elif jumsu >= 90 :
    print("A학점")
elif jumsu >= 80 :
    print("B학점")
elif jumsu >= 70 :
    print("C학점")
elif jumsu >= 60 : 
    print("D학점")
elif jumsu >= 0 :
    print("F학점")
else :
    print("점수가 0보다 작습니다. 다시입력하세요")

###

###

if jumsu >= 0 and jumsu <= 100:
    if jumsu >= 90:
        print("A학점")
    elif jumsu >= 90 :
        print("A학점")
    elif jumsu >= 80 :
        print("B학점")
    elif jumsu >= 70 :
        print("C학점")
    elif jumsu >= 60 : 
        print("D학점")
    else :
        print("F학점")
elif jumsu < 0: 
    print("음수는 점수가 될 수 없습니다.")
else :
    print("100이 만점입니다. 작은 점수를 입력하세요.")

###

###

if jumsu < 0 or jumsu > 100 : print('점수가 올바르지 않습니다.')
elif jumsu >= 90: print("A학점")
elif jumsu >= 80: print("B학점")
elif jumsu >= 70: print("C학점")
elif jumsu >= 60: print("D학점")
else: print("F학점")