"""
3. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""


def print_info(full_name, birth_year, living_adress, e_mail, phone_number):
    print(f'{full_name}, {birth_year} года рождения, проживает: {living_adress}, \nemail: {e_mail}, телефон: {phone_number}')


name = input('Введите имя: ')
year_born = input('Год рождения: ')
adress = input('Адрес: ')
email = input('email: ')
phone = input('Телефон: ')

print_info(full_name=name, living_adress=adress, birth_year=year_born, e_mail=email, phone_number=phone)
