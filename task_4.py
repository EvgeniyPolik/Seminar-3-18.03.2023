"""
4. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""
def my_func_with_sort(*args):
    list_args = list(args)
    list_args.sort()
    return list_args[-1] + list_args[-2]

def my_func_without_sort(*args):
    max_value_index = 0
    for i in range(len(args)):
        if args[i] > args[max_value_index]:
            max_value_index = i
    if max_value_index != 0:
        premax_value_index = 0
    else:
        premax_value_index = 1
    for i in range(len(args)):
        if args[i] > args[premax_value_index] and i != max_value_index:
            premax_value_index = i
    return args[max_value_index] + args[premax_value_index]

list_numbers = [4, 3, 5]
print(f'Результат с сортировкой: {my_func_with_sort(*list_numbers)}')
print(f'Результат без сортировки: {my_func_without_sort(*list_numbers)}')
