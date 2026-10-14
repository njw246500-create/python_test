st1 = 'He likes apples, and she does, too'

# 특정문자 기준으로 문자열 분리
# 기본값 : 공백문자
# 결과값 : 리스트 

st2 = st1.split()
print(st1)
print(st2)
print('-'*50)

# ', '를 기준으로 분리
st2 = st1.split(',')
print(st2)

# 공백을 기준으로 3번만 분리
st2 = st1.split(' ',3) # 자르고 나머지는 몽땅 하나로
print(st2)

st2 = st1.split()
st3 = ','.join(st2)
print(st2)
print(st3)

