# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.


def count_num_2():
    """
    python -m timeit -n 1000 -s "import less4_1" "less4_1.count_num_2()"
    1000 loops, best of 5: 1.21 usec per loop
    """
    el = '3'
    text = '233 67 8 330 13'
    text = ''.join(text.split())
    count_el = 0
    for i in range(len(text)):
        if text[i] == el:
            count_el += 1


def count_num_1():
    """
    python -m timeit -n 1000 -s "import less4_1" "less4_1.count_num_1()"
    1000 loops, best of 5: 2.05 usec per loop

    """
    el = 3
    num_list = [233, 67, 8, 330, 13]
    count_el = 0
    for i in range(len(num_list)):
        while num_list[i] > 0:
            if num_list[i] % 10 == el:
                count_el += 1
            num_list[i] //= 10


"""
Вариант со строкой гораздо быстрее математических вычислений
"""
