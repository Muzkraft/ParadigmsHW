"""
Контекст
Ещё один известный и довольно эффективный алгоритм
сортировки массива - сортировка слиянием (merge sort).
Алгоритм делится на два этапа:
○ этап разбиения - массив разбивается на пару
массивов до тех пор, пока полученные массивы не
станут массивами длины 1 (состоящими из одного
элемента).
○ этап слияния - соединяем пары массивов в большие
массивы так, чтобы полученные массивы были
отсортированы.
● Ваша задача.
Реализовать сортировку слиянием на любом языке в любой
парадигме. На вход ваша программа получает массив из
чисел, а вернуть должна отсортированный массив.

"""


def merge_sort(arr):
    # Тривиальный случай. Условие выхода из рекурсии
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    # Recursive call, до тех пор пока не попадем в тривиальный случай
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    merged = []
    left_index = right_index = 0

    # поэлементная сортировка
    while left_index < len(left_half) and right_index < len(right_half):
        # текущий левый элемент меньше правого
        if left_half[left_index] < right_half[right_index]:
            merged.append(left_half[left_index])
            left_index += 1
        # текущий левый элемент НЕ меньше правого
        else:
            merged.append(right_half[right_index])
            right_index += 1

    # добавляем остатки в конец массива, если они есть
    merged.extend(left_half[left_index:])
    merged.extend(right_half[right_index:])

    return merged


arr = [1, 3, 4, 0, 6, 2, 8, 100, 55, 23, 234, 66, 99]
sorted_arr = merge_sort(arr)
print('Отсортированный массив: ', sorted_arr)
