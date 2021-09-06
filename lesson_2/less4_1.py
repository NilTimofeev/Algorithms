# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.


def count_num_2():
    el = '3'
    text = '233 67 8 330 13'
    text = ''.join(text.split())
    count_el = 0
    for i in range(len(text)):
        if text[i] == el:
            count_el += 1
    print(f'цифра в числах встречается {count_el} раз')


count_num_2()


def count_num_1():
    el = 3
    num_list = [233, 67, 8, 330, 13]
    count_el = 0
    for i in range(len(num_list)):
        while num_list[i] > 0:
            if num_list[i] % 10 == el:
                count_el += 1
            num_list[i] //= 10
    print(f'цифра в числах встречается {count_el} раз')


count_num_2()
