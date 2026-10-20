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

import student.score as g
h = g([100,100,100,90,80])

import student.grade as s
j = s([100,100,100,90,80])

print(h,j)

import student.info as i
i('홍길동',h,j)



