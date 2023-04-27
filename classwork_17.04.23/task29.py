#todo:
#  Реализуйте функцию convert(), которая принимает один аргумент:
#  number — целое число
#  Функция должна возвращать кортеж из трех элементов, расположенных в следующем порядке:
#  двоичное представление числа number в виде строки без префикса 0b
#  восьмеричное представление числа number в виде строки без префикса 0o
#  шестнадцатеричное представление числа number в виде строки в верхнем регистре без префикса 0x
#  Примечание 1. В задаче удобно воспользоваться функциями bin(), oct() и hex().
#  Задачу решить доступным способом
#  Задачу решить с помощью применения функции map и lambda
cort = (lambda x: bin(x),
        lambda x: oct(x),
        lambda x: hex(x))

def convert(num):

    return [bin(num)[2:], oct(num)[2:], hex(num)[2:].upper()]


number = 213

print(convert(number))
print([i(number)[2:].upper() for i in cort])
