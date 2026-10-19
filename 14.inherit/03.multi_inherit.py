class A : 
    def method(self) : 
        print(" A method")

class B(A) :
    def method(self) : 
        print('B method')

class C(A) :
    def method(self) : 
        print("C method")

class D(B, C) :  # 다중상속
    pass 

d = D()
d.method() # pass 이면 나를 상속받은 곳으로 다시 돌아감, B로 돌아가서 실행! 
# MRO(Method Resolution Order) 규칙 : 다중 상속시 메서드를 찾는 순서

print(D.mro())


