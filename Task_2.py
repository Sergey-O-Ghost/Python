# 2. Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().

my_list1 = []
my_list2 = []
my_index_1 = 0
my_ask = "y"

while my_ask != "n":
    my_list1.append(input("Input element: "))
    print(my_list1)
    my_ask = input("Add next element? (y/n): y ")
    if my_ask == "":
        my_ask = "y"
    while not((my_ask == "y") or (my_ask == "n")):
        my_ask = input("Add next element? (y/n): y ")
        if my_ask == "":
            my_ask = "y"

num_1 = (len(my_list1)) // 2

for num_2 in range(1, num_1 + 1):
    # print(my_list1[num_2 * 2 - 1:2:-1])
    my_list2.append(my_list1[num_2 * 2 - 1])
    my_list2.append(my_list1[num_2 * 2 - 2])
    # print(f'Num_2 = {num_2}')

if len(my_list1) % 2:
    my_list2.append(my_list1[-1])

print("", my_list1, my_list2, sep='\n')
