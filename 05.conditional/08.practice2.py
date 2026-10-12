# 사용자로부터 두개의 수를 입력받고, 연산자도 입력받음

# 연산결과를 출력하기 

#  +, -, *, /, //, %, **

num1 = int(input("첫번째 수를 입력하세요"))
num2 = int(input("두번째 수를 입력하세요"))
k = str(input("연산자를 입력하세요"))

a = num1 + num2
b = num1 - num2
c = num1 * num2
d = num1 / num2
e = num1 // num2
f = num1 % num2
g = num1 ** num2

if k == '+' :
    print(num1, k, num2, '=', a)
    print(f"두수의 합 : {a}")
if k == '-' : 
    print(num1, k, num2, '=', b)
    print(f"두수의 차 : {b}")
if k == '*' : 
    print(num1, k, num2, '=', c)
    print(f"두수의 곱 : {c}")
if k == '/' :
    print(num1, k, num2, '=', d)
    print(f"두수의 나누기 : {d}")
if k == '//' :
    print(num1, k, num2, '=', e)
    print(f"두수의 몫 : {e}")
if k == '%' :
    print(num1, k, num2, '=', f)
    print(f"두수의 나머지 : {f}")
if k == "**" :
    print(num1, k, num2, '=', g)
    print(f"첫번째 수의 두번째수 제곱 : {g}")


# 양수, 홀수(짝수)인지 
# 음수이면서 홀수(짝수) 인지 

number = int(input("숫자를 입력하세요"))
if number >= 0 :
    if number % 2 == 0 : 
        print("0이거나 양수이면서 짝수입니다")
    else :
        print("양수이면서 홀수입니다.")
else :
    if number % 2 == 0 :
        print("음수이면서 짝수입니다.")
    else : 
        print("음수이면서 홀수입니다.")



###
###

if num1 == 0:
    print("0입니다")
else : 
    if num1 > 0:
        print("양수입니다.")
    else : 
        print("움수입니다")

    if num1 % 2 == 0:
        print("짝수입니다")
    else :
        print("홀수입니다")

print("-"*30)

if num1 == 0 : 
    print("0입니다")
else : 
   sign ='양수' if num1 > 0 else '음수' 
   parity = '짝수' if num1 % 2 == 0 else '홀수'

   print(sign, '입니다')
   print(parity, '입니다')
