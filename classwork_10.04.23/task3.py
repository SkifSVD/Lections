# todo: Даны три точки A , B , C на числовой оси. Найти длины отрезков AC и BC и их сумму.
# Примечание: все точки получаем через функцию input().
# При решении задачи обратите внимание какой тип вы получаете через функцию input().

a = input("Введите координату точки А: ")

while not a.isdigit():
    a = input("Введите координату точки А: ")

a = int(a)

b = input("Введите координату точки B: ")

while not b.isdigit():
    b = input("Введите координату точки B: ")

b = int(b)

c = input("Введите координату точки C: ")

while not c.isdigit():
    c = input("Введите координату точки C: ")

c = int(c)

ac = c - a if c > a else a - c
bc = c - b if c > b else b - c
summ = ac + bc

print("Длина отрезков AC = ", ac, " и BC = ", bc, ". И их сумма: ", summ)