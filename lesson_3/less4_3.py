# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.
"""
В первом варианте перебираем элементы, сравниваем их.
Во втором используем метод sorted, тогда минимальные элементы будут первыми в массиве.
Сравним результаты скорости выполнения.
"""

from random import randint

mass = [randint(1, 20) for i in range(15)]


def two_min_1():
    """
    python -m timeit -n 1000 -s "import less4_3" "less4_3.two_min_1()"
    1000 loops, best of 5: 796 nsec per loop
    """
    min_1 = mass[0]
    min_2 = mass[1]
    for el in mass:
        if el < min_1 and min_1 > min_2:
            min_1 = el
        elif el < min_2:
            min_2 = el


def two_min_2():
    """
    python -m timeit -n 1000 -s "import less4_3" "less4_3.two_min_2()"
    1000 loops, best of 5: 256 nsec per loop
    """
    mass.sort()
    min_1 = mass[0]
    min_2 = mass[1]


"""
Метод sorted работает втрое быстрее
"""
