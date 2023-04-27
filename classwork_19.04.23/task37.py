#todo: Реализовать декоратор в котором нужно подсчитать кол-во вызовов декорированной функции в процессе выполнения кода.
# Выгрузить статистику подсчета в файл debug.log в формате: Название функции, кол-во вызовов, дата-время последнего выполнения
# Пример:
# render, 10,  12.05.2022 12:00
# show,    5,  12.05.2022 12:02
# render, 15,  12.05.2022 12:07
#
# Декоратор должен применяться для различных функций с переменным числом аргументов.
# Статистику вызовов необходимо записывать в файл при каждом запуске скрипта.

#from datetime import datetime
#from fileinput import filename
#import pickle

from datetime import datetime

def get_time():
    return datetime.now().strftime('%d.%m.%Y %H:%M')

def count_func(func):
    count = 0
    
    def warp(*args, **kwargs):
        f = open(filename, 'a')
        nonlocal count
        count += 1
        res = func(*args, **kwargs)
        f.write(f'{func.__name__}, \t{count}, \t{get_time()}\n')
        f.close()
        
        return res
    return warp

@count_func
def func1():
    print("Выполнение первой функции.")
    pass

@count_func
def func2():
    print("Выполнение второй функции.")
    pass

filename = 'log37.txt'
f = open(filename, 'w')
f.write(" ")
f.close()

func1()
func1()
func2()
func1()
func2()

f = open(filename, 'r')
print(*f)
f.close()

