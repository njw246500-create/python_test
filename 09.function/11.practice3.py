'''
문1) 카페 주문
메뉴와 사이즈를 2개 입력받음.
만약 사이즈가 입력이 안되서 무조건 small 사이즈임

문2) 택배 배송정보
받는사람, 주소, 전화번호를 입력받음.
순서와 상관없이 받아서 출력

문3) 친구들과 식당에 가서 각자 낸 금액의 합계 구하기(tuple)
친구들이 갈 때마다 인원이 달라짐

문4) 회원가입 정보를 입력받기(dict)
사람마다 입력하는 정보의 개수가 다를 수 있음 

'''

# # 문1# 
# def order(x,y='small') : 
#     x = input("카페의 메뉴를 입력하세요 : ")
#     y = input("음료의 사이즈를 입력하세요 : ")
#     print(f"주문하신 메뉴는 {x}, 사이즈는 {y}입니다.")
# x = 0
# y = 0
# order(x,y)

# # 문2# 
# customer = input("받는 사람의 성함을 입력하세요")
# address = input("배송받을 주소를 입력해주세요")
# number = input("받는사람의 전화번호를 입력해주세요")
# package(customer, address, number)

# def package(customer, address, number):
#     print(f"주문자 : {customer}, 주소 : {address}, 전화번호 : {number}")


# 문3 # 식당에 가서 낸 금액의 합계
n = input("사람이 몇명있나요?")
args = input("금액을 입력해주세요!")
def calc(*args,n) : 
    for i in range (n) : 
        receipt = args
        print(f"{receipt}의 금액으로 주문하셨습니다")
        sum = 0
        for x in args : 
            sum += x 
        return print(f"합계는{sum}입니다." )

# # 문4 # 회원가입 정보 입력받기 



# 정답# 


# 문1#
def order_coffee(menu,size = 'small') : 
    print(f"{menu} | {size} 사이즈 주문")

order_coffee("아메리카노")
order_coffee('카페라떼', 'large')
print("-"*30)

# 문2# 
def delivery(name, address, phone) : 
    print("받는 사람 :", name)
    print("주소 :", address)
    print("전화번호 :", phone)

delivery(phone = '010-1234-1234', name = '김철수', address='서울 강남' )

# 문3# 

def cal_bill(*money) : 
    total = 0
    for price in money : 
        total += price
    return total
print(cal_bill(13000, 9000))
print(cal_bill(13000, 9000, 12500))

# 문4 # 
def signup(**info) :
    print('회원가입 정보')

    for k, v in info.items() :
        print(k,':',v)

signup(
    name = '이상원',
    age = 25,
    email = 'abc@test.com'
)

signup(
    name = '홍말숙',
    age = 25,
    email = 'abcd@test.com',
)