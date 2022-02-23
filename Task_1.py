# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы
# сотрудника. Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
# Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.


from sys import argv as arg


# Выводим входные данные с расшифровкой
print('\n'f'Выработка: {arg[1]} ч.')
print(f'Ставка: {arg[2]} ₽/ч')
print(f'Премия: {arg[3]} %')
zp = float(arg[1]) * float(arg[2]) * (float(arg[3]) / 100 + 1)  # Вычисляем ЗП
print('\n'f'Заработная плата составила {zp}₽''\n')              # Выводим ответ
