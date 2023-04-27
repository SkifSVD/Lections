# todo:
#  Создайте класс Shape, объекты которого имеют атрибуты
#  Colour – строка, например, «Красный», «Синий»;
#  Square – площадь объекта.
#  Создайте несколько методов:
#  1) Установить цвет объекта.
#  2) Запросить цвет объекта и напечатать его.
#  3) Задать площадь объекта.
#  4) Запросить площадь  объекта.

class Shape:
    Colour = "Красный"
    Square = 32

    def set_color(self, Colour):
        self.Colour = Colour

    def get_colour(self):
        return self.Colour

    def set_square(self, Square):
        self.Square = Square

    def get_squere(self):
        return self.Square

sh = Shape()

print(f'Цвет: {sh.get_colour()}, Площадь: {sh.get_squere()}')

sh.set_color("Зелёный")
print(f'Цвет: {sh.get_colour()}, Площадь: {sh.get_squere()}')

sh.set_square(43)
print(f'Цвет: {sh.get_colour()}, Площадь: {sh.get_squere()}')