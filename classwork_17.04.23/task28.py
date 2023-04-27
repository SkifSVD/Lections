#todo:
#    Дан список чисел.  Превратить его в список суммы цифр каждого числа. Пример входа: lst = [123, 234, 345, 456]
#    Вывод: [6, 9, 12, 15]
#    При решении используйте map и lambda

lst = [123, 234, 345, 456]
result = []
#result2 = []
for i in lst:
    l = sum([int(a) for a in str(i)])
    result.append(l)

for i in lst:
    result2 = list(map(lambda n: sum(n), ((int(u) for u in str(a)) for a in lst)))

print(result)
print(result2)