# 6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв
# и возвращающую их же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
#
# 7. Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Нужно сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы. Используйте написанную ранее функцию int_func().

def int_func(arg_1):
    res = arg_1[0].upper() + arg_1[1:]  # Применяем к первому символу функцию .upper
    # и добавляем остальные без изменений
    return res  # Возвращаем результат


# Устанавливаем переменнную ответа
my_ans = "y"
while my_ans == "y":
    my_str_out = ""
    my_str = input("\nInput string: ")                # Запрашиваем строку
    my_list = my_str.split()                        # Формируем из строки список слов
    for my_num in range(0, len(my_list)):           # Будем обрабатывать каждый элемент списка
        my_str_out += int_func(my_list[my_num])     # Дописываем обработанное слово в конец итоговой строки
        if my_num != len(my_list) - 1:              # Если текущее слово не последнее...
            my_str_out += " "                       # ... добавляем пробел

    print(my_str_out, '\n')                               # Выводим обработанное значение
    my_ans = ""                                     # Сбрасываем переменную ответа
    while (my_ans != "y") and (my_ans != "n"):          # Ожидаем корректный ответ
        my_ans = input("Input another string? (y/n) y")   # Выдаём запрос на продолжение
        if my_ans == "":                                # Пустой ответ...
            my_ans = "y"                                # ... считаем положительным
