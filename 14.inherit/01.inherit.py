## 상속
# 자식은 여러개 쓸수있지만, 부모는 원래 자식재산이었던것을 쓸 수 없음..

class CalcParent : 
    def plus(self,x,y) : # self도 변수임. 객체가 들어가는것임
        print("부모클래스의 plus()")
        return x+y

    def minus(self,x,y):
        print("부모클래스의 minus()")
        return x-y

class CalcChild(CalcParent) : # CalcParent를 상속받음
    def multi(self,x,y) : 
        print("자식클래스의 multi()")
        return x*y

    def plus(self, x, y) :
        # super().plus(x,y)
        print('부모의 plus',super().plus(x,y))
        print("자식 클래스의 plus()")
        return (x+y)**2

cal1 = CalcChild()
print(cal1.minus(5,3))
print(cal1.plus(3,2)) #내꺼먼저 호출, 내꺼가 우선순위가 더 높음 부모꺼는 우선순위 낮음. 부모꺼 갖고오고 싶으면 super 

cal2 = CalcParent()
print(cal2.plus(3,5))
# print(cal2.multi(2,3)) error

