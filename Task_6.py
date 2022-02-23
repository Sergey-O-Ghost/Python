
# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами,
# то есть характеристиками товара: название, цена, количество, единица измерения.
# Структуру нужно сформировать программно, запросив все данные у пользователя.

# Пример готовой структуры:
#
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
#
# Нужно собрать аналитику о товарах.
# Реализовать словарь, в котором каждый ключ — характеристика товара, например, название.
# Тогда значение — список значений-характеристик, например, список названий товаров.

# Пример:
#
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

my_num = 1
my_ans = "y"
my_dict = {}
my_struct = []
# my_titul = ("product", "price", "quantity", "unit")
while my_ans == "y":
    my_name = input("Input name of product: ")
    my_price = input("Input price of product: ")
    my_quantity = input("Input quantity of product: ")
    my_unit = input("Input unit of product: ")
    my_ans = 0
    while (my_ans != "y") and (my_ans != "n"):
        my_ans = input("Add next product? (y/n) y")
        if my_ans == "":
            my_ans = 'y'
    my_dict = {
        "product": my_name,
        "price": my_price,
        "quantity": my_quantity,
        "unit": my_unit
    }
    my_tup = (my_num, my_dict)
    my_struct.append(my_tup)
    my_num += 1
print('\n', "Structure of data:", '\n')
for my_count in range(0, my_num - 1):
    print(my_struct[my_count])
# print("Exit")
my_titul = my_dict.keys()
my_dict_analytics = {}
# for my_key in my_titul:
#     my_dict_analityc[my_key]: my_dict[]
# print(len(my_struct))
for my_key in my_titul:
    my_dict_analytics[my_key] = []
for my_count in range(0, len(my_struct)):
    # print(my_struct[my_count][1])
    for my_key in my_titul:
        my_dict_analytics[my_key].append(my_struct[my_count][1][my_key])
# print("analytics: ", my_dict_analytics)
my_dict_result = {}
for my_key in my_titul:
    my_dict_result[my_key] = set(my_dict_analytics[my_key])
# Вывод в отдельном цикле, чтобы логически отделить его от этапа сборки словаря:
print('\n', "Analytics of products in sets: ", '\n')
for my_key in my_titul:
    print(f'{my_key} = {my_dict_result[my_key]}')
# Вывод аналитики в виде списка:
print('\n', "Analytics of products in lists: ", '\n')
for my_key in my_titul:
    print(f'{my_key} = {my_dict_analytics[my_key]}')
