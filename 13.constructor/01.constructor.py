# 생성자 : 객체생성시 호출
# 변수를 초기화할때 사용

class Car : 
    def __init__(self, model, color, speed): # car 객체 생성하면서 동시에 호출되는 함수, model, cololr, speed 라는 인스턴스 변수가 자동으로 생성된다. 
        print('생성자 호출')
        self.model = model # 지역변수에 있는것을 인스턴스 변수로 대입 
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