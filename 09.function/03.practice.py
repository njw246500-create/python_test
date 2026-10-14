'''
문1 : 2개의 수를 넣으면 그 사이의 숫자들의 합계 구하기
        3,10을 매개변수로 넣으면 3~10까지의 합계를 출력

문2 : 숫자만큼 별 찍기 매개변수에 3을 넣으면

*
**
***
이렇게 출력 되게 or 

    *
   ***
  *****

'''
# 문제 1 #
# def sum(x,y) : 
#     a = 0
#     for z in range(x,y+1) : 
#         a += x 
#         print("총 합은 ",a,"입니다")
#         x += 1
#     print("총 합은 ",a,"입니다")
#     return a

# x = int(input("첫번째 숫자를 넣으세요"))
# y = int(input("두번째 숫자를 넣으세요"))
# a = sum(x,y)


# # 문제 2 # 

# def star(x) :
#     for i in range(x+1) :
#         print('*'*i)

# def star1(x) :
#     for i in range(1,x+1,2) : 
#         z = '*'*i
#         print(z.center(x+1))

# x = int(input("찍고싶은 별의 개수를 입력해주세요."))
# y = star(x)
# z = star1(x)




## 정답# 

# def total(start,end) : 
#     sum = 0 
#     for x in range(start, end+1):
#         sum += x
#     return sum

# print(total(1,10))
# print(total(25,78))

# # 문2
# def star(n) : 
#     for x in range(n) : 
#         for y in range(x+1) : 
#             print('*', end='')
#         print()

# star(5)

# def star2(n) : 
#     for i in range(n) : 
#         print('*' * (i+1))



'''
  *  
 ***
*****

1헹 (i=0) : 공백 4개, 별 1개
2헹 (i=1) : 공백 3개, 별 3개
3행 (i=2) : 공백 2개, 별 5개
4헹 (i=3) : 공백 1개, 별 7개
5행 (i=4) : 공백 0개, 별 9개


'''
def star_pyramid(rows) : 
    for i in range(rows) : # rows = 5, 0~4 
        # space = ' ' * rows-(1+i) 
        # stars = '*' * (i*2+1)
        # print(space + stars)

        print(' ' * (rows-(1+i)) + '*' * (i*2+1))

star_pyramid(5)