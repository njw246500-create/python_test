'''
* 파일명은 소문자로 시작, 클래스명은 대문자로 시작

* 클래스 선언
    class 클래스명 : 
        pass -> 빈 상태로 만들때 사용(임시 점유용 키워드)
        메서드 생성 -> 그렇지 않으면 메서드를 생성하면 됨

* 매개변수 self 
    자기자신의 객체를 의미 
    클래스 안에서 함수를 호출할 때 

    이름이 반드시 self 가 아니어도 됨. 
    그러나 보통 self를 씀 
'''

class Car : 
    def set1(self) : 
        self.model = 'sm7'
        self.color = 'blue'
        self.speed = 10

    def speedUp(self) :
        self.speed = 20

    def output(self) :
        print('모델 : ', self.model)
        print('색상 : ', self.color)
        print('속도 : ', self.speed)

myCar = Car() # 객체 생성후 이용! 그러면 Car()함수를 모두 이용할 수 있음. 
myCar.set1() # 주석처리할 경우 오류남, set1으로 변수를 만든 후 output을 해야하므 호출할 때 변수가 생성되면서 초기화가 됨. 
myCar.output()
print('-'*30)

myCar.speedUp()
myCar.output()

print(myCar.model)
print(myCar.color)
print(myCar.speed) 

## 객체지향언어 # 
