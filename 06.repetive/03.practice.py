'''
문 : 1~100 까지의 합계를 구하기

    조건 : 사용자가 넣은 숫자의 배수만 합계를 구하고, 갯수는 몇개인지 출력하기

    ex ) 사용자가 넣은 값 : 7
    7, 14, 21, 28 ...



'''

a = int(input("숫자를 입력하세요"))
sum = 0
for i in range(0,100,a) : 
    sum += i 

print(f"숫자 배수의 총합은 {sum}이고, 갯수는 {int(100/a)}개 입니다.")

# 정답
start = int(input("합계를 구할 시작값 입력 : "))
end = int(input("합계를 구할 끝나는 값 입력 : "))

num = int(input("배수 입력 : "))
sum = 0
count = 0
for i in range(start,end+1) : 
    if i % num == 0 : 
        sum += i
        count += 1

print(f'1~100까지 {num}의 배수의 합계는 {sum}, 갯수는 {count} ')

