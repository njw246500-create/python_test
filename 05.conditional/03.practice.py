# 문 : 점수를 입력받아서 짝수인지 홀수인지 판별하기

# 문2 : 2개의 정수를 입력받아 큰 값과 작은값을 판별하여 출력
# ex ) 3,7 => 큰값 : 7, 작은 값 : 3

# 문1 

print("문제1번")
print("-"*30)
score = int(input("점수를 입력해주세요"))
if score % 2 == 0 : 
    print("이 점수는 짝수입니다")
else :
    print("이 점수는 홀수입니다")


# 문2
print("문제2번")
print("-"*30)

number1 = int(input("첫번째 정수를 입력하세요"))
number2 = int(input("두번째 정수를 입력하세요"))

if number1 > number2 :
    print(f"큰 값 : {number1}, 작은 값 : {number2}")

if number1 < number2 : 
    print(f"큰 값 : {number2}, 작은 값 : {number1}")

if number1 == number2 :  
    print("두 값은 동일합니다")


if number2 > number1 : 
    number1, number2 = number2, number1 # 자리바꿈하기

print(f"큰 값 : {number1}, 작은 값 : {number2}")