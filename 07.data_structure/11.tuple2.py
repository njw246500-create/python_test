str_tup = ("국어", "python", 'ai', '수학', '영어')

print(str_tup[2])
print(str_tup[::2])
print(str_tup[-1])
print(str_tup[::-1])

print(str_tup.index("python")) # .index = 인덱스번호, 없으면 오류

tup1 = (1,2,3,4,5)
print("%d %d %d %d" %(tup1[0], tup1[4], tup1[2], tup1[1]))
print(f"{tup1[0]} {tup1[4]} {tup1[2]} {tup1[1]}")
print("{0}{3}{2}{1}".format(tup1[0], tup1[1], tup1[2], tup1[3]))
print("-" * 30)

# 언팩킹 : 튜플의 포장을 풀어서 안의 내용만 출력
# *변수명
print("{3} {0} {1}".format(*tup1)) # *tup1 언팩킹 해서 하나씩 넣은것, 앞에서 부터 3개
print("{} {} {}".format(*tup1[1:4])) 
print(*tup1[:3]) # 앞에서 부터 3개
print(tup1[:3]) # 튜플의 형태
print("-" * 10)

tup2 = (34.23423, 9.37463, 472.48276, 82.3825)
print("{:.2f} {:.2f} {:.2f} {:.2f}".format(*tup2)) # 각각의 소숫점을 적용하기에는 이게 더 편함. 
for i in range(len(tup2)) : 
    if (i < len(tup2)-1) : 
        print("{:.2f}".format(tup2[i]), end = ', ')
    else :
        print("{:.2f}".format(tup2[i]))

# join() : 여러개의 문자열을 하나로 합칠 때 사용하는 문자열 메서드(함수)
#           '구분자'.join(문자열이 담긴 리스트나 튜플)

words = ["Python", "is", "fun"]
# 공백을 기준으로 합치기
print(" ".join(words))

# 하이픈을 기준으로 합치기
print("-".join(words))

# for문을 한 줄로 축약
print(", ".join(f"{x:.2f}" for x in tup2))

tup3 = (10, 20, 30)
a, b, c = tup3
print(tup3)
print(a, b, c)

d, e = tup3[:2]
print(d, e)