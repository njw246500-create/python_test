import calendar

# print(calendar.calendar(2027))

print(calendar.month(2026, 10))

# 윤년 확인 
year1 = int(input("년도 입력 : "))
if calendar.isleap(year1) : 
    print(year1, '년은 윤년')
else : 
    print(year1, '년은 평년')