# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.


with open('task_1.txt') as my_file:     # Возьмём файл из задания №1
    my_list = my_file.readlines()       # Выгрузим строки в список
    numb_str = len(my_list)             # Посчитаем число строк
    print(f'There are {numb_str} lines in the file:''\n')   # Выведем, сколько строк было в файле
    for ind in range(0, numb_str):              # Проверим кажлую строку из списка (перебирая индексы)
        my_str = my_list[ind].split()           # разбиваем строку на список слов
        num_word = len(my_str)                  # считаем слова в строке и выводим результат для строки:
        print(f'There are {num_word} words in {ind + 1} string "{my_list[ind][:-1]}"')
