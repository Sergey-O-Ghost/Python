# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма.
# Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки.
# Выведите соответствующее сообщение.

# 6. Если фирма отработала с прибылью, вычислите рентабельность выручки.
# Это отношение прибыли к выручке. Далее запросите численность сотрудников фирмы
# и определите прибыль фирмы в расчёте на одного сотрудника.

num_vir = int(input("Input viruchka: "))
num_izd = int(input("Input izderzki: "))
if num_vir > num_izd:
    num_rent = ((num_vir - num_izd) * 100) // num_izd
    print("Congratulations, vir > izd. Rent = ", num_rent, "%")
    num_sot = int(input("Input count of workers: "))
    print("Vir/worker = ", (num_vir - num_izd) // num_sot)

else:
    print("Sorry, izd > vir")
