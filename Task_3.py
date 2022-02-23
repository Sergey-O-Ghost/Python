# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента
# и возвращает сумму наибольших двух аргументов.

def my_func(arg_1, arg_2, arg_3):
    if (arg_1 < arg_2) and (arg_1 < arg_3):     # Если первый аргумент меньше остальных
        res = arg_2 + arg_3
    elif (arg_2 < arg_1) and (arg_2 < arg_3):   # Проверяем второй аргумент, если первый не самый маленький
        res = arg_1 + arg_3
    elif arg_1 == arg_2:                        # Если первый и второй аргументы не самые маленькие, но одинаковые...
        if arg_1 > arg_3:                       # ... и больше третьего:
            res = arg_1 * 2
        else:                                   # ... и не больше третьего:
            res = arg_1 + arg_3
    else:                                       # Если первый и второй аргументы не самые маленькие и не одинаковые:
        res = arg_1 + arg_2
    return res                                  # Возвращаем нужную сумму


# Обозначим четыре переменные типа "строка":
my_num_1 = ""
my_num_2 = ""
my_num_3 = ""
my_ans = "y"

while my_ans == "y":
    # Запрашиваем первое число, пока не будет введено число:
    while type(my_num_1) == str:
        my_num_1 = input("Input first number: ")    # забираем у пользователя данные
        try:
            my_num_1 = float(my_num_1)              # Если ввели число, то преобразуем данные в число
        except ValueError:
            my_num_1 = ""

    # Запрашиваем второе число, пока не будет введено число:
    while type(my_num_2) == str:
        my_num_2 = input("Input second number: ")    # забираем у пользователя данные
        try:
            my_num_2 = float(my_num_2)              # Если ввели число, то преобразуем данные в число
        except ValueError:
            my_num_2 = ""

    # Запрашиваем третье число, пока не будет введено число:
    while type(my_num_3) == str:
        my_num_3 = input("Input third number: ")    # забираем у пользователя данные
        try:
            my_num_3 = float(my_num_3)              # Если ввели число, то преобразуем данные в число
        except ValueError:
            my_num_3 = ""

    # Выводим максимальную сумму двух из трёх введённых чисел:
    print(my_func(my_num_1, my_num_2, my_num_3))
    my_num_1 = ""
    my_num_2 = ""
    my_num_3 = ""
    my_ans = ""
    while (my_ans != "y") and (my_ans != "n"):      # Добиваемся ответа, нужно ли повторить процедуру
        my_ans = input("Do you want to retry? (y/n): y")
        if my_ans == "":
            my_ans = "y"
