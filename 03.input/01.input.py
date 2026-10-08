# 사용자로부터 입력받기
# name = input('이름을 입력하세요 : ')
# print(name + '님 환영합니다')

# kor = int(input('국어 점수를 입력하세요 : '))
# com = int(input('컴퓨터 점수를 입력하세요 : '))
# print(kor + com)

# int형변환의 우선순위 
kor = input('국어 점수를 입력하세요 : ')
com = input('컴퓨터 점수를 입력하세요 : ')
print(int(kor) + int(com))
print(int(kor + com)) # 문자열 + 문자열 한 후 int형으로 변환

# 
kor = int(input('국어 점수를 입력하세요 : '))
com = int(input('컴퓨터 점수를 입력하세요 : '))
print(kor + com) # 문자열 + 문자열 한 후 int형으로 변
print('%d + %d = %d' %(kor, com, kor + com))
print('%s + %s = %s' %(kor, com, kor + com)) # 보여줄때만 string으로
print(f'{kor} + {com} = {kor+com}')

