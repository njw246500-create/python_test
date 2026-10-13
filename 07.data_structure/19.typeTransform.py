a = [1,2,3,4,5]
b = (6,7,8,9,10)
c = {11,12,13,14,15}

# 리스트를 set과 tuple로 변환
# list() : 리스트로 변환
# set() : set 으로 변환
# tuple() : 튜플로 변환
set1 = set(a)
print(set1)
print(type(set1),set1)

tuple1 = tuple(a)
print(tuple1)
print(type(set1), set1)
print(type(tuple1), tuple1)

list1 = list(b)
print(type(list1),list1)