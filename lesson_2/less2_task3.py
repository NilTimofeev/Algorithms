# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например,
# если введено число 3486, надо вывести 6843.

num = int(input('введите число: '))
res = ''
while num > 0:
    res = f'{res}{num % 10}'
    num //= 10
print(res)
