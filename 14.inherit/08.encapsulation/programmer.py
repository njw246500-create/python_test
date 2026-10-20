from person import Person

class Programmer(Person) : 
    def __init__(self, name, age, language) :
        super().__init__(name, age, job='programmer')
        self.__language = language

    def get_language(self) : 
        return self.__language

    def introduce(self):
        super().hello()
        # 출력 : 이름, 나이를 출력
        print(f"나는 {self.__language}언어를 사용할 줄 압니다")
        print(f'나의 이름은 {self.get_name()}이고, 나이는 {self.get_age()}세 입니다.')