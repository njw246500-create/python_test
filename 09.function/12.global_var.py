def fun1() : 
    a = 10 #지역변수 : 함수안에서 사용가능
    print('fun1()의 a = ', a)
    print('fun1()에서 전역변수 a = ', globals()['a']) # globals()['a'] a 라는 키 값을 가지고 오시오! 

# print(a) error

def fun2() : 
    print('fun2()의 a = ', a)

a = 20 # 전역변수 

fun1()
fun2()

def fun3() :
    global b
    b = 10
    print('fun3()의 b = ', b)

def fun4() : 
    print('fun4()의 b = ', b)

fun3()
fun4()

def calc_area(radius) : 
    global area
    area = 3.14*radius**2
    return area

print(calc_area(5))
print(area  )
