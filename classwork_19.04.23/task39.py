#todo 1: создайте модуль serializer

# В модуле реализуйте три функции сериализации

# Функция сериализует объект в байтовый поток pickle
# Параметры
# obj - сериализуемый объект
# file - файл для сериализации к примеру "data.pkl"
import pickle

from datetime import datetime

def get_time():
    return datetime.now().strftime('%d.%m.%Y %H:%M:%S')

def to_pickle(obj, file):
    fn = file + '.pkl'
    fdump = open(fn, 'wb')
    pickle.dump(obj, fdump, pickle.HIGHEST_PROTOCOL)
    fdump.close()
    #pass
    # ваш код

#  Функция сериализует объект в json
#  Параметры
# obj - сериализуемый объект
# file - файл для сериализации к примеру "data.json"
def to_json(obj, file):
    fn = file + '.json'
    fdump = open(fn, 'wb')
    pickle.dump(obj, fdump, pickle.HIGHEST_PROTOCOL)
    fdump.close()
    pass
    # ваш код

# Функция сериализует объект в yaml
# Параметры
# obj - сериализуемый объект
# file - файл для сериализации к примеру "data.yml"
def to_yaml(obj, file):
    fn = file + '.yaml'
    fdump = open(fn, 'wb')
    pickle.dump(obj, fdump, pickle.HIGHEST_PROTOCOL)
    fdump.close()
    pass
    # ваш код




#todo 2: Cоздайте модуль deserializer. В модуле реализуйте три функции десериализации


# Функция десериализует объект из файла типа pickle
# file - файл для десериализации к примеру "data.pkl"
def from_pickle(file):
    f = file + '.pkl'
    fdump = open(f, 'rb')
    with open(f, 'rb') as file:
        obj_read = pickle.load(file)

    print(obj_read)
    fdump.close()
    pass
    # ваш код

# Функция десериализует объект из файла типа json
# from_json - функция сереализует объект в json
# Параметры
# file - файл для десериализации к примеру "data.json"
def from_json(file):
    f = file + '.json'
    fdump = open(f, 'rb')
    with open(f, 'rb') as file:
        obj_read = pickle.load(file)

    print(obj_read)
    fdump.close()
    pass
    # ваш код


# Функция десериализует объект из файла типа yaml
# Параметры
# file - файл для десериализации к примеру "data.yml"
def from_yaml(file):
    f = file + '.yaml'
    fdump = open(f, 'rb')
    with open(f, 'rb') as file:
        obj_read = pickle.load(file)

    print(obj_read)
    fdump.close()
    pass
    # ваш код

#todo 3: Cоздайте пакет из двух модулей serializer и deserializer.

# Импортируйте модули пакета в отдельный файл и протестируйте все функции.

filename = 'data'

obj = "\n"

for i in range(1, 5):
    obj += f'{get_time()}\n'

to_pickle(obj, filename)
from_pickle(filename)

to_json(obj, filename)
from_json(filename)

to_yaml(obj, filename)
from_yaml(filename)
