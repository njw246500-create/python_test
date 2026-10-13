# 문제

'''
한 과일 가게의 현재 과일 재고 수량이 다음과 같이 딕셔너리에 저장되어 있다. 
inventory = {
    'apple' : 15,
    'banana' : 8,
    'orange' : 20,
    'melon' : 3

}
문1. 가게에 포도(grape)가 12개 새로 들어왔다. 추가하기
문2. 손님이 망고가 있는지 물어보았다. 망고가 있으면 재고 출력 없으면 '재고가 없습니다' 
문3. 오늘 마감 전, 현재 가게에 남아있는 모든 과일의 이름과 재고수량을 아래 보기와 같은 형식으로 한 줄씩 출력하는 코드를 작성
단, items() 메서드와 for문, f-string을 반드시 사용
[출력 보기]
과일 :  apple | 재고 : 15개
과일 : banana | 재고 : 8개




'''

##풀이##

inventory = {
    'apple' : 15,
    'banana' : 8,
    'orange' : 20,
    'melon' : 3
}

# 문1 # 
inventory['grape'] = 12
print(inventory)

# 문2 #  --> 복습하기
if 'mango' in inventory :
    print(inventory['mango'])
else :
    print("재고가 없습니다.")

# 문3 #
for key, value in inventory.items() : 
    print(f"과일 : {key} | 재고 : {value}개")


# 정답 # 

# 문제1 # -> 포도기 12개 
# inventory['grape'] = 12 # 만약기존에 있는것이라면 덮어쓰기가 된다. 추가되는 값이 아님!

# inventory['apple'] = inventory['apple'] + 12
# inventory['apple'] += 12
in_fr = 'grape'

if in_fr in inventory : 
    inventory[in_fr] += 12
else : 
    inventory[in_fr] = 12
print(inventory)


# 문제2 : mango # 

# in_fr = 'mango'
# if in_fr in inventory : 
#     inventory[in_fr] += 12
#     print("망고가 있습니다. 재고는", inventory['mango'])
# else : 
#     print("망고가 없습니다.")
# mango_count = inventory['mango']

mango = inventory.get('mango', '재고가 없습니다') # 얘는 오류가 안남. 
print(mango)

# 문3
for fruit, count in inventory.items() : 
    print(f'과일: {fruit} | 재고: {count}개')
