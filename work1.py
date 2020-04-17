#   Задание:
#   (Задачу решить без применения сторонних библиотек.
#   (Наличие тестов и отчёта покрытия кода приветствуется.)


# 1. Из списка длинной n случайным образом выбрать k элементов без повторений. Предложить наиболее оптимальный вариант по времени и по ресурсам.
 
#  РЕШЕНИЕ:
#  Стоит отметить, что для решения задачи не следует использовать многопроцессорность и многопотчоность
#  по причине затрат времени на перехват мьютесков (при многопоточности) и количества выделяемой памяти (при многопроцессорности).

import random
import sys
import time
import datetime

my_list = [
        random.randint(1,11), random.randint(1,11), random.randint(1,11),
        random.randint(1,11), random.randint(1,11), random.randint(1,11),
        random.randint(1,11), random.randint(1,11), random.randint(1,11),
        random.randint(1,11), random.randint(1,11), random.randint(1,11),
        ]

print('Сформированный список:', my_list)
print('----' * 15)

# Решение 1
start = time.time()       
values_1 = list(set(my_list))
finish = time.time()
result = finish - start
result_2 = sys.getsizeof(values_1)
print('Полученный список:', values_1)   # Покажем работоспособность кода  
print('Скорость выполнения решения 1:', result)
print('Количество выделеной памяти для решения 1:', str(result_2) + ' bytes')
print('----' * 15)

# Решение 2
def func():            # Покажем работоспособность кода  
    values_2 = []
    for n in my_list:
        if n not in values_2:
            values_2.append(n)
    print('Полученный список:', values_2) 
func()

def test_1(n):         # Декоратор для проверки скорости выполнения
    start = time.time()
    n()
    finish = time.time()
    result = finish - start
    print('Скорость выполнения решения 2:', result)    
    return n

@test_1
def func():            # Проверка насисанного кода декоратором test_1
    values_2 = []
    for n in my_list:
        if n not in values_2:
            values_2.append(n)  
func()

def test_2(n):         # Декоратор для проверки количества выделеной памяти
    result_2 = sys.getsizeof(n)
    print('Количество выделеной памяти для решения 2:', str(result_2) + ' bytes')
    return n

@test_2                # Проверка насисанного кода декоратором test_2
def func():
    values_2 = []
    for n in my_list:
        if n not in values_2:
            values_2.append(n)       
func()
print('----' * 15)
# ОТВЕТ: оптимальным вариантом по времени и по ресурсам является вариант 1.

