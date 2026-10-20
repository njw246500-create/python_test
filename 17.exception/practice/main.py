from exceptions import SeatAlreadyError, SeatNotError
from movie import Movie 

# 클래스는 객체생성먼저

movie = Movie("아바타4", 10)

try : 
    movie.reserve(3)
    movie.reserve(5)
    movie.reserve(3)

except (SeatAlreadyError, SeatNotError, ValueError) as e : 
    print('[처리 실패]', e)

movie.show()

try : 
    movie.cancel(3)
    movie.cancel(5)
except (SeatAlreadyError, SeatNotError, ValueError) as e : 
    print('[처리 실패]', e)