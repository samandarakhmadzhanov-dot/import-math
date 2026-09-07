import math

a = float(input("Введите первый катет: "))
b = float(input("Введите второй катет: "))

c = math.sqrt(a**2 + b**2)
S = a * b / 2
P = a + b + c
k = math.degrees(math.atan(a / b))
h = math.degrees(math.atan(b / a))

print("Гипотенуза:", c)
print("Площадь:", S)
print("Периметр:", P)
print("Первый угол:", k)
print("Второй угол:", h)
