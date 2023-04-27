# todo: Создайте функцию, которая принимает два аргумента, год и месяц, и возвращает list comprehension,
# содержащий все даты этого месяца в этом году. Используйте функцию monthrange(year, month) из модуля
# calendar для нахождения числа дней в месяце.

from calendar import monthrange


def dayofmountinyear(mo, ye):

    return [z for z in range((monthrange(ye, mo))[1])]
    
    
        

year = 1987
mount = 5

days = dayofmountinyear(mount, year)

print(days)