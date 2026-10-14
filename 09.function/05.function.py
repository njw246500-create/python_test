# return에 값이 2개 이상이면 자동으로 튜플로 만듬
def tm() : 
    sum = 5 + 10
    mul = 5*10
    return sum, mul

result = tm()
print(result, type(result))


print('합 = ', result[0])
print('곱 = ', result[1])

total, multi = tm()

print('합 = ', total)
print('곱 = ', multi)