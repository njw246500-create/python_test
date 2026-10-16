class Car : 
    def __init__(self, speed=0, color='black', model='E-class') : 
        self.speed = speed
        self.color = color
        self.model = model

    def output(self) : 
        print('모델 :', self.model)
        print('색상 :', self.color)
        print('속도 :', self.speed)

myCar = Car()
myCar.output()
print("-"*30)

myCar1 = Car(40)
myCar1.output()
print("-"*30)

myCar2 = Car(model='F-class')
myCar2.output()
print("-"*30)

myCar3 = Car(10, 'white', 'k9')
myCar3.output()
print("-"*30)

myCar3.__init__(50, 'yellow', 'k5')
myCar3.output()
print("-"*30)
