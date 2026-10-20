'''
문)
package04
    main.py
    student(package)
        __init__.py
        score.py
        grade.py

- score.py
    여러 과목(몇개가 들어올지 모름)을 입력받아 점수의 평균을 구하는 함수 정의

- grade.py
    학점 계산

- __init__.py
    출력문 1개(처음 호출되었을 대 출력문)
    2개의 파일 import 

- info.py
    이름, 평균점수, 학점 출력



'''

import student

name = '김수완'
# *args 일때 
avg = student.average(90,89,29,98)

# **kwagrs avg = student.average(kor = 90, eng = 89,math = 29, com = 98)

grade = student.get_grade(avg)

