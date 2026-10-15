'''
*파일 다루기
    파일 열기 -> 파일을 읽거나 쓰기 -> 파일 닫기
    open('파일명', '모드') -> write('문자열') -> close() or with
'''

# # 파일 열기
# f = open('11.file/test.txt','w')
# # 파일에 데이터 쓰기 
# # f.write('데이터 출력\n')
# # f.write('5')
# # f.write('True')

# # f.close()
# # print('쓰기완료')

# for i in range(1,11) : 
#     f.write(str(i) + '번째 줄입니다\n')
#     # f.write(f"{i}번째 줄입니다.\n")
# f.close()
# print("쓰기 완료")

with open("11.file/with_test.txt",'w') as f :
    for i in range(1,11) : 
        f.write(f"{i}번째 줄입니다.\n")
    f.write('with로 파일 닫기')