#todo:
# Создайте лямбда функцию, которая принимает один параметр – строку.
# Переводит все буквы в нижний регистр и переворачивает их в обратном порядке. Пример входа: ‘ACbdzYx’,
# Вывод: 'xyzdbca'


txt = input("Введите строку: ")

txt = (lambda s: s[::-1].lower())(txt)

print(txt)