# todo:
#  Определите класс Person. В конструктор которого передается фамилия и возраст ('Иванов', 29)
#  Реализуйте через магические методы условие, при котором возраст у объекта не будет меняться после инициализации.

class Person:
    name = ""
    age = 1
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __setattr__(self, attr, value):
        if attr == 'name':
            self.__dict__[attr] = value

        elif attr == 'age' and value > 0:
            self.__dict__[attr] = value
        else:
            print("Вы ввели неверный возраст!")
            pass

    def __getattr__(self):
        return self.__age

p1 = Person("Иванов", 29)


print(p1.name, p1.age)

p1.age = 0
print(p1.name, p1.age)

p1.age = 15
print(p1.name, p1.age)