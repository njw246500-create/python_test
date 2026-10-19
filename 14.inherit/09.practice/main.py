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
from employee import Employee
from fulltimeemployee import FullTimeEmployee
from parttimeemployee import PartTimeEmployee 

people = [
    PartTimeEmployee('김수철', 1234, 10, 10),
    PartTimeEmployee('박인술', 5678, 10, 10), 
    FullTimeEmployee('박광덕', 9111, 500)
    ]

print('================ 직원정보 =================\n')

for person in people : 
    person.show_info()
    print("-"*30)
