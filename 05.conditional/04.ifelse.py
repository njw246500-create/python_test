
jumsu = 330

# if jumsu >= 90 : # 90보다 큰 값은 모두 다 씀 
#     print("A학점")
# else :           # 90미만인 모든 값(67, 72, 80)
#     if jumsu >= 80 : # 90미만 and 80이상의 값
#         print("B학점")
#     else :       # 80 미만인 모든 값
#         if jumsu >= 70:  # 80미만이면서 70 이상인 값
#             print("C학점")
#         else :   # 70미만인 모든 값
#             if jumsu >= 60:   # 70미만이면서 60이상인 값
#                 print("D학점")
#             else : # 60미만의 값
#                 print("F학점")

# if jumsu >= 90 :
#     print("A학점")
# elif jumsu >= 80 :
#     print("B학점")
# elif jumsu >= 70 :
#     print("C학점")
# elif jumsu >= 60 : 
#     print("D학점")
# else : 
#     print("F학점")


# 연습하기 100점 초과이면 점수 없다고 나오게, 음수여도 마찬가지
if jumsu > 100 : 
    print("점수가 100을 넘어갔습니다")
elif jumsu >= 90 :
    print("A학점")
elif jumsu >= 80 :
    print("B학점")
elif jumsu >= 70 :
    print("C학점")
elif jumsu >= 60 : 
    print("D학점")
elif jumsu >= 0 :
    print("F학점")
else :
    print("점수가 0보다 작습니다.")