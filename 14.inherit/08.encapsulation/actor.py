from person import Person

class Actor(Person) : 
    def __init__(self, name, age, film):
        super().__init__(name, age, job='actor')
        self.__film = film

    def introduce(self):
        super().hello()
        print(f"나의 대표작은 {self.__film}입니다")

    def hochul(self) : 
            print(f"추상클래스의 인스턴스 변수 : {self.__film}, {self.__film}, {self.__film}")

            # superinit 했는데 왜 안나와......