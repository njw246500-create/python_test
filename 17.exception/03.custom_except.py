# 나만의 커스텀 에러를 만들어사용
# 방법1 : 에러메시지를 던질 때 직접 입력받도록   

# 커스텀 에러 클래스정의
class BankBalanceError(Exception) : 
    def __init__(self, message='계좌의 잔액이 부족하여 출금 못함'):
        super().__init__(message)

# 입금 함수
def deposit(balance, money) : 
    if money <= 0 :
        raise BankBalanceError(f"{money}원, (0원 이하 불가)")

    balance += money
    print(f"[입금 완료] 현재잔액 {balance}원")
    return balance

# 출금 함수
def withdraw(balance, money) :
    if balance < money : 
        raise BankBalanceError()

    balance -= money
    print(f"[출금 완료] 현재잔액 {balance}원")
    return balance

# try :
#     current_balance = 5000
#     current_balance = deposit(current_balance, 3000)
#     current_balance = deposit(current_balance, -3000) # 오류발생 
#     current_balance = withdraw(current_balance, 10000) # 오류발생
# except BankBalanceError as e :
#     print(f"[뱅킹 오류] : {e}") 

# 방법2 
# 출금용과 입금용 커스텀 에러 클래스를 따로 정의 
class BankBalanceErr(Exception) : 
    def __init__(self):
        super().__init__('계좌의 잔액이 부족하여 출금 못함')

class DepositErr(Exception) : 
    def __init__(self,money):
        super().__init__(f"{money}원, (0원 이하 불가)")

# 입금 함수
def deposit(balance, money) : 
    if money <= 0 :
        raise DepositErr(money)

    balance += money
    print(f"[입금 완료] 현재잔액 {balance}원")
    return balance

# 출금 함수
def withdraw(balance, money) :
    if balance < money : 
        raise BankBalanceErr()

    balance -= money
    print(f"[출금 완료] 현재잔액 {balance}원")
    return balance

try :
    current_balance = 5000
    current_balance = deposit(current_balance, 3000)
    # current_balance = deposit(current_balance, -3000) # 오류발생 
    current_balance = withdraw(current_balance, 10000) # 오류발생
except (BankBalanceErr, DepositErr) as e :
    print(f"[뱅킹 오류] : {e}") 
