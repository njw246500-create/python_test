class Calculator : 
    def plus(self, x, y) : 
        return x+y

    def minus(self, x, y) : 
        return x-y
    
    def multi(self, x, y) : 
        return x*y
    
    def divide(self, x, y) : 
        return x/y

if __name__ == '__main__' : # 운영체제 스레드, 인터넷을 하며 노래를 들음 -> 스레드 두개 멀티스레드
    cal = Calculator()
    print(cal.plus(3,5))















