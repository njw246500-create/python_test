# private : 외부에서 접근 못하게 막음
class Car : 
    def __init__(self, speed=0, color='blue', model='k7', maker='kia') :
        self.speed = speed
        self.color = color
        self.model = model
        self.__maker = maker
        
    def output(self) : 
        print('속도:', self.speed)
        print('색상:', self.color)
        print('모델:', self.model)
        print('회사:', self.__maker)

    def getMaker(self):
        return self.__maker

    def setMaker(self, maker) : 
        self.__maker = maker 


myCar = Car()
myCar.output()

print(myCar.speed)
print(myCar.model)
print(myCar.getMaker())
print("-"*30)

myCar.speed = 50
myCar.__maker = 'samsung'
myCar.output()

