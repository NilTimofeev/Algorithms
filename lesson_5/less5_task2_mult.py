from collections import deque

first = list('20A4')
second = list('B15')
digits = '0123456789ABCDEF'
# На этот раз будем использовать deque, чтобы не преворачивать результат, а использовать appendleft.
# Цифру берем не только по индексу, как прежде, но и с помощью pop. С deque метод работает быстрее, чем с list
result = deque()
temp = deque()

for i in range(len(second)):
    temp.append(deque())   # домавим очередь для нового слагаемого
    s = digits.index(second.pop())

    for j in range(len(first) - 1, -1, -1):
        f = digits.index(first[j])
        temp[i].appendleft(s * f)

    for _ in range(i):   # добавим нулей, чтобы сместить разряды очередного слагаемого на единицу
        temp[i].append(0)
        print(temp)


digit = 0

for i in range(len(temp[-1])):   # самая длинная очередь, последняя
    res = 0
    for j in range(len(temp)):
        if temp[j]:
            res += temp[j].pop()
    res += digit
    result.appendleft(digits[res % 16])
    digit = res // 16

if digit:
    result.appendleft(digit)
print(result)

