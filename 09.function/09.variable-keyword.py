# 가변 키워드 인자 
# **kwargs : dictionary가 전달됨 # keyword argument

def print_info(**kwargs) : 
    for key, value in kwargs.items() :
        print(key, ':', value)

print_info(name='최명길')
print_info(name='김미영', age = '23', city = 'Seoul')

# 딕셔너리를 넘겨줘도 됨
info = {'name' : '이사람', 'age' : 25, 'city' : 'Gyeonggi-do'} # 딕셔너리를 언패킹한상태로 인자를 넘겨줘야 한다.
print_info(**info) # **는 unpacking 해서 넘겨줌
# print_info(info) : error : info라는 딕셔너리 객체 단 1개를 전달

# **info 하면 아래와 같이 들어감
# print_info(name = '이사람', age = 25, city = 'Gyeonggi-do')

