# 변수 : 어떤 자료형이든 상관없이 넣을 수 있다
var1 = 'Hello Python'
print(var1)
print(id(var1)) # 주소를 출력하는 함수

var1 = 100
print(var1)
print(id(var1))
print('-'*30)
#변수명은 예약어를 쓸 수 없다.
# 뱐수가 무엇을 가리키는지 알 수 있는 이름으로 작명

# python의 자료의 크기는 상관없다.
num1 = 100
num2 = 595436846873584354
num3 = 39.45343824384384
print(num1)
print(num2)
print(num3)
print('num1 type =', type(num1))
print(f'num2 type = {type(num2)}')
print(f'num3 type = {type(num3)}')
print('-'*30)

a = '박수영 이무기'
b = 'Hello world!!!'
c = True
print(a)
print(b)
print(c)
print(f'a type = {type(a)}')
print(f'b type = {type(b)}')
print(f'c type = {type(c)}')

d = 7 
e = 9
f = 5

# int d = 1, e = 5, f = 6 -> unpacking
g, h, i  = 1, 2, 3
print(g, h, i)

j, k, m = '문자', False, 3.14
print(j, k, m)

