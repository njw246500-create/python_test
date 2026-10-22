from employee import Employee

class FullTimeEmployee(Employee) : 
    def __init__(self,name,emp_id, monthly_salary) : 
        super().__init__(name, emp_id)
        self.__monthly_salary = monthly_salary

    def show_info(self) :
            print(f"직원 이름 : {self.get_name}, 직원 사번 : {self.__monthly_salary}")
    # self.get_name 한 이유 : employ의 클래스 선언후 private 을 만들었었기 때문에 그럼,
