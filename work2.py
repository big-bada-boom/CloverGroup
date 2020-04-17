# 2.    Есть массив данных типа:
#       time value
#       2016-11-03 11:13:30        23
#       2016-11-03 11:13:31        13
#       2016-11-03 11:13:32        15
#       ...

#       Интервал - 1 секунда. Массив может быть сколь угодно длинным.
#       a) Получить новый массив, для которого необходимо посчитать статистические данные по 100 секундному окну для каждого значения начальных данных
#          статистическими параметры: среднее, медиана, максимум, минимум
#       б) Решить задачу из предыдущего пункта с учетом группировки данных за день

#  РЕШЕНИЕ:
# 1) Для получения нового массива необходимо написать объект - итератор.
# 2) Итератор должен генерировать объекты 100 секунд (для правильного подсчета статических данных)
# 3) Для проверки пункта б итератор должен возвращать элементы с разной датой.

import random
import time
import datetime
from itertools import groupby

date_time = datetime.datetime(                                 # получим дату с учетом текущей локали
                                year=2016, 
                                month=random.randint(1,12), 
                                day=3).strftime("%d-%m-%Y"
                            )    
now = datetime.datetime.now().strftime("%H:%M:%S")
for_items = date_time +' ' + now                               # создаем объект с разной датой 
value = random.randint(1, 30)                                  # получим случайное значение
items = [for_items, value]                                     # создадим одномерный массив

class Iterator():           # напишем класс - итератор для создания сколь угодно длинного массива.
    def __init__(self, x):  # x - время(с) генерации массива.
        self.x = x

    def __iter__(self):
        self.__n  = 0
        return self
    
    def __next__(self):
        time.sleep(1)
        self.__n += 1
        if self.__n > self.x - 1:
            raise StopIteration
        else:
            date_time = datetime.datetime(                                 # получим дату с учетом текущей локали
                                            year=2016, 
                                            month=11, 
                                            day=random.randint(1,4)).strftime("%d-%m-%Y"
                                        )                                  
            now = datetime.datetime.now().strftime("%H:%M:%S")
            for_items = date_time +' ' + now                               # создаем объект с разной датой 
            value = random.randint(1, 30)                                  # получим случайное значение
            self.items = [for_items, value]                                # создадим одномерный массив
            return self.items
    
my_iter = Iterator(100)     # создадим экземпляр класса с 100 секундным окном
my_iter = iter(my_iter)     # создадим итератор 

my_list = []                # создадим пустой список для занесения данных 
for n in my_iter:
    print('заносим значения ' + str(n) + ' в список my_list с интервалом в 1 сек.')
    my_list.append(n)

def average_value(n):       # создадим функцию для определения среднего значения
    item = 0
    for x in n:
        item += x[1]
    item = item / len(n)
    print('Среднее значение:',item)

def median(n):              # создадим функцию для определения медианы
    list_for_median = []
    for x in n:
        list_for_median.append(x[1])
    sortedLst = sorted(list_for_median)
    lstLen = len(list_for_median)
    index = (lstLen - 1) // 2
    if (lstLen % 2):
        print('Медиана:',sortedLst[index])
    else:
        print('Медиана:',((sortedLst[index] + sortedLst[index + 1]) / 2.0))

def min_f(n):                # создадим функцию для определения минимального значения                 
    list_for_min = []
    for x in n:
        list_for_min.append(x[1])
    list_for_min = sorted(list_for_min)
    print('Минимальное значение:',list_for_min[0])

def max_f(n):                # создадим функцию для определения максимального значения
    list_for_max = []
    for x in n:
        list_for_max.append(x[1])
    list_for_max = sorted(list_for_max)
    print('Максимальное значение:',list_for_max[-1])


print(my_list)  
print('----' * 20)          
average_value(my_list)
median(my_list)
min_f(my_list)
max_f(my_list)
print('----' * 20)

def group(n):                # решим задачу из предыдущего пункта с учетом группировки данных за день
    l = []
    for g in groupby(sorted(n,key=lambda x:x[0][0:10]) ,key=lambda x:x[0][0:10]):
        n = [g[0], 0]
        for i in g[1]:
            n[1] += i[1]
        l.append(n)
    return(l)

group_list = group(my_list)  # группируем данные
print(group_list)

print('----' * 20)
average_value(group_list)
median(group_list)
min_f(group_list)
max_f(group_list)
print('----' * 20)