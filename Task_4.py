# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки нужно пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.

my_str_1 = input("Input string: ")
my_list = my_str_1.split()
for my_num in range(0, len(my_list)):
    my_str_2 = my_list[my_num][:10]
    print(f'{my_num + 1}. {my_str_2}')
