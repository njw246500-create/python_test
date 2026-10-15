students = [[],[],[]]
with open('11.file/test.csv','r') as f:
    a = [line.strip().split('.') for line in f.read().splitlines()]
    
print(f"이름 : {a[0][0]}, 국어 : {a[1][0]}, 영어 : , 수학 : , 컴퓨터 :  , 총점 : , 평균 :  ")
students2 = [[],[],[]]
with open('11.file/test.csv','r') as f:
    lines = f.read().splitlines()
    # lines = f.readlines()
    print(lines)

    for line in lines :
    #     line = line.strip()
    #     print(line)
    #     line = line.split(',')
    #     print(line)
    #     students.append(line)

    # 3줄을 한줄로
        students2.append(line.strip().split(','))

print(students2)


with open('11.file/test.csv','r') as f:
    students3 = [line.strip().split(',')  for line in f.read().splitlines()]
print(students3)

result = ''
for student in students3 : 
    name, kor, eng, math = student # unpacking
    total =int(kor) + int(eng) + int(math)
    avg = total / 3

    result += f"이름 : {name}, 국어 : {kor}, 영어 : {eng}, 수학 : {math}, 총점 : {total}, 평균 : {avg:.1f}\n"

print(result)

with open('11.file/result.txt','w') as f :
    f.write(result)

# 이름 : 더조은, 국어: 90, 영어 : 80, 수학 : 80, 컴퓨터 : 78 총점 : 358 평균 : 87.2
# for문으로 돌면서 unpacking