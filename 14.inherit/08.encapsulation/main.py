'''
문 : 
1. 각 클래스의 모든 인스턴스 변수는 private 으로 변경
2. 추상클래스를 제외한 모든 클래스에서 
추상클래스의 인스턴스 변수를 호출하여 출력하는 메소드 정의
추상클래스 말고 다른 클래스에다가 하나씩 해보고 복붙!! programmer famer actor 

3. main에서 출력

# private 한 상태에서는 get 메서드를 써서 호출하기 ex) self.get_name()
'''


from programmer import Programmer
from famer import Famer
from actor import Actor 


# people = Programmer('김수철', 31, 'python')
# people.introduce() # 여기 오류남 ,, 왜지
# print("-"*30)

# people = Actor('박인술', 29, '왕과사는남자')
# people.introduce()
# print("-"*30)


# people = Famer('박광덕', 24, '오이')
# people.introduce()
# print("-"*30)

people = [
    Programmer('김수철', 31, 'python'),
    Actor('박인술', 29, '왕과사는남자'), 
    Famer('박광덕', 24, '오이')
    ]

print('================ 자기소개 하기(다형성 활용) =================\n')

for person in people : 
    person.introduce()
    print("-"*30)


