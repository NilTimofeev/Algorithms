# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import randint

columns = 5
rows = 7
r_num = 30
matrix = [[randint(-r_num, r_num) for i in range(columns)] for j in range(rows)]

for row in matrix:
    for item in row:
        print(f'{item:>5}', end='')
    print()
print('-' * len(matrix[0] * 5))

max_of_min = -r_num
for column in range(columns):
    min_el = matrix[0][column]
    for row in range(rows):
        if matrix[row][column] < min_el:
            min_el = matrix[row][column]
    print(f'{min_el:>5}', end='')
    if max_of_min < min_el:
        max_of_min = min_el
print("\n"f'Максимальный из минимальных в каждом столбце: {max_of_min}')
