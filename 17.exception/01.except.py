# 보통 else 는 잘안씀.. 

# 예외처리 : try - except - finally

# try : 
#     #오류가 발생할 가능성이 있는 코드
#     result = 10 / 0
#     print(result)
#     print('try 에서 실행됨')

# except : 
#     # 오류가 발생했을때 실행할 코드
#     print('오류 발생. 0으로 나눌 수 없음')

print('프로그램 끝') 

# try : 
#     num = int(input('숫자 입력 :'))
#     result = 10 / num

# except ValueError: 
#     print('숫자만 입력해야됩니다')

# except ZeroDivisionError as e: 
#     print(f'0으로 나눌 수 없음. (에러 메시지 : {e})')

try :
    f = open('17.exception/data.txt','r')

except FileNotFoundError :
    print('파일이 존재하지 않습니다')

else : 
    print("파일을 성공적으로 읽었습니다 ")
finally :
    print("작업을 끝냅니다")

    # finally 는 오류가 나도 실행을 함. 없으면 오류나면 실행안함. 