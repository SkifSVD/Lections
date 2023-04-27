#todo:
# Каждый третий четверг каждого месяца билеты в Эрмитаж бесплатны. Напечатайте список дат в 2023 году, когда вход бесплатен.

from calendar import monthrange
import datetime

def lst_date(yr):
    for i in range(1, 13):
        t = monthrange(yr, i)
        tmp = 0
        for j in range(1, t[1]+1):
            
            if (datetime.date(yr, i, j)).weekday() == 3:
                tmp += 1
                if tmp%3 == 0:
                    tmp = 0
                    print((datetime.date(yr, i, j)).strftime('%Y.%m.%d'))


year = 2023
lst = {}
lst_date(year)