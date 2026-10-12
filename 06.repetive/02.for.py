# 1 ~ 100 합계 구하시오
sum = 0 # 변수 초기화가 되어있어야한다. 
for i in range(1,101) : 
    sum += i 
print(sum)

# 1~100까지 5의 배수의 합을 구하시오

sum = 0 
for z in range(1,101) : 
    if(z % 5 == 0) :
        sum += z
print('1부터 100 까지 5의 배수의합은 :', sum)

sum = 0
for n in range(0,101,5):
    sum += n
print('1부터 100 까지 5의 배수의합은 :', sum)
