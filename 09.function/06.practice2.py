# '''
# 문1 : 매개변수로 2개의 숫자와 연산자를 입력받아 출력

# (num1, num2, op)

# 문2 : 국어, 영어 점수를 사용자로 부터 입력받아 
#         함수로 평균을 입력받아 평균의 학점을 return 하기

# 문3 : 로또를 함수로 
# '''



# #문1#

# def calculator() :
#     x = input("첫번째 숫자를 입력하세요")
#     y = input("두번째 숫자를 입력하세요") 
#     z = input("연산자를 입력하세요")
#     print((x,y,z))

# calculator()

# #문2#
# import random
# def average(x,y) :
#     aver = (x+y)/2
#     return aver



# x = int(input("국어 점수를 입력하세요 : "))
# y = int(input("영어 점수를 입력하세요 : "))
# average(x,y)

# #문3# 
# ans = set()

# def lotto():
#     while len(ans) <=5 :
#         for i in range(6) : 
#             x = random.randint(1,45)
#             print(f"번호는 {x}나왔습니다")
#             ans.add(x)
#             i += 1
#     print(ans)
#     print(f"로또 번호는 {ans} 입니다.")

# lotto()

# #문4# 
# '''
# 문 4 :
# 입력한 비밀번호가 비밀번호 규칙에 맞으면 생성되고,
# 규칙에 맞지 않으면 다시 생성하도록 메시지를 출력하는 프로그램을 작성
# 1. 8글자 이상이어야 함import random


# 2. 문자 및 숫자로만 생성해야 하며 기호는 불가능

# 새로운 비밀번호를 입력하세요 : abcd
# 오류. 비밀번호가 규칙에 맞지 않습니다

# 새로운 비밀번호를 입력하세요 : abcd1234$$$
# 오류. 비밀번호가 규칙에 맞지 않습니다

# 새로운 비밀번호를 입력하세요 : 1234abcd
# 비밀번호가 생성 되었습니다
# '''

# def password() : 
#     a = input("새로운 비밀번호를 입력해주세요 : ")

#     if len(a) < 8 or len(a) > 8: 
#         while len(a) < 8 or len(a) > 8: 
#             a = input("오류. 비밀번호가 규칙에 맞지 않습니다.\n새로운 비밀번호를 입력하세요 : ")
#             if len(a) == 8 : 
#                 break

#     if a.isalnum() == False :
#         while a.isalnum() == False : 
#             a = input("오류. 비밀번호가 규칙에 맞지 않습니다.\n새로운 비밀번호를 입력하세요 : ")
#             if a.isalnum() == True : 
#                 break

#     print('비밀번호가 생성 되었습니다.')


# password()


## 정답 ##

# 문1# 
import random

def calc(v1, v2, op) : 
    result = 0
    if op == '+' :
        result = v1 + v2
    elif op == '-' :
        result = v1 - v2
    elif op == '*' :
        result = v1 * v2
    elif op == '/' :
        result = v1 / v2
    return result

# val1 = int(input('숫자입력 : '))
# val2 = int(input('숫자입력 : '))
# oper = input('연산자입력 : ')
# print(calc(val1, val2, oper))

#문제 2
# kor = int(input('국어점수 입력 : '))
# eng = int(input('영어점수 입력 : '))
# avg = (kor + eng) / 2

# def grade(avg) : 
#     if avg >= 90 : return 'A'
#     elif avg >= 80 : return 'B'
#     elif avg >= 70 : return 'c'
#     elif avg >= 60 : return 'D' 
#     else : return 'F'

# print(grade(avg), '학점입니다.')


#문제3# 

def lotto() : 
    lotto_set = set()
    while len(lotto_set) < 6 : 
        num = random.randint(1,45)
        lotto_set.add(num)

    lotto_list = sorted(lotto_set)
    print(f"오늘의 행운 번호 : {lotto_list}")

lotto()

#문제4#
def checkPwd(pwd) : 
    # if len(pwd) < 8 : 
    #     return False
    # if pwd.isalnum() : 
    #     return True
    # else : 
    #     return False

    if len(pwd) >= 8 and pwd.isalnum() : 
        return True 
    else : 
        return False

password = input("비밀번호 입력 : ")
if checkPwd(password) : 
    print(("비밀번호가 생성되었습니다."))
else : 
    print("비밀번호 규칙에 맞지 않습니다.")