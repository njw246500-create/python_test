import my_module3 as m

print(m.PI)
print(m.fruits)

print(m.fruits[2])

m.count = 5
print(m.count)

print(m.add(3,7))

# 클래스
student = m.Student('김마리', 25)
student.introduce()
m.Student.hello()

# 람다함수
print(m.square(5))