#todo Задача 1. Транспонирование матрицы, transpose(matrix)
#Создайте списковое включение, которое генерирует следующую последовательность: 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, и т.д. до 10


##todo Задача 2. Транспонирование матрицы, transpose(matrix)
#Написать функцию transpose(matrix), которая выполняет транспонирование матрицы. Решить с использованием списковых включений.
#Пример:
#>>> transpose([[1, 2, 3], [4, 5, 6]])

#[[1, 4], [2, 5], [3, 6]]


#||1 2 3||      ||1 4||
#||4 5 6||  =>  ||2 5||
#               ||3 6||



##todo Задача 3. Найти сумму элементов матрицы
#Написать msum(matrix)  которая подсчитывает сумму всех элементов матрицы:
#Задачу решить с помощью генераторов.

#>>> matrix = [[1, 2, 3], [4, 5, 6]]
#>>> msum(matrix)

def  transpose(matx):
    t = []
    for i in range(len(matx[0])):
        tmp = []
        for j in range(len(matx)):
            tmp.append(matx[j][i])
        t.append(tmp)
    return t

def msum(matx):
    s = 0
    for i in matx:
        for j in i:
            s += j

    return s


#Задание 1
n = 10
m = []

for i in range(n+1):
    for j in range(i):
        m.append(i)

print(f'Решение Задачи 1:\n{m}')


#Задание 2
matrix1 = [[1, 2, 3], [4, 5, 6]]

matrixT = transpose(matrix1)
print("\nРешение задание 2:\nИзначальная матрица:\n")
for i in matrix1:
    print(i)

print("\nПреобразованная матрица:\n")
for i in matrixT:
    print(i)

#Задание 3

print(f'\nСумма элементов в матрице: {msum(matrix1)}')
