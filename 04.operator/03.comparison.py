# 비교연산자 : 비교결과가 True, False 로 출력
# >, <, >=, <=
# ==, !=

num1 = int(input("첫번째 정수 입력 : ")) 
num2 = int(input("두번째 정수 입력 : "))

print(f"{num1}이 {num2}보다 큰가? {num1 > num2}")
print(f"{num1}이 {num2}보다 크거나 같은가? {num1 >= num2}")
print(f"{num1}이 {num2}보다 작은가? {num1 < num2}")
print(f"{num1}이 {num2}보다 작거나 같은가? {num1 <= num2}")
print(f"{num1}과 {num2}는 같은가? {num1 == num2}")
print(f"{num1}과 {num2}는 같지않은가? {num1 != num2}")