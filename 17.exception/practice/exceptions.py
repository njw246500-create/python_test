class SeatAlreadyError(Exception) : 
    def __init__(self, seat_num):
        self.seat_num = seat_num 
        super().__init__(f'{self.seat_num}번 좌석은 이미 예약되어 있습니다.')

class SeatNotError(Exception) : 
    def __init__(self, seat_num):
        self.seat_num = seat_num 
        super().__init__(f'{self.seat_num}번 좌석은 유효하지 않습니다.') 