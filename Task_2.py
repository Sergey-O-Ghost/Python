# 2. Выполнить функцию, которая принимает несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.

def printkard(firstname, lastname, by, city, mail, phone):
    print(f'{firstname} {lastname}, {by} year of birth, from {city}, e-mail: {mail}, phone: {phone}')


my_name = input("Input you first name: ")
my_family = input("Input you last name: ")
my_year = input("Input you year of birth: ")
my_city = input("Input you city from: ")
my_mail = input("Input you e-mail address: ")
my_phone = input("Input you phone: ")

printkard(firstname=my_name, lastname=my_family, by=my_year, city=my_city, mail=my_mail, phone=my_phone)
