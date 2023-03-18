"""
2. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль (try except).

Пример:
Введите первое число: 10
Введите второе число: 0
Вы что? Пытаетесь делить на 0!
"""
def division(first_value, second_value):
    return first_value / second_value

try:
    first_value = int(input('Введите первое число: '))
    second_value = int(input('Введите второе число: '))
    result = division(first_value, second_value)
except ValueError:
    print('Введено не число!')
except ZeroDivisionError:
    print('Деление на 0 не допустимо!')
else:
    print(f'Результат деления: {result}')