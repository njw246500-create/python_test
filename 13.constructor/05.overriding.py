class Car : 
    def __init__(self, speed=0, color='black', model='E-class') : # 지역변수에 기본값을 넣어준 것.
        self.speed = speed
        self.color = color
        self.model = model

    def output(self) : 
        print('모델 :', self.model)
        print('색상 :', self.color)
        print('속도 :', self.speed)

    def __str__(self):
        result = f'속도 : {str(self.speed)}, 색상 : {str(self.color)}, 모델 : {str(self.model)}'
        return result

myCar = Car()
myCar.output()
print("-"*30)
print(myCar) # 원래는 주소가 호출이됨. 
print(myCar.__str__())