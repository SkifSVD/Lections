#todo
# Создайте декоратор, которые переводит все текстовые аргументы функции в верхний регистр и возвращает их в виде списка текстовых аргументов.
class Person:
    def __init__(self, name, lstname):
        self.name = name
        self.lstname = lstname

    @property
    def get_upper(self):
        return [self.name.upper(), self.lstname.upper()]


p1 = Person("владимир", "волков")

print(p1.get_upper)