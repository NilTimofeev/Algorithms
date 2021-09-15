# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
# промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

from random import  randint
# функция слияния двух отсортированных списков


def split_and_merge_list(arr):
    middle = len(arr) // 2
    left = arr[:middle]     # деление массива на два примерно равной длины
    right = arr[middle:]

    if len(left) > 1: # если длина 1-го списка больше 1, то делим дальше
        left = split_and_merge_list(left)
    if len(right) > 1: # если длина 2-го списка больше 1, то делим дальше
        right = split_and_merge_list(right)

    result = []

    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:] + right[j:]

    return result


array = [randint(0, 50) for i in range(10)]
print(array)

array = split_and_merge_list(array)
print(array)
