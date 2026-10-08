#index 번호 + 일때는 앞에서 부터 0부터 시작
#index 번호 - 일때는 뒤에서 부터 -1부터 시작
st1 = 'abcdefghijk'

print(st1[0])
print(st1[3])
print(st1[8])
print('-'*30)

print(st1[-3])
print(st1[-1])
print(st1[-4])
print('-'*30)

# 슬라이싱(slicing)
# [시작 : 끝 : step] -> step 생략하면 1씩 증가
print(st1[1:3])
print(st1[:3])
print(st1[2:])
print(st1[:]) # print(st1) 같은말
print('-'*30)

print(st1[1:9:2])
print(st1[1:9:3])
print(st1[::3])
print(st1[::-1]) # 순서를 뒤집을 때 사용
print(st1[::-2]) 
print(st1[5:1:-2])
print(st1[-1:-6:-1])
print('-'*30)

# 문자열 연결하기 : +
st2 = 'xyz'
st3 = st1 + st2
print(st1)
print(st2)
print(st3)

# 문자열 반복하기 : *
st4 = st2 * 3
print(st4)
print('-'*30)

# 문자열의 문자개수 확인
print(len(st1))

# indexing 에서는 문자를 변경못함.
# st1[0] = 'z'
st1 = 'z' + st1[1:]
print(st1)

st1 = st1[:2] + '한글' + st1[4:]
print(st1)