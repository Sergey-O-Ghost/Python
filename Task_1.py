# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

mylist_1 = [122, 15.5, "Hello, IT!", ["Windows", "Must", "Die"], 0b111000111, 0o11, 0xb0b]
my_in = 1
while type(my_in) == int:
    my_in = input("Input number from 1 to 7, or 'e' for exit: ")
    if my_in.isnumeric():
        if (abs(int(my_in)) > 0) and (abs(int(my_in)) < 8):
            print(mylist_1[int(my_in) - 1])
            my_in = int(my_in)
    elif my_in != "e":
        my_in = 1
