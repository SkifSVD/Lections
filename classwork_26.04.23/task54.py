# todo:
#  Функция get_weekday()
#  Реализуйте функцию get_weekday(), которая принимает один аргумент:
#
#  number — целое число (от 1 до 7 включительно)
#  Функция должна возвращать полное название дня недели на русском, который соответствует числу number, при этом:
#
#  если number не является целым числом, функция должна возбуждать исключение:
#  TypeError('Аргумент не является целым числом')
#  если number является целым числом, но не принадлежит отрезку [1;7]
#  функция должна возбуждать исключение:
#  ValueError('Аргумент не принадлежит требуемому диапазону')

#todo:
# Сделайте функцию get_weekday() статической в классе Helper

class Helper:
    @staticmethod
    def get_weekday(n):
        d = {1:"Понедельник", 2:"Вторник", 3:"Среда", 4:"Четверг", 5:"Пятница", 6:"Суббота", 7:"Воскресенье"}
        try:
            a = (d[int(n)])

        except KeyError:
            print("Значение должно быть в пределах от 1 до 7")
            a = "Ошибка пределов"
        except ValueError:
            print("Не является числом")
            a = "Ошибка типа входных данных"
        return a

    


h = Helper()


print(h.get_weekday(7))