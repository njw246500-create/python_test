from person import Person

class Famer(Person) : 
    def __init__(self, name, age, vegetable):
        super().__init__(name, age, job='famer')
        self.__vegetable = vegetable

    def introduce(self) : 
        super().hello()
        print(f'나는 {self.__vegetable}을 키웁니다.')

    def hochul(self) : 
            print(f"추상클래스의 인스턴스 변수 : {self.__vegetable}, {self.__vegetable}, {self.__vegetable}")