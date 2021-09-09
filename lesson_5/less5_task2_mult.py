from collections import deque

first = list('C4F')
second = list('A2')
digits = '0123456789ABCDEF'
"""
1. Умножаем цифру из second на все цифры из first на каждой итерации. Значит 2 цикла for (внешний для second и 
внутренний для first). На каждой итерации внешнего получаем новое слагаемое.
2. Разряды слагаемых нужно сместить, иначе код будет громоздкий и непонятный, с костылями, как в задаче суммы.
Добавим нулей кратно итерации внешнего цикла (каждое последующее слагаемое +0). Поэтому не можем перебрать second с
конца как first (нужен номер итерации). Бедем рвать second с помощью pop.
3. Используем deque где необходим метод appendleft, чтобы не вращать числа (формирование слагаемого и результата)
4. При сложении пробежимся по числам столько раз сколько цифр в самом длинном слагаемом (в последнем много нулей).
По индексам не обратимся, выйдем за границы. Будем проверять есть ли еще число и рвать с помощью pop
"""

result = deque()
temp = deque()

for i in range(len(second)):
    temp.append(deque())   # домавим очередь для нового слагаемого
    s = digits.index(second.pop())

    for j in range(len(first) - 1, -1, -1):
        f = digits.index(first[j])
        temp[i].appendleft(s * f)

    for _ in range(i):   # добавим нулей, чтобы сместить разряды очередного слагаемого на один
        temp[i].append(0)


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

