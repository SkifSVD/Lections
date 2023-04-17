# Написать игру "Поле чудес"

#Отгадываемые слова и описание лежат в разных  массивах по одинаковому индексу.
#words = ["оператор", "конструкция", "объект"]
#desc_  = [ "Это слово обозначает наименьшую автономную часть языка программирования", "..", ".." ]
#Пользователю выводится определение слова и количество букв в виде шаблона. Стиль шаблона может быть любым.
#Слово из массива берется случайным порядком. Принимая из ввода букву мы ее открываем
#в случае успеха а в случае неуспеха насчитывам штрафные балы. Игра продолжается до 10 штрафных баллов
#либо победы.

#Пример вывода:

#"Это слово обозначает наименьшую автономную часть языка программирования"

#▒  ▒  ▒  ▒  ▒  ▒  ▒  ▒

#Введите букву: O

#O  ▒  ▒  ▒  ▒  ▒  O  ▒


#Введите букву: Я

#Нет такой буквы.
#У вас осталось 9 попыток !
#Введите букву:
import random


words = ["азбука", "буквы", "словарь"] #Слова для разгадки
desc_ = ["Книга которая учит читать", "Из каких элементов состоит слово", "Сборник слов"] #вопросы

rnd_Choise = random.randint(0, 2)       # Случайный выбор вопроса
err_Score = 0                           # Начальный счетчик ошибок
word_Choise = list(words[rnd_Choise])   # выбранное слово
symbol = '▒'                             # Символ для неизвестных букв
word_Type = []

chanses = 3

print(desc_[rnd_Choise])            #Вывод вопроса

while err_Score <= chanses:
    score = 0

    for i in word_Choise:
        marker = 0

        for j in word_Type:
            if i == j:
                score += 1
                marker += 1
                print(j, end = " ")
        if marker == 0:
            print(symbol, end = " ")


    t = input("\n\nВведите букву: ")
    print("\n\n")
    
    timer = 0
    for i in word_Choise:# Цикл прохода по буквам слова
        timer += 1
        if t == i:              # Сравнение введённого символа с символами в слове
            tmp = 0             # временное значение для исключения повторения символов
            for j in word_Type: # Проверка на совпадения, для избежания повторного добавления символов
                if t == j:
                    tmp += 1

            if tmp == 0:        # Если символ ранее не вводился и присутствует в эталонном слове то добавляем в список отгаданных символов
                word_Type.append(t)
                          # Увиличиваем счётчик отгаданных символов
            else:
                err_Score += 1
        elif not t == i and timer == len(word_Choise):
            err_Score += 1

            

    if err_Score > 0:
        if err_Score == chanses:
            print("Game Over")
            break
    elif score == len(word_Choise) - 1:
        print(word_Choise, "\n\nВы выиграли!")
        break
    else:
        continue

        
