#todo: Напишите функцию, которая шифрует строку, содержащую латинские буквы с помощью шифра Цезаря. Каждая буква сдвигается на заданное число n позиций вправо. Пробелы, знаки препинания не меняются. Например, для n = 1.
# a → b,   b → c,    p → q,    y → z,    z V a
# A → B,   B → C,   Z → A
# Т.е. заголовок функции будет def code(string, n):
# В качестве результата печатается сдвинутая строка.

def code(string, n):
    a = ['a', 'b', 'c', 'd', 'e',
         'f', 'g', 'h', 'i', 'k',
         'l', 'm', 'n', 'o', 'p',
         'q', 'r', 's', 't', 'v',
         'x', 'y', 'z', 'A', 'B',
         'C', 'D', 'E', 'F', 'G',
         'H', 'I', 'K', 'L', 'M',
         'N', 'O', 'P', 'Q', 'R',
         'S', 'T', 'V', 'X', 'Y',
         'Z']
    stg = []

    for symbol in string:
        i = 0
        for etal in a:
            if symbol == etal:
                i += n
                if i > 22:
                    i -= 23
                elif i > 45:
                    i -= 23
                stg.append(a[i])
                break
            else:
                i += 1
        if i == 46:
            stg.append(symbol)

    return stg
    
n = int(input("Введите велечину сдвига: "))
txt = input("Введите строку: ")


for i in code(txt, n):  
    print(end = i)

print("\n")

