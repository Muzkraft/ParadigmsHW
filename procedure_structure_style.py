# def quicksort(arr):
#     if len(arr) <= 1:
#         return arr
#     else:
#         base = arr[0]
#         less = [x for x in arr[1:] if x <= base]
#         greater = [x for x in arr[1:] if x > base]
#         return quicksort(less) + [base] + quicksort(greater)
#
#
# numbers = [1, 2, 5, 7, 9, 6, 4, 8, 23, 3, 4]
# sorted_numbers = quicksort(numbers)
# print(sorted_numbers)

"""
● Контекст
След матрицы - это сумма чисел на её главной диагонали. След определён только для квадратных матриц
(количество столбцов = количеству строк).
● Задача
Реализовать чисто структурную реализацию вычисления следа для любой матрицы NxN.

"""
# matrix = [[1,2,3,],
#           [4,5,6,],
#           [7,8,9,]]
# trace = 0
# for i, row in enumerate(matrix):
#     for j, el in enumerate(row):
#         if i == j:
#             trace += el
#
# print(trace)
#
# # Задача
# # Добавить процедурную парадигму в имеющуюся реализацию вычисления следа.
# def get_trace(matrix):
#     trace = 0
#     for i, row in enumerate(matrix):
#         for j, el in enumerate(row):
#             if i == j:
#                 trace += el
#     return trace
#
# print(trace)

"""
 Условие
На вход подается число в десятичной системе счисления
● Задача
Написать скрипт в любой парадигме, который возвращает полученное число переведенное в двоичную
систему счисления. Обоснуйте сделанный выбор парадигм.
"""

# number = int(input('Введите число: '))
#
# def decimal_to_binary(decimal):
#     binary = ""
#     while decimal > 0:
#         binary = str(decimal % 2) + binary
#         decimal = decimal // 2
#     return binary
#
# print(f"{number} = {decimal_to_binary(number)}")

"""
Таблица умножения
Домашнее задание
● Условие
На вход подается число n.
● Задача
Написать скрипт в любой парадигме, который выводит на экран таблицу умножения всех чисел от 1 до n.
Обоснуйте выбор парадигм.
● Пример вывода:
1 * 1 = 1
1 * 2 = 2
1 * 3 = 3
1 * 4 = 4
1 * 5 = 5
1 * 6 = 6
..
1 * 9 = 9
"""
number = int(input("Введите число: "))

for i in range(1, number + 1):
    for j in range(1, 10):
        print(f'{i} * {j} = {i*j}')
    print()

"""
Я выбрал императивный, структурный стиль, т.к. задачу быстрей и проще решить именно так. Так же здесь нет необходимости
улучшать читаемость, производительность кода, или переиспользовать его, поэтому использование,
например функционального или декларативного способа нецелесообразно"""