# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк. Программа должна
# вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

# 5x4 это 5 строк и 4 столбца?
matrix = [[''] * 4 for _ in range(5)]

for row in range(5):
    result = 0
    for column in range(3):
        matrix[row][column] = int(input(f'строка {row + 1} столбец {column + 1}: '))
        result += matrix[row][column]
    matrix[row][3] = result


for row in matrix:
    for item in row:
        print(f'{item:>5}', end='')
    print()



