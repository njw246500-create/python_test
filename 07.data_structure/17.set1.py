'''
*set : 중복불가, 
       순서가 없다(index 없음)
       {중괄호 사용}

    *** 주의 : 빈 set을 만들때 {} 이건 딕셔너리
        set() -> 만들어야 set이 됨


'''
a = {1,2,3,1,2,3,4,1,3,5}
print(a)  # 중복된거 전부 사라져서 출력함..
print(len(a))

b = {'홍길동', 3, 5, True, (4,5)}
print(b) # 순서가 내가 쓴대로 나오지 않음..

c = {}
print(type(c))

d = set()
print(type(d))