from employee import Employee 

class PartTimeEmployee(Employee) :
    def __init__(self,name,emp_id, hourly_wage, hours) : 
        super().__init__(name, emp_id)
        self.__hourly_wage = hourly_wage
        self.__hours = hours

    def show_info(self) :
            print(f"직원 이름 : {self.__hourly_wage}, 직원 사번 : {self.__hours}")
    