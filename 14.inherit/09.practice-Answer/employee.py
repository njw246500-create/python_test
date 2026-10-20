'''
- Employee(추상클래스) 
    생성자에서 name, emp_id를 초기화한다. 
    show_info()는 직원의 이름과 사번을 출력한다.
    calculate_salary()는 추상메서드이다. 

- FullTimeEmployee -> Employee 상속받음
    월급(monthly_salary)을 입력받음

- PartTimeEmployee -> Employee 상속받음
    시급(hourly_wage)과 근무시간(hours)을 입력받음

- main 
    직원들을 리스트에 저장하고 반복문으로 급여를 출력한다. 

'''

from abc import ABC, abstractmethod

class Employee(ABC) : 
    def __init__(self, name, emp_id) : 
        self.name = name 
        self.emp_id = emp_id

    def show_info(self) : 
        print(f"이름 : {self.name}, 사번 : {self.emp_id}")

    @abstractmethod
    def calculate_salary(self) : 
        pass

class FullTimeEmployee(Employee) : 
    def __init__(self, name, emp_id, monthly_salary) :
        super().__init__(name,emp_id) 
        self.monthly_salary = monthly_salary

    def calculate_salary(self) :
        return self.monthly_salary

class PartTimeEmployee(Employee) : 
    def __init__(self, name, emp_id, hourly_wage, hours):
        super().__init__(name, emp_id)
        self.hourly_wage = hourly_wage
        self.hours = hours

    def calculate_salary(self) :
        return self.hourly_wage * self.hours

from employee import FullTimeEmployee, PartTimeEmployee
emps = [
    FullTimeEmployee('더조은', 'tj001', 4000000),
    PartTimeEmployee('황현희', 'tj002', 11000,80),
    FullTimeEmployee('이만수', 'tj003', 3500000)
]

for emp in emps :
    emp.show_info()
    print(f"급여 : {emp.calculate_salary()}원")
    print()