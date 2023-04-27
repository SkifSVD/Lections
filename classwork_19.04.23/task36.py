#todo:
# Реализовать декоратор который подсчитывает время выполнения функции.

import time
def cicle(n):
    fib1 = 1
    fib2 = 1
 
    i = 0
    while i < n - 2:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        i = i + 1
    return fib2


n = 50
x = time.perf_counter_ns()
z = cicle(n)
y = time.perf_counter_ns()

print(f"Функция: {cicle.__name__} Выполнялась в теченииЖ {(y-x)/1000:0.2f} us")
