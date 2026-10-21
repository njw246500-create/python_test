# 클래스(static) 메소드
# 공동으로 사용

'''
*self를 안 쓸때
    - 정적메서드로 사용시 

    class Car : 
        @staticmethod
        def 정의 

    - 호출시
    클래스이름.메서드이름
    객체생성이름.메서드이름

'''
class Calc :
    @staticmethod 
    def plus1(self, x, y):
        print('static 메서드 호출')
        return x+y

    def plus(self, x, y) : # 인스턴스변수에는 self 가 들어감 ,나 자신의 객체가먼저 들어감. 
        print('인스턴스 메서드 plus() 호출')
        return x+y

    def minus(self,x,y) : 
        return x-y

    def result(self,x,y) :
        result1 = Calc.plus1(x,y)
        result2 = self.plus(x,y)
        return result1 + result2

print(Calc.plus1(100, 50, 30)) # 객체 생성없이 선언가능! annotation 있는경우! # 정적 메서드에서는 self, x, y 3개 받음 

# cal1 = Calc()
# print(cal1.plus(1,2))
# print(cal1.plus1(5,5))
# print('-'*30)

# @staticmethod를 안 넣었을 때 
# cal2 = Calc()
# print(cal2.plus1(100,50))
# 오류남 : 첫번째 매개변수가 객체를 받는 self로 들어감