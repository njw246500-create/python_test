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

    # 호출하는것은 똑같지만 반응은 다르다 -> 다형성