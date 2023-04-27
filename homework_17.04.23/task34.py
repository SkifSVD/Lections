# todo:
#  Напишите рекурсивную функцию sumn(n), которая вычисляет и печатает сумму чисел от 0 до n.

def sumn(n):
    tmp = 0
    for i in range(n+1):
        tmp += i
    return tmp


num = 10

print(sumn(num))