# 2차원 리스트 : [[],[],[]]
# [10, [3,6,9], 8, [4,7]] -> 1차원
name = ['이차원', '박수영', '최명길']
score = [[] for i in range(3)]
print(name)
print(score)

[
    [],
    [],
    []
]
score[0].append(96)
score[0].append(68)
score[0].append(87)

score[1].append(78)
score[1].append(68)
score[1].append(87)

score[2].append(96)
score[2].append(90)
score[2].append(87)

print(score)

total = [0,0,0]
for i in range(3) : 
    total[i] = sum(score[i])
    print(f'{name[i]} : 총점 = {total[i]}, 평균 = {total[i]/len(score[i]):.2f}')