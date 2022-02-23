# 6. Реализовать два небольших скрипта:
#
# итератор, генерирующий целые числа, начиная с указанного;
#
# итератор, повторяющий элементы некоторого списка, определённого заранее.
#
# Подсказка: используйте функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Предусмотрите условие его завершения. #### Например, в первом задании выводим
# целые числа, начиная с 3. При достижении числа 10 — завершаем цикл.
# Вторым пунктом необходимо предусмотреть условие, при котором повторение элементов списка прекратится.


# Импортируем функции из модулей:

from itertools import count as iterco, cycle as itercy
from sys import argv as arg
from random import random


def rnd():      # Определяем функцию, которая будет возвращать числа от 0 до 1000
    res = round(random() * 1000)
    return res

# Собственные функции, аналогичные функциям из модуля itertools (Не сразу прочитал подсказку)
#
# def iterco(arg_1):
#     global my_ans
#     res = arg_1
#     while my_ans == "y":
#         yield res
#         res += 1
#
# def itercy(arg_1):
#     global my_ans
#     fun_counter = 0
#     while my_ans == "y":
#         res = arg_1[fun_counter]
#         yield res
#         if fun_counter == (len(arg_1) - 1):
#             fun_counter = 0
#         else:
#             fun_counter += 1


# Определим переменные:
my_count = 1
my_len = 0
my_ans = "y"
my_start = ""

print()
try:                    # Проверим на наличие первый аргумент
    my_start = arg[1]   # Если он на месте - запишем его в переменную начала отсчёта
except IndexError:      # Если его не ввели - попросим ввести
    my_start = input("Start number not input! Enter start number:")

while type(my_start) == str:    # В этом цикле будем добиваться целого значения начала отсчёта
    try:                        # Проверяем, является ли переменная целым числом
        my_start = int(my_start)
    except ValueError:          # Если нет - просим ввести заново
        my_start = input("Input number is not a integer! Enter a integer number: ")

try:                        # Проверим второй аргумент
    my_len = int(arg[2])    # Пробуем записать значение в переменную длинны списка, как целое число
except IndexError:          # Если аргумент не ввели - сообщим об этом...
    print("Lenght not input! Lenght of list set in default value - 10 elements")
    my_len = 10             # ... и установим размер списка - 10 элементов
except ValueError:          # Если аргумент ввели, но это не целое число, сообщим об этом...
    print("Lenght not is integer! Lenght of list set in default value - 10 elements")
    my_len = 10             # ... и также установим размер списка - 10 элементов

my_list_1 = [rnd() for my_count in range(0, my_len)]    # Генерируем список заданной длинны

my_num_1 = iterco(my_start)     # Создадим итератор для первой последовательности
my_num_2 = itercy(my_list_1)    # Создадим итератор для второй последовательности
while my_ans == "y":            # Завершение работы итератора определяет пользователь
    print(f'Start number: {my_start}')              # Выводим начальное значение для первого итератора
    print(f'Iterable list: {my_list_1}')            # Выводим список, созданный для второго итератора
    print(f'Current step number: {my_count}''\n')   # Выводим номер шага (для контроля)
    # Выводим текущие значения обоих итераторов
    print(f'Values of iterators: {next(my_num_1)} and {next(my_num_2)}''\n')
    my_ans = ""     # Далее идёт запрос, нужно ли выводить следующее значение
    while (my_ans != "y") and (my_ans != "n"):  # работа завершается, если ввести "n"
        my_ans = input("Would you like to continue? (y/n) y")
        if my_ans == "":                        # если ввели "y" или ничего - выводим следующие значения
            my_ans = "y"
    my_count += 1
