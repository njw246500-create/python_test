st1 = 'He likes apples, and she does, too'

# 대문자로 
st2 = st1.upper()
print(st1)
print(st2)
print("-"*30)

# 소문자로
st2 = st1.lower()
print(st1)
print(st2)
print("-"*30)

# 대문자 <-> 소문자
st2 = st1.swapcase()
print(st1)
print(st2)

# 문장의 첫글자만 대문자로
st3 = st2.capitalize()
print(st2)
print(st3)
print('-'*30)

# 단어의 첫글자를 대문자로
st2 = st1.title()
print(st1)
print(st2)