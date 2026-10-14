st1 = '12345'
st2 = 'pythonAi'
st3 = 'Python AI'
st4 = '이정은'
st5 = '1234abcd'

# 숫자만으로 구성되어 있는지 검사
print('숫자로만 구성되어 있는가?', st1.isdigit())
print('숫자로만 구성되어 있는가?', st2.isdigit())
print('숫자로만 구성되어 있는가?', st5.isdigit())
print("-"*50)

# 문자로만 구성되어 있는지 검사, 공백도 취급
print("문자로만 구성되어 있는가?", st1.isalpha())
print("문자로만 구성되어 있는가?", st2.isalpha())
print("문자로만 구성되어 있는가?", st3.isalpha())
print("문자로만 구성되어 있는가?", st4.isalpha())
print("문자로만 구성되어 있는가?", st5.isalpha())

# 숫자나 문자로 구성되어있는지 검사
print('숫자나 문자로 구성되어 있는가?', st1.isalnum())
print('숫자나 문자로 구성되어 있는가?', st2.isalnum())
print('숫자나 문자로 구성되어 있는가?', st3.isalnum())
print('숫자나 문자로 구성되어 있는가?', st4.isalnum())
print('숫자나 문자로 구성되어 있는가?', st5.isalnum())

# 문자열이 소문자인지 검사
st6 = st2.lower()
st7 = st3.lower()
print('st6 :', st6)
print('st7 :', st7)
print('문자열이 소문자인가?', st6.islower())
print('문자열이 소문자인가?', st2.islower())
print('문자열이 소문자인가?', st7.islower())
print('문자열이 소문자인가?', st4.islower())
print('문자열이 소문자인가?', st5.islower())

# 문자열이 공백문자인지 검사
st6 = '       '
print('문자열이 공백문자인가?', st6.isspace())
print("-"*50)

st1 = 'PythonAi'
st2 = 'Pythonai'
st3 = 'Python Ai'
st4 = 'Python AI'

# 단어의 첫글자가 대문자인지 검사
print("단어의 첫글자가 대문자인가?",st1.istitle())
print("단어의 첫글자가 대문자인가?",st2.istitle())
print("단어의 첫글자가 대문자인가?",st3.istitle())
print("단어의 첫글자가 대문자인가?",st4.istitle())

# 빈자리를 0으로 채우기
st1 = 'Hello Python!!'
st2 = st1.zfill(20) # 20자리 중에서 빈칸은 0으로 채우시오.
print(st1)
print(st2)