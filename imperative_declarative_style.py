"""
Контекст
Предположим, что нам хочется для любого массива чисел array и любого числа target узнать содержится
ли target в array. Такую процедуру будем называть поиском.
Задача
Реализовать императивную функцию поиска элементов на языке Python.

"""
import random

# def imperative_search_target(array, target):
#     for el in array:
#         if el == target:
#             return True
#     return False
#
# print(imperative_search_target([1,2,3,4,5], 6))

# Задача
# Реализовать декларативную функцию поиска элементов на языке Python

# def declarative_search(array, target):
#     return target in array
#
# print(declarative_search([1,2,3,4,5], 1))

"""
 Условие
На вход подается: список целых чисел arr
● Задача
Реализовать императивную функцию, которая возвращает три числа:
○ Долю позитивных чисел
○ Долю нулей
○ Долю отрицательных чисел
"""

# def imperative_numbers_share(arr):
#     count_positive = 0
#     count_zeros = 0
#     count_negative = 0
#     for el in arr:
#         if el > 0:
#             count_positive += 1
#         elif el == 0:
#             count_zeros += 1
#         else:
#             count_negative += 1
#     positives = count_positive / len(arr)
#     zeros = count_zeros / len(arr)
#     negatives = count_negative / len(arr)
#     return positives, zeros, negatives
#
#
# print(imperative_numbers_share([-1, 2, -3, 4, 0, 5, 0, -6, 7, 9]))
#
#
# #  Доля чисел: декларативный вариант
#
# def declarative_numbers_share(arr):
#     pos_cnt = len(list(filter(lambda x: x > 0, arr)))
#     neg_cnt = len(list(filter(lambda x: x < 0, arr)))
#     zeros_cnt = len(list(filter(lambda x: x == 0, arr)))
#     counters = [pos_cnt, zeros_cnt, neg_cnt]
#     shares = list(map(lambda x: x / len(arr), counters))
#     return shares
#
# print(declarative_numbers_share([-1, 2, -3, 4, 0, 5, 0, -6, 7, 9]))

"""
Задача №1
Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.
"""
random_arr = list(random.randint(0, 100) for _ in range(42))
print(random_arr)


def sort_list_imperative(numbers):
    for i in range(0, len(numbers)):
        min_position = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] > numbers[min_position]:
                min_position = j
        if min_position != i:
            temp = numbers[i]
            numbers[i] = numbers[min_position]
            numbers[min_position] = temp

    return numbers


print(sort_list_imperative(random_arr))

"""
Задача №2
Написать точно такую же процедуру, но в декларативном стиле"""


def sort_list_declarative(numbers):
    return sorted(numbers, reverse=True)


def sort_list_declarative_v2(numbers):
    numbers.sort(reverse=True)
    return numbers


print(sort_list_declarative(random_arr))
print(sort_list_declarative_v2(random_arr))
