'''
불꽃기사,35,920,780
얼음마법사,28,850,420
그림자암살자,42,1200,350
숲의궁수,31,780,510
천둥전사,50,1500,1100
달빛사제,25,420,680
용기사,55,1800,1400
독안개도적,33,980,390
태양마법사,45,1350,600
바위골렘,40,650,1600
'''

##01. file_write . py #
'''
*파일 다루기
파일 열기 -> 파일을 읽거나 쓰기 -> 파일 닫기
open('파일명', '모드') -> write('문자열') -> close() or with

f = open('경로') -> f.write -> f.close & print 해서 확인하기!
'''

# 파일 열기
# f = open('11.file/practice.txt','w')
# # 파일에 데이터 쓰기 
# f.write('데이터 출력\n')
# f.write('5')
# f.write('''불꽃기사,35,920,780
# 얼음마법사,28,850,420
# 그림자암살자,42,1200,350
# 숲의궁수,31,780,510
# 천둥전사,50,1500,1100
# 달빛사제,25,420,680
# 용기사,55,1800,1400
# 독안개도적,33,980,390
# 태양마법사,45,1350,600
# 바위골렘,40,650,1600''')
# f.close()
# print('쓰기완료')

# for i in range(1,11) : 
#     f.write(str(i) + '번째 줄입니다\n')
#     # f.write(f"{i}번째 줄입니다.\n")
# f.close()
# print("쓰기 완료")


# with open (file, mode, encoding) as 참조변수:
#    참조변수.write("파일에 글쓰기")
with open("11.file/with_test.txt",'w') as f : # with 블록을 벗어나는 순간 파일을 알아서 닫아준다. close 를 할 필요가 없음 
    for i in range(1,11) : 
        f.write(f"{i}번째 줄입니다.\n")
    f.write('with로 파일 닫기')




## 02.file_read.py# 
#전체내용 읽어오기
# with open('11.file/practice.txt','r') as f :
#     text = f.read()
#     print(text)
#     t1 = text.split('\n') # 줄바꿈에 의해서 출력을 분리 시키는것임 
#     print(t1)

# # 한행만 읽어오기 
# print("-"*30)
# with open('11.file/practice.txt','r') as f:
#     text = f.readline() #첫째줄만 읽고 문자열로 반환하는 함수
#     print(text)
# print("-"*30)

with open('11.file/practice.txt','r') as f:
    # text_lines = f.readlines() # 모든 내용을 1행씩 읽어와서 리스트로 저장
    # text_lines = text_lines.strip()
    text_lines = [ text_lines.strip() for text_lines in f.readlines() ] # strip()함수로 앞,뒤 공백과 줄바꿈 없애줌
    text_lines = f.read().splitlines() # 1행씩 잘라주는 함수
    print(text_lines)




## 03.file.append.py##
# 추가모드로 열기
# with open('11.file/practice.txt','a') as f: # 'a'문자는 추가한다는 명령어 
#     f.write('이어쓰기\n')

#     for i in range(11,21) : 
#         f.write(str(i) + '번째 이어쓰기\n')

# print("쓰기완료")

# # 덮어쓰기 막기
# with open('11.file/test2.txt','x', encoding = 'UTF-8') as f : # 'x' exclusive : 덮어쓰기가 불가능 한것임,
#     f.write('즐거운 하루')

# print('쓰기 완료')



## 04.file_csv.py ##
students = [[],[],[], ]
with open('11.file/test.csv','r') as f:
    a = [line.strip().split('.') for line in f.read().splitlines()]