# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется
# как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

first = list('A2')
second = list('C4F')
result = []
first.reverse()
second.reverse()
digits = '0123456789ABCDEF'

if len(first) < len(second):
    first, second = second, first
print(first)
print(second)

digit = 0
for i in range(len(second)):
    n1 = digits.index(first[i])
    n2 = digits.index(second[i])
    print(n1, n2)
    res = (n1 + n2 + digit) % 16
    print(res)
    if n1 + n2 >= 16:
        digit = 1
    else:
        digit = 0
    print(digit)



# def toHex(dec):
#     x = (dec % 16)
#     digits = "0123456789ABCDEF"
#     rest = dec / 16
#     if rest == 0:
#         return digits[x]
#     return toHex(rest) + digits[x]


# def toHex(decimal):
#     hex_str = ''
#     digits = "0123456789ABCDEF"
#     if decimal == 0:
#         return '0'
#
#     while decimal != 0:
#         hex_str += digits[decimal % 16]
#         decimal = decimal // 16
#
#     return hex_str[::-1]  # reverse the string
#
#
# numbers = [0, 16, 20, 45, 255, 456, 789, 1024]
# print([toHex(x) for x in numbers])

