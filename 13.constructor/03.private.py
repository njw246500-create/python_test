# private : 외부에서 접근 못하게 막음
class Car : 
    def __init__(self, speed=0, color='blue', model='k7', maker='kia') :
        self.speed = speed
        self.color = color
        self.model = model
        self.__maker = maker # maker의 변수를 private으로 만들기 -> 외부에서 접근하지 못함. 
        
    def output(self) : 
        print('속도:', self.speed)
        print('색상:', self.color)
        print('모델:', self.model)
        print('회사:', self.__maker)

    def getMaker(self): # getMaker > 변수이름 앞에 get 붙이면 private 값 접근가능함. 
        return self.__maker

    def setMaker(self, maker) : 
        self.__maker = maker 


myCar = Car()
myCar.output()

print(myCar.speed)
print(myCar.model)
print(myCar.getMaker()) # print(myCar.__maker)은 불가능
print("-"*30)

myCar.speed = 50
myCar.__maker = 'samsung' # 오류는 나지 않지만 접근이 불가능하므로 값이 바뀌지는 않다. 
myCar.output()

