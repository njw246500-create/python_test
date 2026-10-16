import json

def enco(file_path) : 
    encodings = ['UTF-8', 'EUC-KR', 'CP949']

    for enc in encodings : 
        try : 
            with open(file_path, 'r', encoding = enc) as f :
                return enc

        except UnicodeDecodeError:
            continue

# data.json 한개의 {} 만 있을때 
files = '11.file/data/data.json'
with open(files,'r', encoding = enco(files)) as f : 
    data = json.load(f)

print(data)
print(type(data))

print(f"이름 : {data['name']}")
print(f"보유기술 : {data['skills']}")
print(f"보유기술 : {data['skills'][0]}")
print('-'*50)

# data2.json 여러개의 {}가 있을때
students = []
add_string = ''
files = '11.file/data/data2.json'
with open(files, 'r', encoding = enco(files)) as f :
    for line in f : 
        line = line.strip()
        add_string += line

        if line == '}' : 
            student_dic = json.loads(add_string)
            students.append(student_dic)

            add_string = ''

print('============ [변환된 students 리스트] ==============')
print(students)
print('============ [한명씩 출력] ==============')
for std in students : 
    print(f'이름 : {std['name']} | 나이 : {std['age']}세 | 보유기술 : {std['skills']}')
    print(f'이름 : {std['name']} | 나이 : {std['age']}세 | 보유기술 : {', '.join(std['skills'])}')


# data3.json 여러개의 {}가 줄바꿈이 있을 때

students = [] # 빈 리스트
add_string = '' 
files = '11.file/data/data2.json' # data2.json 이라는 프로그램의 경로로 파일을 받기
with open(files, 'r', encoding=enco(files)) as f :  # with 안에서만 실행됨, 파일 불러와서 읽기, enco로 encoding 해서 f 로 해석
    for line in f : # 파일에서 각각의 line 
        if not line : # 바닥(빈 행)
            continue
        
        line = line.strip() # 각 줄을 벗겨내서 line 이라는 변수에 대입하기 
        # print('line 은',line)
        # print("-"*30)
        add_string += line # 라인이라는 변수에 줄바꿈없이 string 문자를 추가하기
        # print('add_string은',add_string)

        if line == '}' : 
            student_dic = json.loads(add_string)
            students.append(student_dic)

            add_string = ''
            # print("-"*30)
            # print(student_dic)

print('================ [변환된 students 리스트] ===============')