# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.

my_list_win = [1, 2, 12]
my_list_spr = [3, 4, 5]
my_list_sum = [6, 7, 8]
my_list_aut = [9, 10, 11]
my_list_year = ["Winter", "Winter", "Spring", "Spring", "Spring", "Summer",
                "Summer", "Summer", "Authumn", "Authumn", "Authumn", "Winter"]
my_dict_1 = {
    1: "Winter",
    2: "Winter",
    3: "Spring",
    4: "Spring",
    5: "Spring",
    6: "Summer",
    7: "Summer",
    8: "Summer",
    9: "Authumn",
    10: "Authumn",
    11: "Authumn",
    12: "Winter"
}
my_mou = 0
while type(my_mou) == int:
    my_mou = input("Input number of mounth, or 'e' for exit: ")
    if my_mou.isnumeric():
        if (abs(int(my_mou)) > 0) and (abs(int(my_mou)) < 13):
            my_mou = int(my_mou)
            if my_mou in my_list_aut:
                print("Through list 1: Authumn")
            if my_mou in my_list_sum:
                print("Through list 1: Summer")
            if my_mou in my_list_spr:
                print("Through list 1: Spring")
            if my_mou in my_list_win:
                print("Through list 1: Winter")
            print(f'Through list 2: {my_list_year[my_mou - 1]}')
            print(f'Through dict: {my_dict_1[my_mou]}')
        else:
            my_mou = 1
    elif my_mou != "e":
        my_mou = 1
