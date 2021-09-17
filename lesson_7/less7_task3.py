"""
3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
медианы, в другой — не больше медианы.
Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно, используйте метод
сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).



В решении показаны алгоритмы выбора и сортировки Хоара.

Выбирается опорный элемент (в данном случае случайно), остальные числа разделяются на большие и меньшие опорного.
В случае сортировки каждая ветвь сортируется рекурсивно.
В алгоритме выбора рекурсия выполняется только в одну сторону, в ту, где искомый элемент.
"""

import random

m = 5
array = random.sample(range(0, 50), 2 * m + 1)
print(f'Исходный массив  {array}')
m = len(array) // 2


def quick_select(arr, m):
    small, large = [], []
    pivot = random.choice(arr)

    for el in arr:
        if el < pivot:
            small.append(el)
        elif el > pivot:
            large.append(el)

    if m < len(small):
        return quick_select(small, m)
    elif m < len(small) + 1:
        return pivot
    else:
        return quick_select(large, m - len(small) - 1)


print(f'Медиана, полученная алгоритмом выбора Хоара: {quick_select(array, m)}\n')


def quicksort(arr):

    if len(arr) <= 1:
        return arr

    small, large, piv = [], [], []
    pivot = random.choice(arr)

    for el in arr:
        if el < pivot:
            small.append(el)
        elif el > pivot:
            large.append(el)
        else:
            piv.append(el)

    return quicksort(small) + piv + quicksort(large)


res = quicksort(array)
print(f'Отсортированный массив:  {res}')
print(f'Медиана - средний элемент в отсортированном массиве: {res[m]}')
