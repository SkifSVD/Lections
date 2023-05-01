# #todo: Написать авторизацию пользователя в систему.
# При реализации авторизации спроектировать абстрактный класс и реализовать методы в наследуемом классе
# login, check_password, check_login

# При запуске программы пользователю необходимо ввести
# логин и пароль, поэтапно.
# login: _________
# password: ________
#
# При неправильном вводе логина должно генерироваться пользовательское исключение LoginNotFound
# Введеный пароль должен проверятся на длину. Длина должна быть более 8 символов иначе генерируем пользовательское
# исключение LengthError
# При вводе некорректного пароля генерируем соответсвуещее исключение
# При успешном заходе генерируем исключение "Доступ разрешен!"

from abc import ABC, abstractmethod

class Users(ABC):
    @abstractmethod
    def login(self):
        pass

    def check_pasword(self):
        pass

    def check_login(self):
        pass

class User(Users):
    users = {"User":"Password", "Skif":"umbalumba"}
    def login(self, l, p):
        try:
            self.check_login(l) #*
            self.check_pasword(p)#*
            if l in self.users and p == self.users[l]:
                print("Доступ Разрешен")
            else:
                raise LoginError
        except LoginError:
            pass

    def check_pasword(self, p):
        try:
             raise LengthError(len(p))
        except LengthError:
            pass

        

    def check_login(self, login):
        try:
            if not login in self.users:
                raise LoginNotFound
        except LoginNotFound:
            pass

class LengthError(Exception):
    def __init__(self, number):
        if number < 8:
            print(f"В пароле должно быть не менее 8 символов! сейчас: {number}")

class LoginNotFound(Exception):
    def __init__(self):
        print(f"Логин не найден!")

class LoginError(Exception):
    def __init__(self):
        print("Доступ запрещён!")

        


user = User()
while True:
    login = input("Введите логин: ")
    password = input("Введите пароль: ")

    user.login(login, password)
