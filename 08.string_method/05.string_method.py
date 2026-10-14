st1 = 'He likes apples, and she does, too'

# 가운데 맞춤
st2 = st1.center(50)
print(st1)
print(st2 + '*')

# 공백대신 '-'로 채움
st2 = st1.center(50, '-')
print(st2)

# 오른쪽 맞춤
st2 = st1.rjust(50)
print(st2)

st2 = st1.ljust(50)
print(st2 + '===')

# expandtabs() : 공백 8개가 들어가는 함수
st3 = '1\tand\t2'
print(st3)
st4 = st3.expandtabs()
print(st4)

print(repr(st3))
print(repr(st4))

print(len(st3))
print(len(st4))