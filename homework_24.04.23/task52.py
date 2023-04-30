#todo:
#  Разработать систему учета решения задач учениками курса «Разработчик на Питоне».
#
# Проблема.
# Преподаватель каждый урок задает некоторое количество задач в качестве домашнего задания, для упрощения можно считать, что одну.
# Каждый ученик решает каждую задачу. Переводит ее статус в решенную.
# Преподаватель проверяет каждую задачу каждого ученика и либо подтверждает ее статус как решенную или меняет ее статус как не решенную.
# Вопрос. Как спроектировать систему классов на Питоне для решения задачи учета?
# Разработайте систему
# классов (Teacher, Pupil, Lesson, Task. Нужен ли класс Группа?);
# атрибутов для каждого состояния каждого объекта;
# методов для каждого объекта.
# Отчетность? Запросы? Начните с формулировки решаемой задачи – спецификации или технического задания. Затем спроектируйте классы, атрибуты, методы. Протестируйте систему.

from copy import copy

class Teachers:
    """Список преподавателей на случай если надо будет добавлять несколько"""
    teachers = []
    """Инициализация объекта Учителя"""
    def __init__(self, name, tname, lname):
        self.name = name
        self.tname = tname
        self.lname = lname

    """Метод добавления нового преподавателя"""
    def addTeacher(self, name, tname, lname):
        self.teachers.append(Teachers(name, tname, lname))

    """Получаем объект преподавателя"""
    def getTeach(self, id):
        return self.teachers[int(id)-1]

    """Отображение списка преподавателей"""
    def lstTeach(self):
        for i in range(len(self.teachers)):
            print("ID ", i+1, self.teachers[i].name, self.teachers[i].tname, self.teachers[i].lname)
            print('_'*100)
        


class Students:
    
    def __init__(self, name, tname):
        self.name = name
        self.tname = tname
        self.students = []
        self.tasks = []

    def addStudent(self, name, tname):
        self.students.append(Students(name, tname))

    def getStud(self, id):
        return self.students[int(id)-1]

    def updLessons(self, id, lessLst):
        lst = self.students[int(id)-1].tasks
        lstLess = lessLst
        tmp = []

        for i in range(len(lstLess)):
            for j in range(len(lstLess[i].tasks)):
                tmp.append(lstLess[i].tasks[j])
            
        for i in tmp:
            b = False
            for j in lst:
                if i.name == j.name:
                    b = True
                    break
            if b == False:
                lst.append(copy(i))

        self.students[int(id)-1].tasks = lst

    def updLessForAllStud(self, lessLst):
        for i in range(len(self.students)):
            lst = self.students[i].tasks
            lstLess = lessLst
            tmp = []
            for j in range(len(lstLess)):
                for k in range(len(lstLess[j].tasks)):
                    tmp.append(lstLess[j].tasks[k])

            for j in tmp:
                b = False
                for k in lst:
                    if j.name == k.name:
                        b = True
                        break
                if b == False:
                    lst.append(copy(j))

            self.students[i].tasks = lst

    def dispStudentTask(self, id):
        lst = self.students[int(id)-1].tasks

        for i in range(len(lst)):
            print("ID", i+1, lst[i].name, lst[i].status)

    def changeStatus(self, idS, idT):
        self.students[int(idS)-1].tasks[int(idT)-1].status = not self.students[int(idS)-1].tasks[int(idT)-1].status

    def studList(self):
        for i in range(len(self.students)):
            print("ID", i+1, self.students[i].name, self.students[i].tname)
            print('_'*100)

class Lessons:
    """Инициализация объекта Lessons"""
    def __init__(self, name, author):
        self.name = name
        self.author = author
        self.tasks = []
        self.lessons = []

    """Добавление нового урока"""
    def addLesson(self, name, author):
        self.lessons.append(Lessons(name, author))

    def addTaskToLess(self, id, name):
        self.lessons[int(id)-1].tasks.append(Tasks(name))

    def getLstLess(self):
        return [x for x in self.lessons]


    def lstLess(self):
        print()
        for i in range(len(self.lessons)):
            print("ID ", i+1, self.lessons[i].name, "\tАвтор:", self.lessons[i].author.name, self.lessons[i].author.tname)
            for j in range(len(self.lessons[i].tasks)):
                print("\tID ", j+1, self.lessons[i].tasks[j].name)
            print('_'*100)
        print('='*100)
        

