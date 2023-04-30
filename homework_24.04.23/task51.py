#todo:
# Определите класс Person. При создании объекта p=Person(‘Иванов’, ‘Михаил’, ‘Федорович’) необходимо ввести полное имя человека.
# При печати объекта должно выводиться следующее:
# print(p) # чивородеФлиахиМвонавИ

class Person:
    def __init__(self, name, lname, sname):
        self.name = name
        self.lname = lname
        self.sname = sname

    def __str__(self):
        return f'{self.sname[::-1]}{self.lname[::-1]}{self.name[::-1]}'

p = Person('Иванов', 'Михаил', 'Федорович')

print(p)
