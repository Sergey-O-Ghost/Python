# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

str_1 = input("Input number: ")
num_1 = 0
num_2 = 0
while (num_1 < len(str_1)) and (num_2 != 9):
    if int(str_1[num_1]) > num_2:
        num_2 = int(str_1[num_1])
    print(num_1, int(str_1[num_1]))
    num_1 += 1
print()
print("Biggest num =", num_2)
