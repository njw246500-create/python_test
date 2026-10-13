# tuple : 리스트와 동일하지만 변경은 불가능함
# 소괄호 () -> 안써도 됨.

tup1 = (10,20,30,40)
tup2 = ('python', 4.67,90,True)
tup3 = 'python',4.67,90,True
print("tup3의 type = ", type(tup3))
# 데이터가 1개 일때 
tup4 = (10,)
tup5 = 10,
tup6 = 10

print("tup4의 type =", type(tup4))
print("tup5의 type =", type(tup5))
print("tup6의 type =", type(tup6))
print("-" * 30)

print(tup1[1])
print(tup3[3])
print("-"*30)

# error
# tup1[1] = 100 
# tup1.clear()

# 변수 자체를 삭제
del(tup1)
# print(tup1)

