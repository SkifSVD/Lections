# todo: Даны переменные A, B, C. Изменить их значения, переместив содержимое A в B, B — в C, C — в A,
# и вывести новые значения переменных A, B, C.

a = 6
b = 10
c = 2
print("Даны переменнаые:\n\tA = ", a, "\n\tB = ", b, "\n\tC = ", c)

tmp = a
a = c
c = b
b = tmp

print("После перестановки:\n\tA = ", a, "\n\tB = ", b, "\n\tC = ", c)