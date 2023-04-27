# todo:
#   Создайте класс Pet с атрибутам имя, вес и уровень сытости.
#   Напишите метод info, который в качестве результата выдает эти атрибуты.
#   Напишите метод hungry, который возвращает уровень сытости и комментирует: если меньше 5, то «голоден», если больше 10, то «сыт».
#   Напишите метод feed, который передает питомцу некоторую еду, которая прибавляется к уровню сытости и вызывает метод info.


class Pet:
    def __init__(self, name, weight, eat):
        self.name = name
        self.weight = weight
        self.eat = eat

    def info(self):
        print(f'Имя: {self.name}, Вес: {self.weight}, Сытость: {self.eat}')

    def hungry(self):
        print(f'Уровень сытости: {self.eat}.', end = ' ')
        if self.eat < 5:
            print("Ваш зверёк голоден!")
        elif self.eat > 10:
            print("Ващ зверёк сыт.")

    def feed(self, eat):
        self.eat += eat

anim = Pet("Барсик", 5, 4)

anim.info()
anim.hungry()
anim.feed(10)
anim.hungry()




