# # O(n^2) пузырек
# import random
#
# size = 10
# array = [i for i in range(size)]
# random.shuffle(array)
# print(array)
#
# n = 1
# while n < len(array):
#     for i in range(len(array) - n):
#         if array[i] > array[i + 1]:
#             array[i], array[i + 1] = array[i + 1], array[i]
#     n += 1
# print(array)


# сортировка выбором O(n^2)
# import random
# size = 10
# array = [i for i in range(size)]
# random.shuffle(array)
# print(array)
#
#
# def selection_sort(arr):
#     for i in range(len(array)):
#         idx_min = i
#         for j in range(i + 1, len(array)):
#             if array[j] < array[idx_min]:
#                 idx_min = j
#         array[i], array[idx_min] = array[idx_min], array[i]
#
#
# selection_sort(array)
# print(array)


# Вставками O(n^2)
# import random
# size = 10
# array = [i for i in range(size)]
# random.shuffle(array)
# print(array)
#
#
# def insertion_sort():
#     for i in range(1, len(array)):
#         spam = array[i]
#         j = i
#         while array[j - 1] > spam and j > 0:
#             array[j] = array[j - 1]
#             j -= 1
#
#         array[j] = spam
#
#
# insertion_sort()
# print(array)


# Шелла O(n^2) -  O(n^3/2) если однинаковые элементы, то их порядок не сохранится
# 1, 4, 10, 23, 57, 132, 301, 701, 1750 до 4000 элементов
# import random
#
# size = 10
# ar = [i for i in range(size)]
# random.shuffle(ar)
# print(ar)
#
#
# def shell_sort(array):
#     assert len(array) < 4000, 'массив слишком большой'
#
#     def new_increment(a):
#         inc = [1, 4, 10, 23, 57, 132, 301, 701, 1750]
#         while len(ar) <= inc[-1]:
#             inc.pop()
#         while len(inc) > 0:
#             yield inc.pop()
#
#     for inc in new_increment(array):
#         for i in range(inc, len(array)):
#             for j in range(i, inc - 1, -inc):
#                 if array[j - inc] <= array[j]:
#                     break
#                 array[j], array[j - inc] = array[j - inc], array[j]
#
#
# shell_sort(ar)
# print(ar)


# Сортировка Хаала
# import random
# size = 10
# array = [i for i in range(size)]
# random.shuffle(array)
# print(array)
#
#
# def quick_sort(array):
#     if len(array) <= 1:
#         return array
#
#     pivot = random.choice(array)
#     s_ar = []
#     m_ar = []
#     l_ar = []
#
#     for item in array:
#         if item < pivot:
#             s_ar.append(item)
#         elif item > pivot:
#             l_ar.append(item)
#         elif item == pivot:
#             m_ar.append(item)
#         else:
#             raise Exception('случилось непредвиденное')
#     return quick_sort(s_ar) + quick_sort(m_ar) + quick_sort(l_ar)


# print(quick_sort(array))

# без использования дополнительной пямяти


# def quick_sort_no_memory(array, fst, lst):
#     if len(array) <= 1:
#         return array
#
#     pivot = array[random.randint(fst, lst)]
#     i, j = fst, lst
#     while i <= j:
#         while array[i] < pivot:
#             i += i
#         while array[j] > pivot:
#             j -= 1
#         if i <= j:
#             array[i], array[j] = array[j], array[i]
#             i, j = i + 1, j - 1
#     quick_sort_no_memory(array, fst, j)
#     quick_sort_no_memory(array, i, lst)
#
#
# quick_sort_no_memory(array, 0, len(array) - 1)
# print(array)



# Timsort O(n * log n)

# с использованием ключа
from collections import namedtuple
from operator import attrgetter

Person = namedtuple('Person', 'name age')
p1 = Person('Vasya', 25)
p2 = Person('Kolya', 30)
p3 = Person('Olya', 23)

people = [p1, p2, p3]
print(people)
result = sorted(people, key=attrgetter('age'))
print(result)


