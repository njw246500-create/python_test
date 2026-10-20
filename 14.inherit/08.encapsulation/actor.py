from person import Person

class Actor(Person) : 
    def __init__(self, name, age, film):
        super().__init__(name, age, job='actor')
        self.__film = film

    def get_film(self) : 
        return self.__film # private 으로 선언되어있으니까 보려고 바꾼것,

    def introduce(self):
        super().hello()
        print(f"나의 대표작은 {self.__film}입니다")
        print(f'나의 이름은 {self.get_name()}이고, 나이는 {self.get_age()}세 입니다.')