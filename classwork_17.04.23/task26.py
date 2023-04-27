# todo:
#  Напишите функцию, которая принимает два аргумента, lst - список чисел и x – число.
#  Функция возвращает список, содержащий квадраты чисел из lst, которые больше числа x.
#  Сделайте несколько вариантов решений:
#  1) Просто цикл с условием.
#  2) Воспользуйтесь функцией filter, для чего создайте функцию проверки числа больше x
def choise(n):
    return n>num

def kwadrats(lst, x):
    lst = list(lst)
    kwadFiltered = []
    
    for i in lst:
        if i > x:
            kwadFiltered.append(i ** 2)

    return kwadFiltered
 
def kwadrats2(lst):
    #relist2 = list(filter(lambda n: (n>x) , lst))
    reList = list(map(lambda n: n**2, filter(choise, lst)))

    return list(reList)


lstIn = list([1, 10, 15, 23, 5])
num = 12

lst1 = kwadrats(lstIn, num)
lst2 = kwadrats2(lstIn)

print(lst1)
print(lst2)