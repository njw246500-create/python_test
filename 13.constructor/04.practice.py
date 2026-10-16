'''
은행 : 개설할 때 계좌주 이름과 초기 예금액을 넣어줌 
        입금하면 잔고 변경
        출금 잔고 변경 (찾는 금액 잔액보다 많으면 출금안되게 출력'잔액부족')


'''


class Bank : 
    def __init__(self, name = input("이름을 입력하세요") , budget = 0) : 
            self.name = name
            self.budget = budget
            print("현재 잔액은 0원 입니다.")

    def budget_change(self, a, budget) : 
        budget += a 
        print(f"입금금액 {a}원 입금 후의 통장 잔고는 {budget}원 입니다. ")
        return a, budget

    def budget_out(self, a, budget) : 
        if a > budget : 
            print("잔액부족")

        if a <= budget :
            b = budget - a
            print(f"찾으시는 금액 {a}원을 출금합니다. 남은 잔액은 {b}원 입니다. ")
            return b
            


myBank = Bank()
a = int(input(f"{myBank.name}님 얼마를 입금하실 예정입니까?"))

myBank.budget_change(a, myBank.budget)

b = int(input(f"{myBank.name}님 얼마를 출금하실 예정입니까?"))\

myBank.budget_out(b, myBank.budget)