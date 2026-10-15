# 가변 위치 인자 : 매개변수가 갯수가 정해져 있지 않을 때 사용
# *args : 튜플이 전달되고 저장됨 - 대체적으로 args, kwargs 라는 형태의 이름을 씀, 이름은 바뀌어도 상관없다

def total(*args) : 
    print(type(args))
    sum = 0
    for x in args : 
        sum += x 
    return sum 

print(total(1,3))
print(total(3,8,56,68,89))
print(total())
print('-'*30)

# 매개변수가 여러개 일때
def add_mul(op, *args) : 
    if op == 'add' : 
        result = 0
        for i in args : 
            result += i
    elif op == 'mul' : 
        result = 1
        for i in args : 
            result *= i
    return result

print(add_mul('add',1,2,3,4,5))
print(add_mul('mul',3,6))

def calc_sum(name, *args, academy) : 
    print(f'Name : {name}, Academy : {academy}')
    sum = 0
    for x in args : 
        sum += x 
    return sum

print('합계 : ', calc_sum('최상급', 1,2,3,4,5, academy = '더조은'))