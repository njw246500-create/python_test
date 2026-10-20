from exceptions import SeatAlreadyError, SeatNotError

class Movie :
    def __init__(self, movie_title, total_seats):
        self.movie_title = movie_title
        self.total_seats = total_seats
        self.reserved_seats = [] # 사용자들한테 예약받을 좌석

    def validate_seat(self, seat_num) : 
        if not 1 < seat_num <= self.total_seats : 
            raise ValueError('존재하지 않는 좌석 번호 입니다') # raise 다음에 error 코드 쓰기

    def reserve(self, seat_num) : 
        self.validate_seat(seat_num) # seat_num을 넘겨서 유효한지 아닌지 먼저체크
        if seat_num in self.reserved_seats : 
            raise SeatAlreadyError(seat_num) # 에러를 적어주고 (넣어줄 값)

        self.reserved_seats.append(seat_num) # 번호를 리스트에 추가해주기
        print(f"{seat_num}번 예약 완료")

    def cancel(self, seat_num) : 
        self.validate_seat(seat_num)
        if seat_num not in self.reserved_seats : 
            raise SeatNotError(seat_num)

        self.reserved_seats.remove(seat_num)
        print(f"{seat_num}번 예약 취소 완료")

    def show(self) : 
        print(f"영화 : {self.movie_title}")
        print(f"예약된 좌석 : {sorted(self.reserved_seats)}")