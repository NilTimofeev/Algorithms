from random import randint


def max_of_min_1():
    columns = 5
    rows = 7
    r_num = 30
    matrix = [[randint(-r_num, r_num) for i in range(columns)] for j in range(rows)]
    max_of_min = -r_num

    for column in range(columns):
        min_el = matrix[0][column]
        for row in range(rows):
            if matrix[row][column] < min_el:
                min_el = matrix[row][column]
        print(f'{min_el:>5}', end='')
        if max_of_min < min_el:
            max_of_min = min_el


def max_of_min_2():
    columns = 5
    rows = 7
    r_num = 30
    mass = []
    matrix = [[randint(-r_num, r_num) for i in range(columns)] for j in range(rows)]
    max_of_min = -r_num

    for column in range(columns):
        min_el = matrix[0][column]
        for row in range(rows):
            if matrix[row][column] < min_el:
                min_el = matrix[row][column]
        mass.append(min_el)
    for el in mass:
        if el > max_of_min:
            max_of_min = el
