"""
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках
записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*
5
    1 2 3 4 5
    6
    -> 5
"""


def get_array():
    count_number = int(input('Введите размер массива: '))
    numbers = []
    for i in range(count_number):
        numbers.append(int(input(f'Введите элемент массива № {i + 1}: ')))

    return numbers


def get_min_diff_number(n, exp_list):
    min_different = abs(n - exp_list[0])
    min_different_number = exp_list[0]
    for item in exp_list:
        if min_different > abs(n - item):
            min_different = abs(n - item)
            min_different_number = item

    return min_different_number


try:
    numbers = get_array()
    n = int(input('Введите искомое число: '))
except ValueError:
    print('Введено не число!')
else:
    print(f'Самый близкий элемент к искомому: {get_min_diff_number(n, numbers)}')
