# todo: Решить линейное уравнение A·x + B = 0, заданное своими коэффициентами A и B (коэффициент A не равен 0).
# Примечание: коэффициенты получаем через функцию input().

a = input("Введите коэффициент А ")

while not a.isdigit():
    a = input("Введите коэффициент А ")

a = int(a)

b = input("Введите коэффициент B ")

while not b.isdigit():
    b = input("Введите коэффициент B ")

b = int(b)

x = -b/a
print("Неизвестное х = ", x)
print("Проверка: ", a, " * ", x, " + ", b, " = ", a*x+b)