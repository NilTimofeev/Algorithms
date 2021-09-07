# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется
# как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
from collections import deque

first = list('1C52')
second = list('891')
result = []
first.reverse()  # перевернем, чтобы по индексу в цикле получить нужные цифры
second.reverse()
digits = '0123456789ABCDEF'

if len(first) < len(second):
    first, second = second, first   # количество итераций будет равно длине короткого числа

digit = 0   # четыре пишем, один в уме ... digit - это в уме
for i in range(len(second)):
    sum_ = digits.index(first[i]) + digits.index(second[i]) + digit
    result.append(digits[sum_ % 16])
    if sum_ >= 16:
        digit = 1
    else:
        digit = 0

diff_len = len(first) - len(second)
if diff_len:
    for i in first[-diff_len:]:
        sum_ = digits.index(i) + digit
        result.append(digits[sum_ % 16])
        if sum_ >= 16:
            digit = 1
        else:
            digit = 0
if digit:
    result.append('1')
result.reverse()
print(result)

