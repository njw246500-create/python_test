s = {1,2,3,1,2,3,4,1,3,5}

print(2 in s)
print(6 in s)

# 데이터 추가
s.add(10)
print(s)

#  update
s.update({5,11,12,13})
print(s)

# 개별 삭제 가능
s.remove(2)
print(s)

# 전체 데이터 삭제
s.clear()
print(s)