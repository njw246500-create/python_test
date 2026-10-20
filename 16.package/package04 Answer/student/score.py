def average(*scores) : # 개수 상관없이 들어올 수 있음 *: 튜플로 들어옴, **: 딕셔너리로 들어옴
    return sum(scores) / len(scores) 

# *args => 튜플로 반환
# def average(*scores) : 
#    return sum(scores) / len(scores)

# {key:value, key:value}
# {kor : 90, eng : 89, ...}
# **kwargs => 딕셔너리로 반환
# def average(**scores) : 
#   total = 0
# for subject, score in scores.items() :  # 딕셔너리를 언팩킹 하는것
#   print(f"{subject} : {score}점)
#   total += score

# return total / len(scores)



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

'''