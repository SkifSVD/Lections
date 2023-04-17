#Единицы массы пронумерованы следующим образом: 1 — килограмм, 2 — миллиграмм, 3 — грамм, 4 — тонна, 5 — центнер.
#Дан номер единицы массы и масса тела M в этих единицах (вещественное число). Вывести массу данного тела в килограммах.
# Данную задачу нужно решить с помощью конструкции  match  (Python v3.10)


# Пример:
# Введите единицу массы тела
#       1 - килограмм
#       2 — миллиграмм
#       3 — грамм
#       4 — тонна
#       5 — центнер
#>4

#Введите  массу тела
#>1

#Ответ: 1000 кг
print("Введите единицу массы тела")
print("      1 - килограмм")
print("      2 - миллиграмм")
print("      3 - грамм")
print("      4 - тонна")
print("      5 - центнер")

typeMass = int(input())

while typeMass <= 0 or typeMass > 5:
    print("Введите единицу массы тела")
    print("      1 - килограмм")
    print("      2 - миллиграмм")
    print("      3 - грамм")
    print("      4 - тонна")
    print("      5 - центнер")

    typeMass = int(input())

mass = float(input("Введите массу тела "))

while mass <= 0:
    mass = float(input("Введите массу тела "))

def printMass(typeMass):
    match typeMass:
        case 1:
            return mass
        case 2:
            return mass /  1000000
        case 3:
            return mass / 1000
        case 4:
            return mass * 1000
        case 5:
            return mass * 100



print("Ответ: ", printMass(typeMass), " кг")