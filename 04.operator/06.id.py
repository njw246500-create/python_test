a = 1
b = 2
print(f"a의 주소 : {id(a)}")
print(f"b의 주소 : {id(b)}")
print(a is b)
print('-' * 30)

c = 1
print(f"c의 주소 : {id(c)}")
print(a is c) # 데이터 값이 같으면 주소가 동일함. 

b = 1
print(f"b의 주소 : {id(b)}")
