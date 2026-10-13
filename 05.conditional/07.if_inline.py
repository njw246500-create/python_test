# 삼항 연산식

'''

if num1 == 2 :
    print("2입니다")
else :
    print("2가 아닙니다")
'''

num1 = 7
# print('2입니다') if num1 == 2 else print("2가 아닙니다") # if 참이면 앞에거 실행, 거짓일때 뒤에서 실행
# print('2입니다' if num1 == 2 else '2가 아닙니다')


# 합격, 불합격

# # 일반 조건문
score = 75
# if score >= 60:
#     result = '합격'
# else : 
#     result = '불합격'

# print("합격" if score >= 60 else '불힙격')

# 삼항연산자로 변수에 저장
result = '합격'if score >= 60 else '불합격'  
print(result)

# 두 수 중 큰 수 찾기

num2 = 13
num3 = 7

max_num = num2 if num2 > num3 else num3 
print(f"{num2}과 {num3}중 큰 숫자는 {max_num} 입니다. ")

# 회문 : 왼쪽에서 읽은 것과 오른쪽으로 읽었을 때 같은 문자열

str = 'abcdcba' 

if str == str[::-1] : 
    print(f"{str} : 회문")
else :
    print(f"{str} : 회문 아님")


print(str, ': 회문' if str == str[::-1] else ': 회문 아님')
print(f"{str} : {': 회문' if str == str[::-1] else ': 회문 아님'}") # 따옴표 분류 잘 하기 