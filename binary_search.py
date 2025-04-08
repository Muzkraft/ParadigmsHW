"""
● Контекст
Предположим, что мы хотим найти элемент в массиве (получить
его индекс). Мы можем это сделать просто перебрав все элементы.
Но что, если массив уже отсортирован? В этом случае можно
использовать бинарный поиск. Принцип прост: сначала берём
элемент находящийся посередине и сравниваем с тем, который мы
хотим найти. Если центральный элемент больше нашего,
рассматриваем массив слева от центрального, а если больше -
справа и повторяем так до тех пор, пока не найдем наш элемент.
● Ваша задача
Написать программу на любом языке в любой парадигме для
бинарного поиска. На вход подаётся целочисленный массив и
число. На выходе - индекс элемента или -1, в случае если искомого
элемента нет в массиве.
"""


def binary_search_iterative(arr, target):
    # Определить границы поиска
    left, right = 0, len(arr) - 1
    while left <= right:
        # Вычислить серединный индекс
        mid = left + (right - left) // 2
        # Если средний элемент является искомым, вернуть его индекс
        if arr[mid] == target:
            return mid
            # Если искомый элемент больше, сузить поиск до правой половины
        elif arr[mid] < target:
            left = mid + 1
            # Если искомый элемент меньше, сузить поиск до левой половины
        else:
            right = mid - 1
            # Вернуть -1, если цель не найдена
    return -1


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 2

# Запустить итеративную функцию
result = binary_search_iterative(arr, target)
if result != -1:
    print(f"Iterative: Искомое находится по индексу: {result}")
else:
    print("Iterative: Искомое не найдено")


def binary_search_recursive(arr, target, left, right):
    # Если границы поиска пересекаются, искомого значения в массиве нет
    if left > right:
        return -1
    # Вычислить серединный индекс
    mid = left + (right - left) // 2
    # Если серединное значение равно искомому, вернуть его индекс
    if arr[mid] == target:
        return mid
        # Если искомое значение больше серединного, искать дальше в правой половине
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
        # Если искомое значение меньше серединного, искать дальше в левой половине
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


# Запустить рекурсивную функцию
result = binary_search_recursive(arr, target, 0, len(arr) - 1)
if result != -1:
    print(f"Recursive: Искомое находится по индексу: {result}")
else:
    print("Recursive: Искомое не найдено")
