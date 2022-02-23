# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма.
# Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки.
# Выведите соответствующее сообщение.

num_vir = int(input("Input viruchka: "))
num_izd = int(input("Input izderzki: "))
if num_vir > num_izd:
    print("Congratulations, vir > izd")
else:
    print("Sorry, izd > vir")
