# 5. Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделённых пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.


my_str = None   # Обозначим переменную

try:                                        # Проверим, существует ли файл
    with open('task_5.txt') as my_file:     # Если существует...
        pass                                # ... то ничего не делаем
except FileNotFoundError:                   # Если файла нет...
    with open('task_5.txt', mode="w"):      # ... создадим его...
        pass                                # ... но записывать в него пока ничего не будем

with open('task_5.txt') as task_5:          # Посчитаем строки в файле (для добавления перевода строки)
    if len(task_5.readlines()) == 0:        # Если файл пустой...
        new_file = True                     # ... установим переменную в значение "Истина"
    else:                                   # Если файл не пустой...
        new_file = False                    # ... то значение будет "Ложь"

while my_str != "":     # Пока пользователь не введёт пустую строку, будем считывать строки:
    my_str = input("Input string to write in the file, ""--clear"" for clear the file or empty string to exit: ")
    if my_str == "--clear":                             # если ввели специальное слово...
        with open('task_5.txt', mode='w') as task_5:    # ... очистим файл...
            new_file = True                             # ... и установим флаг "new_file" в значение "Истина"
    else:                                               # в ином случае запишем строку в файл:
        if new_file:                                        # если файл новый, то просто запишем строку...
            with open('task_5.txt', mode='a') as task_5:
                task_5.write(my_str)
            new_file = False                                # ... и снимем флаг
        else:                                               # Если файл не новый...
            with open('task_5.txt', mode='a') as task_5:
                task_5.write('\n' + my_str)                 # ... то допишем строку после перевода строки
        my_list = my_str.split()                        # разделяем строку на список значений...
        my_sum = 0                                      # обнуляем общую сумму
        my_exc = 0                                      # и счётчик исключений
        for ind in range(0, len(my_list)):              # проверяем все значения списка
            try:
                my_num = float(my_list[ind])            # Если значение числовое...
                my_sum += my_num                        # Добавим к общей сумме
            except ValueError:                          # Если не числовое...
                my_exc += 1                             # ... увеличим счётчик исключений
        if len(my_list) > 0:                            # Если строка не пустая, выводим результат...
            print(f'Summ of {len(my_list) - my_exc} numbers is {my_sum}')

print('\n', "Output file:", '\n')       # Сообщим, что будет выведен весь файл...

with open('task_5.txt') as task_5:      # ... и выведем его
    print(task_5.read())
