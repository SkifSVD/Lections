#todo: Создать абстрактный класс Transport (транспорт) содержащий:
# Поля:
# скорость;
# себестоимость перевозки груза;
# стоимость перевозки груза.
# В классе должны быть абстрактные методы:
# метод Cost (без параметров) – вычисление стоимости перевозки груза.
# Метод Info - информация (без параметров), который возвращает строку, содержащую информацию об объекте.
#
# На его основе реализовать дочерние классы:
# Marine - морской транспорт,
# Ground - наземный транспорт.

from abc import ABC, abstractmethod

class Transport(ABC):
    speed = 0
    price = 0
    cost = 0
    @abstractmethod
    def Cost(self):
        print(f"Цена: {self.cost}")

    def Info(self):
        print(f"Скорость: {self.speed}, стоимость: {self.price}")

class Marine(Transport):
    def __init__(self, name, price, cost):
        self.name = name
        self.price = price
        self.cost = cost

    def Cost(self):
        print(f"Цена: {self.cost}")

    def Info(self):
        print(f"Скорость: {self.speed}, стоимость: {self.price}")

class Ground(Transport):
    def __init__(self, name, price, cost):
        self.name = name
        self.price = price
        self.cost = cost

    def Cost(self):
        print(f"Цена: {self.cost}")

    def Info(self):
        print(f"Скорость: {self.speed}, стоимость: {self.price}")


m1 = Marine("Корабль 1", 0.35, 35000)
m2 = Marine("Корабль 2", 0.50, 50000)

g1 = Marine("Автомобиль 1", 0.10, 2300)
g2 = Marine("Автомобиль 2", 0.20, 4600)

m1.Info()
m1.Cost()
m2.Info()
m2.Cost()
g1.Info()
g1.Cost()
g2.Info()
g2.Cost()