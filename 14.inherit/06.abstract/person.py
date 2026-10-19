# 추상클래스로 만들것임.
from abc import ABC, abstractmethod

class Person(ABC) : 
    def __init__(self, name, age, job=None):
        self.name = name
        self.__age = age
        self.job = job

    def hello(self) :
        print(f"Hello, I'm {self.name}")
    
    def update_age(self, age) : 
        if age < 0 : 
            print('나이는 음수일 수 없습니다')
        else :
            self.__age = age
            print(f'현재 나이는 {self.__age}세') 
    
    def getAge(self) :
        return self.__age 

    @abstractmethod
    def introduce(self) : 
        pass # 보통 abstract는 pass 를 많이 써준다. 

    # 추상메서드는 자식클래스에서 오버라이딩 했는가만 검사. 구현해도 실행가능함.
    # @abstractmethod
    # def info(self) : 
    #     print('이 메서드는 자기소개 입니다.')

    # def info(self) : 
    #     print('programmer 정보입니다')


    # 추상클래스의 목적

    # 동물의 소리를 체크하기 위해 사운드를 만듬 
    # 고양이 - 야옹, 강아지 멍멍, 송아지 음메
    # 클래스에 따라 메소드의 이름은 다양하게 만들수있음
    # 여러 사람들이 메소드의 이름을 다 다르게 만듬
    # abstract를 만들어놓으면 메소드 이름을 확정지어서 통일시킬 수 있음.
    # 추상메소드를 상속받아 그대로 구현할 수 있는 장점이 있다. 보통 안에는 pass 만 넣어준다. 