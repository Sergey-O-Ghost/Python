# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

num_sec = int(input("Input time in sec: "))
num_th = num_sec // 3600
num_tm = (num_sec - (num_th * 3600)) // 60
num_ts = num_sec % 60
print(f'{num_th}:{num_tm}:{num_ts}')
