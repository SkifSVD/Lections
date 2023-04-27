#todo: Заданы два списка. Необходимо их сериализовать в один файл.
import pickle
list_one = [True, 'If the implementation is hard to explain, it\'s a bad idea.', {'age': 27}]
list_two = [False, 'Sparse is better than dense.', {'age': 90}]

filename = "tst.json"
obj = [list_one, list_two]
fdump = open(filename, 'wb')
pickle.dump(obj, fdump, pickle.HIGHEST_PROTOCOL)
fdump.close()

with open(filename, 'rb') as f:
    obj_read = pickle.load(f)

for i in range(len(obj_read)):
    print(obj_read[i])
