from person import Person

class Famer(Person) : 
    def __init__(self, name, age, vegetable):
        super().__init__(name, age, job='famer')
        self.__vegetable = vegetable

    def get_vegetable(self) : # 부모클래스에서 private이 되어있는 상태니까 이거 해야지! 
        return self.__vegetable

    def introduce(self) : 
        super().hello()
        print(f'나는 {self.__vegetable}을 키웁니다.')
        print(f'나의 이름은 {self.get_name()}이고, 나이는 {self.get_age()}세 입니다.')

