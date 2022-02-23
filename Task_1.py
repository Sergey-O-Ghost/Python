def my_div(arg_1, arg_2):
    if arg_2 == 0:  # Проверяем, делим ли на ноль
        if arg_1 == 0:  # Провряем, что делим на ноль
            res = "Indeterminancy (0/0)!"  # Если 0/0, то записываем в результат неопределённость
        else:
            res = "Infinity (division by zero)!"  # Если число делим на ноль, то записываем в тезультат бесконечость
    else:  # Если делим не на ноль, то вычисляем результат
        res = arg_1 / arg_2
    return res  # возвращаем результат


# Обозначим две переменные типа "строка":
my_divisible = ""
my_divisor = ""
# Запрашиваем делимое, пока не будет введено число:
while type(my_divisible) == str:
    my_divisible = input("Input the divisible: ")  # забираем у пользователя данные
    try:
        my_divisible = float(my_divisible)  # Если ввели число, то преобразуем данные в число
    except ValueError:
        my_divisible = ""
# Запрашиваем делитель, пока не будет введено число:
while type(my_divisor) == str:
    my_divisor = input("Input the divisor: ")
    try:
        my_divisor = float(my_divisor)
    except ValueError:
        my_divisor = ""

print("Division result: ", my_div(my_divisible, my_divisor))
