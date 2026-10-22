from abc import ABC, abstractmethod

class Employee :
    def __init__(self,name,emp_id):
        self.__name = name
        self.__emp_id = emp_id

    def get_emp_id(self) : 
        return self.get_emp_id
    def show_info(self) :
        print(f"직원 이름 : {self.__name}, 직원 사번 : {self.__emp_id}")

    @abstractmethod # 추상메서드 -> 객체 안만들고도 사용가능한 메서드

    def calculate_salary(ABC) : 
        pass 