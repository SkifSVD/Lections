# todo:
#  Создайте класс Triangle с методом, который при создании объекта проверяет три переменный x, y, z на то,
#  что из них можно составить треугольник. Требования: все числа должны быть больше нуля, сумма любых двух должны быть больше третьего.

class Triangle:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        if self.x > 0 and self.y > 0 and self.z > 0:
            print("Первое условие выполнено!")
            if x + y > z and x + z > y and y + z > x:
                print("Второе условие выполнено!")
            else:
                if x + y > z:
                    print("Сумма X и Y должна быть больше Z")
                elif x + z > y:
                    print("Сумма X и Z должна быть больше Y")
                elif z + y > x:
                    print("Сумма Z и Y должна быть больше X")
        else:
            if self.x > 0:
                print("X должен быть больше 0")
            elif self.y > 0:
                print("Y должен быть больше 0")
            elif self.z > 0:
                print("Z Должен быть больше 0")


    def print(self):
        print(self.x, self.y, self.z)
        


x = 2
y = 2
z = 3

t1 = Triangle(x, y, z)

t1.print()

