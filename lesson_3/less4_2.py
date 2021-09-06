# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""
При проверке задания мне предложили создать список, писать в него минимумы по столбцам.
Потом выбрать максимальный из списка. Перебрать небольшой массив нужно дополнительно
и добавить метод append(). Насколько он ресурсозатратный пока не знаю. Попробуем увидеть разницу.
"""
from random import randint

columns = 500
rows = 700
r_num = 30
matrix = [[randint(-r_num, r_num) for i in range(columns)] for j in range(rows)]



def max_of_min_1():
    """
    матрица 5 на 7: python -m timeit -n 1000 -s "import less4_2" "less4_2.max_of_min_1()"
    1000 loops, best of 5: 31.8 usec per loop

    матрица 500 на 700: python -m timeit -n 1000 -s "import less4_2" "less4_2.max_of_min_1()"
    1000 loops, best of 5: 27.5 msec per loop
    """
    max_of_min = -r_num
    for column in range(columns):
        min_el = matrix[0][column]
        for row in range(rows):
            if matrix[row][column] < min_el:
                min_el = matrix[row][column]
        if max_of_min < min_el:
            max_of_min = min_el


def max_of_min_2():
    """
    матрица 5 на 7: python -m timeit -n 1000 -s "import less4_2" "less4_2.max_of_min_2()"
    1000 loops, best of 5: 32.1 usec per loop

    матрица 500 на 700: python -m timeit -n 1000 -s "import less4_2" "less4_2.max_of_min_2()"
    1000 loops, best of 5: 27.5 msec per loop
    """
    max_of_min = -r_num
    mass = []
    for column in range(columns):
        min_el = matrix[0][column]
        for row in range(rows):
            if matrix[row][column] < min_el:
                min_el = matrix[row][column]
        mass.append(min_el)
    for el in mass:
        if el > max_of_min:
            max_of_min = el


"""
Разницы нет. Время выполнения почти одинаковое
"""