kim = [100, 98, 68]
park = [89, 67, 99]
lee = []

hap = [0,0,0]

hap[0] = sum(kim)
hap[1] = sum(park)


a = int(input("lee 의 점수1을 입력하세요"))
lee.append(a)
b = int(input("lee 의 점수2을 입력하세요"))
lee.append(b)
c = int(input("lee 의 점수3을 입력하세요"))
lee.append(c)

hap[2] = sum(lee)
print('김수현의 총점 = ',hap[0], '평균 = %.2f' %(hap[0]/len(kim)))
print(f"박미자의 총점 = {hap[1]} 평균 = {hap[1]/len(park):.2f}")
print(f"이미자의 총점 = {hap[2]} 평균 = {hap[2]/len(lee):.2f}")
# 정답

# for x in range(3) : 
#     # num = int(input("숫자 : "))
#     lee.append(int(input("숫자 : ")))
# print(lee)
