
# 문1 : 삼각형의 넓이 구하는 파일(class) 생성
#        실행하는 파일을 만들어 import 하여 실행

# 문2 : 별도의 클래스에 메소드 2개 만들기
'''
    메소드 1 : 이름, 파이썬 점수, Ai 점수를 2명 사용자로부터 입력받기
    메소드 2 : 출력문 
            출력문 ex)
            이름 : 김수영
            파이썬 : 98
            AI : 79
            합계 : 177
            평균 : 87.7
    실행파일 : 2명으로 부터 입력받아 2명 출력하기


'''

class Triangle :
    def getArea(self, b, h) :
        self.b1 = b
        self.h1 = h
        return self.b1 * self.h1 /2

        
class Score : 
    def set(self) :
        self.name = input("이름 : ")
        self.python = int(input("파이썬 점수 입력 : "))
        self.ai = int(input("인공지능 점수 입력 : "))
        self.sum = self.python + self.ai
        self.avg = self.sum / 2
    
    def output(self) : 
        print('이름 : ', self.name)
        print('파이썬 점수 : ', self.python)
        print('인공지능 점수 : ', self.ai)
        print('합계 : ', self.sum)
        print('평균 : ', self.avg)



'''
# 문1 # 
from triscore import Triangle as t
b = int(input("밑변 : "))
h = int(input("높이 : "))

area = t()
print(area.getArea(b, h))


# 문2 #
from triscore import Score as sc
sc1 = sc()
sc2 = sc()

sc1.set()
sc2.set()

sc1.output()
print()
sc2.output()



'''