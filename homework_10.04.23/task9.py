# todo: Дан номер некоторого года (положительное целое число).
# Вывести соответствующий ему номер столетия, учитывая, что, к примеру, началом 20 столетия был 1901 год.

year = int(input("Введите год (положительное целое число): "))
while year <= 0:
    year = int(input("Вы ввели не верное значение! Введите положительное целое число: "))

stoletie = ((year - (year % 100 - 1)) + 100) // 100

print(year, " год относится к ", stoletie, " столетию.")