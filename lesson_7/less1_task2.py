# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
# промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

from random import  randint
# функция слияния двух отсортированных списков
def merge_list(a, b):
    c = []
    N = len(a)
    M = len(b)

    i = 0
    j = 0
    while i < N and j < M:
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    c += a[i:] + b[j:]
    return c


# функция деления списка и слияния списков в общий отсортированный список
def split_and_merge_list(arr):
    middle = len(arr) // 2
    left = arr[:middle]     # деление массива на два примерно равной длины
    right = arr[middle:]

    if len(left) > 1: # если длина 1-го списка больше 1, то делим дальше
        left = split_and_merge_list(left)
    if len(right) > 1: # если длина 2-го списка больше 1, то делим дальше
        right = split_and_merge_list(right)

    return merge_list(left, right)   # слияние двух отсортированных списков в один


array = [randint(0, 50) for i in range(10)]
array = split_and_merge_list(array)

print(array)
