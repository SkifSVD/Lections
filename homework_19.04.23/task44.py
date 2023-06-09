#todo: Напишите программу, в которой используется две функции. В одной программа «спит» 2 секунды, в другой – 3 секунды. Пусть каждая функция возвращает время, которое она «проспала».
# Главная программа запускает цикл от 0 до 10, если число четное, то запускает функцию с 2 секундами, если нечетное, то функцию с 3 секундами. Накапливает сон обеих функций отдельно и печатает две суммы.

import time

def f_sleep_1():
    print("Старт первой функции и сна 2с")
    time.sleep(2)
    return 2

def f_sleep_2():
    print("Старт второй функции и сна 3с")
    time.sleep(3)
    return 3


t1 = 0
t2 = 0

for i in range(11):
    if i == 0:
        print("Число равняется 0")
    elif i%2 == 0:
        t1 += f_sleep_1()
        
    else:
        t2 += f_sleep_2()
    print(i)
        

print(f'Первая функция спала: {t1}c, а вторая: {t2}c')

