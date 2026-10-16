# 생성자 : 객체생성시 호출
# 변수를 초기화할때 사용

class Car : 
    def __init__(self, model, color, speed):
        print('생성자 호출')
        self.model = model
        self.color = color
        self.speed = speed


    def output(self) : 
        print('모델 : ', self.model)
        print('색상 : ', self.color)
        print('속도 : ', self.speed)

myCar1 = Car('sm7','red',20)
myCar1.output()
print('-'*30)

myCar2 = Car("e-class",'yellow',50 )
myCar2.output()
print('-'*30)

myCar2.__init__('h-class','white', 150)
myCar2.output()