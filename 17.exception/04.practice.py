'''
문제 : 영화관 좌석 프로그램

- custom except 
1. 좌석이 예약된 상태에서 좌석을 선택했을 때 
2. 없는 좌석번호로 예약할 때 

- class
1. 초기화 영화제목, 총 좌석수 
2. 좌석이 유효한 좌석인지  
    좌석이 있으면 예약 되는것, 없는 좌석은 예외발생 
3. 예약
    예약하기. 이미 예약된 좌석이면 1번 except 발생 
4. 예약취소 
5. 출력하기 
영화 : ??? 
예약된 좌석 : ??? 
'''
# # 입금 함수
# def deposit(balance, money) : 
#     if money <= 0 :
#         raise DepositErr(money)

#     balance += money
#     print(f"[입금 완료] 현재잔액 {balance}원")
#     return balance

import random



class Movie : 
    def __init__(self, title, seat):
        self.title = title
        self.seat = seat 
        print(f"[예약정보] 영화 : {self.title}, 선택한 좌석 : {self.seat} ")

    def availseat(self) : 
        if self.seat <=0 or self.seat > 100 : 
            raise CustomException2
        print(f"{self.seat}번호는 예약가능한 범위의 좌석입니다.")

    def reserve(self) :
        if self.seat != 88 : 
            raise CustomException1
        print(f"{self.seat}는 현재 빈 자리입니다! 예약해드리겠습니다.")

    def announce(self) : 
        print(f"[예약정보 안내] \n 영화 : {self.title} \n 예약된좌석 : {self.seat}")

class CustomException1(Movie) : 
    def __init__(self) :
        super().__init__(f"좌석{self.seat}는 이미 예약되어있습니다.")

class CustomException2(Movie) : 
    def __init__(self) : 
        super().__init__(f"좌석번호가 없습니다.{self.seat}는 범위 밖의 번호입니다.")

 
current_seat = 0
try :
    current_seat = Movie('왕과 사는 남자', 88) # 클래스는 객체생성하고 대입해야나옴!! 
    current_seat.availseat() # 괄호도 넣어주어야함. 
    current_seat.reserve()
    current_seat.announce()



except (CustomException1, CustomException2) as e :
    print(f"[영화관 예약 오류] : {e}")

