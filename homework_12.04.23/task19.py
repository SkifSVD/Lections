#todo: Напишите калькулятор (простой). На вход подается строка, например:
# 1 + 2  или  5 – 3  или  3 * 4  или  10 / 2.
# Вывод: сосчитать и напечатать результат операции.
# Гарантируется, что два операнда и операция есть в каждой строчке, и все они разделены пробелами.

from unittest import result


a = input("Введите выражение: ")

lst = a.split()
result = 0
if lst[1] == '+':
    result = int(lst[0]) + int(lst[2])
elif lst[1] == '-':
    result = int(lst[0]) - int(lst[2])
elif lst[1] == '*':
    result = int(lst[0]) * int(lst[2])
elif lst[1] == '/':
    result = int(lst[0]) / int(lst[2])

print(result)