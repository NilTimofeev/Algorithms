# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется
# как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

# first = list('1C52')
# second = list('891')
# result = []
# first.reverse()  # перевернем, чтобы по индексу в цикле получить нужные цифры
# second.reverse()
# digits = '0123456789ABCDEF'
from collections import deque

def mult_hex(x, y):
    HEX_NUM = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
               0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
               10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    result = deque()
    spam = deque([deque() for _ in range(len(y))])

    x, y = x.copy(), deque(y)

    for i in range(len(y)):
        m = HEX_NUM[y.pop()]

        for j in range(len(x) - 1, -1, -1):
            spam[i].appendleft(m * HEX_NUM[x[j]])

        for _ in range(i):
            spam[i].append(0)

    transfer = 0

    for _ in range(len(spam[-1])):
        res = transfer

        for i in range(len(spam)):
            if spam[i]:
                res += spam[i].pop()

        if res < 16:
            result.appendleft(HEX_NUM[res])

        else:
            result.appendleft(HEX_NUM[res % 16])
            transfer = res // 16

    if transfer:
            result.appendleft(HEX_NUM[transfer])

    return list(result)


a = list('1C52')
b = list('891')
# print(a, b)



print(*a, '*', *b, '=', *mult_hex(a, b))