# 파일 열기
#
# 전체내용 읽어오기
# with open('11.file/test.txt','r') as f :
#     text = f.read()
#     print(text)
#     t1 = text.split('\n')
#     print(t1)

# 한행만 읽어오기 

# with open('11.file/test.txt','r') as f:
#     text = f.readline()
#     print(text)


with open('11.file/test.txt','r') as f:
    # text_lines = f.readlines() # 모든 내용을 1행씩 읽어와서 리스트로 저장
    text_lines = [text_lines.strip() for text_lines in f.readlines() ] # strip()함수로 앞,뒤 공백과 줄바꿈 없애줌
    text_lines = f.read().splitlines() # 1행씩 잘라주는 함수
    print(text_lines)