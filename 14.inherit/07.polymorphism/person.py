# 추상클래스로 만들것임.
from abc import ABC, abstractmethod

class Person(ABC) : 
    def __init__(self, name, age, job=None):
        self.__name = name
        self.__age = age
        self.__job = job


    # getter 메소드 === 조회용
    def get_name(self) :
        return self.__name

    def get_age(self) : 
        return self.__age

    def get_job(self) :
        return self.__job

# setter 메소드 ---- 수정용
    def set_age(self, age) : 
        if age < 0 : 
            print("나이는 음수가 없습니다")
        else :
            self.__age = age
            print(f'[{self.__name}]의 나이가 {self.age}세로 업데이트 되었습니다.')

    def set_job(self, job) : 
        self.__job = job 

    def hello(self) : 
        print(f"안녕, 나는 {self.__name}이라고 해")

    @abstractmethod
    def introduce(self) : 
        pass