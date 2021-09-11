import sys
print(sys.version, sys.platform)
# 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] win32

# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

el_list = []


def show_size(elements):
    for el in elements:
        print(f'type - {el.__class__}, size - {sys.getsizeof(el)}, odj - {el}')
    # if hasattr(x, '__iter__'):
    #     if hasattr(x, '__items__'):
    #         for xx in x.items():
    #             show_size(x, level + 1)
    #     elif not isinstance(x, str):
    #         for xx in x:
    #             show_size(x, level + 1)


def count_num():
    n = 1 #int(input('сколько чисел введем?: '))
    el = 3 #int(input('какую цифру посчитать?: '))
    count_el = 0
    for i in range(n):
        num = 34563213 #int(input('введите число: '))
        while num > 0:
            if num % 10 == el:
                count_el += 1
            num //= 10
    print(f'цифра в числах встречается {count_el} раз')

    print(locals().keys())
    for el_name in dir():
        if not el_name.startswith('__'):
            el_list.append(locals()[el_name])
    show_size(el_list)


def count_num_2():
    n = 1 #int(input('сколько чисел введем?: '))
    el = '3' #int(input('какую цифру посчитать?: '))
    count_el = 0
    for i in range(n):
        num = '34563213' #int(input('введите число: '))
        while num > 0:
            if num % 10 == el:
                count_el += 1
            num //= 10
    print(f'цифра в числах встречается {count_el} раз')

    print(locals().keys())
    for el_name in dir():
        if not el_name.startswith('__'):
            el_list.append(locals()[el_name])
    show_size(el_list)





count_num()

