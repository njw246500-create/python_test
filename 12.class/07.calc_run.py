from calc1 import Calc1 as c
c1 = c()
x = input("이름을 입력해주세요")
a,b = c1.data(x)
c1.show(x, a, b)

y = input("두번째분 이름을 입력해주세요")
d,e = c1.data(y)
c1.show(y,d,e)

c1.all(x,a,b,y,d,e)