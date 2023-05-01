# todo: Создать абстрактный класс Press (пресса) содержащий:
# Поля: название, цена за единицу.
# В классе должны быть абстрактные методы:
# метод SetPrice (без параметров) – установка цены.
# Метод Info - информация (без параметров), который возвращает строку, содержащую информацию об объекте.
#
# На его основе реализовать дочерние классы:
# Magazine - журнал,
# Book- книга.

from abc import ABC, abstractmethod
from selectors import DefaultSelector

class Press(ABC):
    name = ""
    price = 0

    @abstractmethod
    def SetPrice(self):
        pass

    def Info(self):
        return f"Название: {self.name}, Стоимость: {self.price} руб."

class Magazine(Press):
    def __init__(self, name):
        self.name = name

    def SetPrice(self, price):
        self.price = price

class Book(Press):
    def __init__(self, name):
        self.name = name

    def SetPrice(self, price):
        self.price = price
        


m1 = Magazine("Сад и огород")
m1.SetPrice(128.50)

b1 = Book("Мастер и Маргарита")
b1.SetPrice(1230.43)
print(m1.Info())
print(b1.Info())