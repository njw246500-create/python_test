

# 20세 이상이면 성년
# 15세에서 19세 청소년
# 15세 미만은 어린이

age = int(input("나이 입력 : "))
if age > 19 :
    print("성년입니다.")
elif age > 15 : 
    print("청소년입니다")
else : 
    print("어린이 입니다")

###
###

if age <= 19 : 
    if age >= 15 : 
        print("청소년 입니다")
    else : 
        print("어린이 입니다")

else : print("성년 입니다")