class Tasks:
    """Инициализация задания"""
    def __init__(self, name):
        self.name = name
        self.status = False

    def addTask(self, name):
        self.name = name
        self.status = False


#Добавляем объекты
teach = Teachers('', '', '')
less = Lessons('', '')
stud = Students('', '')

#Создаём преподавателей
teach.addTeacher("Иван", "Владимирович", "Волков")
teach.addTeacher("Герман", "Андреевич", "Суздальский")

#Создаём студентов
stud.addStudent("Григорий", "Степанович")
stud.addStudent("Епифаний", "Маркович")
stud.addStudent("Антон", "Леонидович")
stud.addStudent("Максим", "Батькович")

#немного заполним список уроков и занятий

less.addLesson("Урок 1", teach.getTeach('1'))
less.addTaskToLess('1', "Задание 1")
less.addTaskToLess('1', "Задание 2")
less.addLesson("Урок 2", teach.getTeach('1'))
less.addTaskToLess('2', "Задание 3")
less.addTaskToLess('2', "Задание 4")

stud.updLessForAllStud(less.getLstLess())

while True:
    print("Сделайте выбор:\n"
          "1 - Вы Преподаватель\n"
          "2 - Вы студент\n"
          "3 - Выход")
    choise = input()
    obj = 0
    if choise == '1':
        #Выбор преподавателя и работа с меню преподавателя
        choise = ''
        teach.lstTeach()
        id1 = input("Введите свой ID: ")
        obj = teach.getTeach(id1)
        print("\nЗдравствуйте", obj.name, obj.tname)
        print('_'*100)
        while True:
            choise = ''
            print("1 - Посмотреть список пройденных уроков\n"
                  "2 - Добавить новый урок\n"
                  "3 - Добавить задание\n"
                  "4 - Показать список студентов\n"
                  "5 - Проверить выполнение заданий\n"
                  "0 - Назад")
            choise = input()
            if choise == '1':
                #Просмотр списка пройденных Уроков
                less.lstLess()
            elif choise == '2':
                less.addLesson(input("Введите название урока: "), obj)
                less.lstLess()
            elif choise == '3':
                choise = ''
                less.lstLess()
                print("Выберете ID урока для добавления занятия")
                id2 = input()
                less.addTaskToLess(id2, input("Введите название задания: "))
                less.lstLess()
                stud.updLessForAllStud(less.getLstLess())
            elif choise == '4':
                stud.studList()
            elif choise == '5':
                choise = ''
                stud.studList()
                id2 = input("Введите ID студента: ")
                stud.dispStudentTask(id2)
                while True:
                    print("1 - Изменить статус задания\n"
                          "0 - Назад")
                    choise = input()
                    if choise == '1':

                        stud.changeStatus(input("Введите ID задания: "), id2)
                        pass
                    elif choise == '0':
                        break
            elif choise == '0':
                break

    elif choise == '2':
        #Выбор Студента и работа с меню студента
        choise = ''
        stud.studList()
        id1 = input("\nВведите ваш ID: ")
        obj = stud.getStud(id1)
        print("\nЗдравствуйте", obj.name, obj.tname)
        print('_'*100)
        while True:
            choise = ''
            print("1 - Посмотреть список полученных заданий\n"
                  "2 - Обновить список заданий\n"
                  "3 - Изменить статус задания\n"
                  "0 - Назад\n")
            choise = input()
            if choise == '1':
                stud.dispStudentTask(id1)
            elif choise == '2':
                stud.updLessons(id1, less.getLstLess())
                stud.dispStudentTask(id1)
            elif choise == '3':
                stud.dispStudentTask(id1)
                id2 = input("\nВведите ID задания: ")
                stud.changeStatus(id1, id2)
                stud.dispStudentTask(id1)
                pass
            elif choise == '0':
                break
    elif choise == '0':
        break
