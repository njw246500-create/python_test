'''
2차원 리스트로 
과정     파이썬   AI   빅데이터   디자인   합계   평균
홍길동
아무개
이순신
----------------------------------------------------
합계
평균

'''
#초기데이터 설졍 
# students = [
#     ['이름', 67, 78, 68, 67]
# ]

# subject1 = input("과목1명을 입력하세요")
# subject2 = input("과목2명을 입력하세요")
# subject3 = input("과목3명을 입력하세요")
# subject4 = input("과목4명을 입력하세요")

# subjectlist = []
# for i in range (3) : 
#     b = []
#     subjectlist.append(b)

# for i in range(3) : 
#     name = input(f"사용자{i+1}의 이름을 입력해주세요")
#     subjectlist[i].append(name)

# for j in range(3) : 
#     print(f"{subjectlist[j][0]}의 점수 입력")
#     for i in range(5) :
#         a = int(input(f"과목{i+1}의 점수를 입력해주세요"))
#         subjectlist[j].append(a)

# a1 = subjectlist[0][1]
# a2 = subjectlist[1][1]
# a3 = subjectlist[2][1]
# b1 = subjectlist[0][2]
# b2 = subjectlist[1][2]
# b3 = subjectlist[2][2]
# c1 = subjectlist[0][3]
# c2 = subjectlist[1][3]
# c3 = subjectlist[2][3]
# d1 = subjectlist[0][4]
# d2 = subjectlist[1][4]
# d3 = subjectlist[2][4]

# a = a1 + a2 + a3
# b = b1 + b2 + b3
# c = c1 + c2 + c3
# d = d1 + d2 + 3

# print(f"과정 {subject1} {subject2} {subject3} {subject4} 합계 평균")
# print(subjectlist[0][0], subjectlist[0][1], subjectlist[0][2], subjectlist[0][3], subjectlist[0][4], sum(subjectlist[0][1:4]), sum(subjectlist[0][1:4])/len(subjectlist) ,sep = ' ' )
# print(subjectlist[1][0], subjectlist[1][1],subjectlist[1][2],subjectlist[1][3],subjectlist[1][4], sum(subjectlist[1][1:4]),sum(subjectlist[1][1:4])/len(subjectlist), sep = ' ' )
# print(subjectlist[2][0],subjectlist[2][1],subjectlist[2][2],subjectlist[2][3],subjectlist[2][4], sum(subjectlist[2][1:4]),sum(subjectlist[2][1:4])/len(subjectlist), sep = ' ' )
# print("-"*50)
# print(f"합계  {a} {b} {c} {d}")
# print(f"평균  {a/4} {b/4} {c/4} {d/4}")


# ## 정답

students = [
    ['홍길동', 67, 87, 68, 67],
    ['아무개', 98, 78, 84, 67],
    ['이순신', 47, 80, 68, 98]

]
'''
sub_sum = [0,0,0,0]

print("과정\t파이썬\tAI\t빅데이터\t디자인\t합계\t평균")
for row in students : 
    name = row[0]
    scores = row[1:]

    for i in range(4) :
        sub_sum[i] += scores[i]

    s_sum = sum(scores)
    s_avg = s_sum / len(scores)

    # 학생별 합계
    print(f"{name}\t{scores[0]}\t{scores[1]}\t{scores[2]}\t{scores[3]}\t{s_sum}\t{s_avg}")
print("-" * 50)

sub_avg = [total / len(students) for total in sub_sum]
print(f"합계\t{sub_sum[0]}\t{sub_sum[1]}\t{sub_sum[2]}\t{sub_sum[3]}")
print(f"합계\t", end = "")
for total in sub_sum : 
    print(total, end = '\t')
print(f"평균\t{sub_avg[0]:.1f}\t{sub_avg[1]:.1f}\t{sub_avg[2]:.1f}\t{sub_avg[3]:.1f}")
print(f"평균\t", end = '')
for avg in sub_avg : 
    print(f'{avg:.1f}', end = '\t')
'''

name = ['홍길동', '이순신', '아무개']
subjects = ['파이썬','AI','빅데이터','디자인']
scores = [[79,75,90,86],[100,65,97,76],[99,75,70,88]]

print("과정\t파이썬\tAI\t빅데이터\t디자인\t합계\t평균")

for i in range(3) : 
    total = sum(scores[i])
    avg = total / len(subjects)

    print(f"{name[i]}\t{scores[i][0]}\t{scores[i][1]}\t{scores[i][2]}\t{scores[i][3]}\t{total}\t{avg:.1f}")

# 과목별 

for j in range(4) : 
    total = 0
    for i in range(3) : 
        # 이렇게 한번 써보기!!@ scores[0][0] + scores[1][0] + scores[2][0]
        total += scores[i][j]
    print(f"{total/3:.1f}", end = '\t')
print()

