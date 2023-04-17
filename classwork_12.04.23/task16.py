#todo: На вход подается предложение из нескольких слов. Слова разделены пробелами.
# Напечатайте самое длинное слово в этом предложении. 

txt = input("Введите несколько слов через пробел: ")

lst =  txt.split()

index = 0
size = 0
for word in lst:
    if len(word) > size:
        size = len(word)
        index = lst.index(word)


print(lst[index])