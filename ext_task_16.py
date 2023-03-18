"""
Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой
строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai.
Последняя строка содержит число X
*Пример:*

5
    1 2 3 4 5
    3
    -> 1
"""


def get_array():
    count_number = int(input('Введите размер массива: '))
    numbers = []
    for i in range(count_number):
        numbers.append(int(input(f'Введите элемент массива № {i + 1}: ')))

    return numbers


def get_count_number(n, exp_list):
    count_number = 0
    for i in exp_list:
        if n == i:
            count_number += 1

    return count_number


try:
    numbers = get_array()
    n = int(input('Введите искомое число: '))
except ValueError:
    print('Введено не число!')
else:
    count_number = get_count_number(n, numbers)
    print(f'Количество вхождений числа {n} = {count_number} (самописный метод)')
    print(f'Количество вхождений числа {n} = {numbers.count(n)} (встроенный метод)')
