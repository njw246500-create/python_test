'''
* 클래스 변수 : 모든 객체가 변수를 공유
    - class 바로 밑에서 선언
    - 사용법 : 클래스이름.변수명
* 인스턴스 변수 : 자기자신의 객체에서만 사용
    - 함수안에서 선언 : self.변수명
    - 사용법 : 객체명.변수명

'''

class Car : 
    maker = '삼성르노'
    def set1(self) : 
        self.model = 'sm5'
        self.color = 'black'
        self.speed = 10

    def speedUp(self) : 
        self.speed += 10

    def speedDown(self) :
        self.speed -= 10


    def output(self):
        print('모델 :', self.model)
        print('색상 :', self.color)
        print('속도 :', self.speed)

print('제조사 :', Car.maker)

myCar1 = Car()
myCar1.set1()
myCar1.output()
print('-'*30)

myCar2 = Car()
myCar2.set1()
myCar2.speedUp()
myCar2.output()
print("-"*30)
myCar1.output()
print("="*30)

myCar1.speedDown()
myCar2.speedUp()
print("---- myCar1 ----")
myCar1.output()
print("---- myCar2 ----")
myCar2.output()

print("제조사 : ", Car.maker)
print(myCar1.maker)
print(myCar2.maker)

Car.maker = '기아'
print("제조사 : ", Car.maker)
print(myCar1.maker)
print(myCar2.maker)

