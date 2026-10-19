from person import Person

class Programmer(Person) : 
    def __init__(self, name, age, language) :
        super().__init__(name, age, job='programmer')
        self.__language = language

    def introduce(self):
        super().hello()
        # 출력 : 이름, 나이를 출력
        print(f"나는 {self.__language}언어를 사용할 줄 압니다")

    def hochul(self) : 
        print(f"추상클래스의 인스턴스 변수 : {self.__language}, {self.__language}")