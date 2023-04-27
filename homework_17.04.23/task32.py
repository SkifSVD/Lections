#todo: Дан генетический код ДНК (строка, состоящая из букв G, C, T, A)
# Постройте РНК, используя принцип замены букв: G → C, C → G, T → A, A→T.
# Напишите функцию, которая на вход получает ДНК, и возвращает РНК. Например:
#Ввод: GGCTAA
#Вывод: CCGATT


def getRNK(s):
    lst = list(s)

    for i in range(len(lst)):
        if lst[i] == 'G':
            lst[i] = 'C'
        elif lst[i] == 'C':
            lst[i] = 'G'
        elif lst[i] == 'T':
            lst[i] = 'A'
        elif lst[i] == 'A':
            lst[i] = 'T'
        else:
            print("Oops!")
            break

    return lst



dnk = "GGCTAA"

print(f"Ввод: {dnk}")

print(f"Вывод: ", end='')
for i in getRNK(dnk):
    print(i, end='')

print("\n")