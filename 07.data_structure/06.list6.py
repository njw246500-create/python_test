'''
사용자로 부터 정수 4개를 입력받아
리스트에 저장하고 합계 출력

'''

numList = [0,0,0,0]
# numList2 = [ 0 for i in range(101) ]
# print(numList2)

# sum = 0
# numList[0] = int(input("숫자 : "))
# numList[1] = int(input("숫자 : "))
# numList[2] = int(input("숫자 : "))
# numList[3] = int(input("숫자 : "))

# sum = numList[0] + numList[1] + numList[2] + numList[3] 
# print("합계 :", sum)
# print("-")
# for문 -> 어떤게 변하고 어떤게 안변하는지 체크

# numList = [0,0,0,0]
# sum = 0
# for x in range(4) : 
#     numList[x] = int(input("숫자 : "))
#     sum += numList[x]
# print('합계 :', sum)

# 비어있는 리스트일경우 하는방법
# numList = []
# sum = 0
# for x in range(4) : 
#     num = int(input("숫자 : "))
#     numList.append(num)
#     sum += numList[x]
# print('합계 :', sum)
# print(numList)

numList = [0,0,0,0]
for x in range(4) : 
    numList[x] = int(input("숫자 : "))
print('합계 :', sum(numList))