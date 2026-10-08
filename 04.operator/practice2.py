'''
문
파운드(lb)와 킬로그램(kg)을 상호 변환하는 프로그램 만들기

kg = pound * 0.453592
pound = kg * 2.204623

'''

a = int(input('파운드 입력하세요'))
kg_a = a * 0.453592
print("%.2flb 파운드는 킬로그램으로 환산하면 %.2fkg 입니다." %(a, kg_a))

b = int(input('킬로그램 입력하세요'))
pound_b = b*2.204623
print("%.2fkg 킬로그램은 파운드로 환산하면 %.2flb 입니다." %(b, pound_b))