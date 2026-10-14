st1 = 'He likes apples, and she does, too likes'

# 문자열에서 특정 문자열의 갯수를 구하시오
print(st1.count('like'))

# 왼쪽에서 오른쪽으로 문자열을 검색
p = st1.find("like")
print(p)
print(st1.find("like", p+1))
print(st1.find("love")) # 없으면 -1
print("-"*30)

# 오른쪽에서 왼쪽으로 문자열 검색
p = st1.rfind("like")
print(p)
print(st1.rfind('like',0, p))

#index() : fint() 가능은 같지만 없으면 예외 발생
p = st1.index("like")
print(p)
# print(st1.index("love")) # 없으면 오류

# 시작하는 단어인지 검사
print(st1.startswith("likes"))
print(st1.startswith("likes", 3))

# 끝나는 단어인지 검사
print(st1.endswith("likes"))
print(st1.endswith("too"))
print(st1.endswith('likes',0,8))

