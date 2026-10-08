

'''
논리연산자 : 수학의 boolean 대수 연산
<진리표>
x      y      x and y     x or y     not x      xor(서로다를때만 True)
T      T         T           T         F                

'''
num1 = 100
num2 = 200
x = 7
y = 3
f_result = num1 >= num2 # F 
t_result = x >= y # T 
print(f'f_result = {f_result}, t_result = {t_result}') 

and_result = f_result and t_result
or_result = f_result and t_result
print(f"f_result and t_result = {and_result}")
print(f"f_result or t_result = {or_result}")

print(f"f_result not = {not f_result}")

xor = f_result ^ t_result
xor2 = f_result ^ f_result
print(xor)
print(xor2)