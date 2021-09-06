# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.

from random import randint

mass = [randint(1, 20) for i in range(15)]


def two_min_1():
    min_1 = mass[0]
    min_2 = mass[1]
    for i in range(2, len(mass)):
        if mass[i] < min_1 and min_1 > min_2:
            min_1 = mass[i]
        elif mass[i] < min_2:
            min_2 = mass[i]


def two_min_2():
    mass.sort()
    min_1 = mass[0]
    min_2 = mass[1]

