# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

num_1 = input("Input nomber: ")
print(int(num_1 * 3) + int(num_1 * 2) + int(num_1))
