'''
편의점에서 주말 (토요일, 일요일) 알바의 근무시간을 저장한 튜플
 토요일 오전, 토요일 오후, 일요일 오전, 일요일 오후 근무시간

 work_hours = (4,5,3,4)
 문1. 주말 동안 일한 총 근무시간의 합 구하기
 문2. 일요일 근무 시간만 따로 뗴어내어 sun_hours 라는 새로운 튜플을 만들어 출력
 문3. 토요일 오전 근무 시간이 4시간에서 5시간으로 변경


'''

##문1##

work_hours = (4,5,3,4)

print(" 주말동안 일한 총 시간 : ", sum(work_hours))

##문2##
sun_hours = (work_hours[2], work_hours[3])
print(sun_hours)

## 문3 ## 

work_hours_change = (5,*work_hours[1:] ) # 언팩킹 해서 대입하기.
print(work_hours_change)


## 정답
# 문1
total_hours = sum(work_hours)
print("총 근무시간 :", total_hours)

# 문2
sun_hours = work_hours[2:]
print('일요일 근무시간 :', sun_hours)

# 문3
# 튜플은 수정 불가. 새로운 튜플을 만들면 된다. 
updated_hours = (5,) + work_hours[1:]
print(updated_hours)
