class Calc1 :
    def data (self, x) :
        a = int(input(f"안녕하세요. {x}님, 먼저 파이썬 점수를 입력해주세요."))
        b = int(input(f"{x}님, Ai 점수를 입력해주세요."))
        return a,b
    
    def show (self, x, a, b) : 
        print(f" 이름 : {x} \n 파이썬 : {a} \n AI : {b} \n 합계 : {a+b} \n 평균 : {0.5*(a+b)} ")

    def all (self,x,a,b,y,c,d) :
        print("-"*50)
        print(f" 이름 : {x} \n 파이썬 : {a} \n AI : {b} \n 합계 : {a+b} \n 평균 : {0.5*(a+b)} ")
        print("="*50)
        print(f" 이름 : {y} \n 파이썬 : {c} \n AI : {d} \n 합계 : {c+d} \n 평균 : {0.5*(c+d)} ")