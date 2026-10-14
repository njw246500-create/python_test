# 디폴트 매개변수

def greet(name, msg='안녕') : 
    print(name, msg)

greet('더조은', '좋은하루')
greet('더조은')

def greet2(name,age, class1='704', aa = 'OOOO') :
    print(name,age,class1,aa)

greet2('파이썬', '34')
greet2('파이썬', '24', '603')
greet2('파이썬', '24', '603', '하하하')

# 가변객체 사용 불가 -> 가변객체의 경우 None을 사용해야한다. 
# def welcome(city, name = 'Guest', room = []) : 
#     room.append(101)
#     print(f"Hello {name}, This is {city}. You can use {room}")

# welcome('Seoul')
# welcome('Seoul', '더조은', '1001')

def welcome2(city, name = 'Guest', room = None) : 
    if room == None : 
        room = '1001'
    print(f"Hello {name}, This is {city}. You can use {room}")

welcome2('Seoul')
welcome2('Seoul', '더조은', '1002')
